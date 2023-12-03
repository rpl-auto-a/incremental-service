from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from post_properti.models import PostProperti
from reviewrating.models import Review
from reviewrating.forms import ReviewForm

# Create your views here.
def show_reviews(request, id):
    reviews = Review.objects.filter(post=id)
    post = PostProperti.objects.get(pk=id)
    total_reviews = reviews.count()

    one_star_rating = reviews.filter(rating=1)
    two_star_rating = reviews.filter(rating=2)
    three_star_rating = reviews.filter(rating=3)
    four_star_rating = reviews.filter(rating=4)
    five_star_rating = reviews.filter(rating=5)

    context = {
        "user": request.user,
        "post": post,
        "reviews": reviews,
        "total_reviews": total_reviews,

        "one_star_percent": int(one_star_rating.count()/total_reviews * 100),
        "two_star_percent": int(two_star_rating.count()/total_reviews * 100),
        "three_star_percent": int(three_star_rating.count()/total_reviews * 100),
        "four_star_percent": int(four_star_rating.count()/total_reviews * 100),
        "five_star_percent": int(five_star_rating.count()/total_reviews * 100),
    }
    return render(request, "reviews.html", context)
    

@login_required(login_url="authentication:login_user")
def add_review(request, id):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('review:show_reviews'))
    
    context = {'form': form}
    return render(request, "add_review.html", context)

    """ if request.method == 'POST':
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
    return HttpResponseNotFound() """

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
