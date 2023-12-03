from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reviewrating.models import Review
from post_properti.models import PostProperti
from django.core import serializers
from .forms import ReviewForm

# Create your views here.
def show_reviews(request):
    reviews = Review.objects.filter(post=1)
    total_reviews = reviews.count()
    context = {
        "reviews": reviews,
        "test": "test",
        "total_reviews": total_reviews,
        "angka": int(153/400 * 100),
        "star": 5,
    }
    return render(request, "reviews.html", context)
    

@login_required(login_url="authentication:login_user")
def add_review(request, post_id):
    if request.method == 'POST':
        user = request.user
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        post = PostProperti.objects.get(pk=post_id)

        review = Review(
            user = user,
            rating = rating,
            review = review,
            post = post
        )

        review.save()
        return JsonResponse({'message': 'Review created successfully'}, status=200)
    return HttpResponseNotFound()

def delete_review(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)

        if request.user == review.user:
            review.delete()
            return JsonResponse({'message': 'Review deleted successfully'}, status=200)
        else:
            return JsonResponse({'message': 'You are not authorized to delete this review'}, status=403)
    except Review.DoesNotExist:
        return JsonResponse({'message': 'Review not found'}, status=404)
    
# Method untuk mengedit ReviewRating
@login_required
def edit_review(request, review_id):
    review = Review.objects.get(pk=review_id)

    if request.method == 'POST':
        edit_form = ReviewForm(request.POST, request.FILES, instance=review)
        if edit_form.is_valid():
            try:
                edit_form.save()
                messages.success(request, 'Review updated successfully.')
                return redirect('show_reviews')
            except Exception as e:
                messages.error(request, f'Error updating review: {e}')
        else:
            messages.error(request, 'Error updating review. Please correct the form errors.')
    else:
        edit_form = ReviewForm(instance=review)
    
    return render(request, 'edit_review.html', {'form': edit_form, 'review': review})
