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

        "one_star_count": one_star_rating.count(),
        "two_star_count": two_star_rating.count(),
        "three_star_count": three_star_rating.count(),
        "four_star_count": four_star_rating.count(),
        "five_star_count": five_star_rating.count(),

        "one_star_percent": int((total_reviews and one_star_rating.count()/total_reviews or 0) * 100),
        "two_star_percent": int((total_reviews and two_star_rating.count()/total_reviews or 0) * 100),
        "three_star_percent": int((total_reviews and three_star_rating.count()/total_reviews or 0) * 100),
        "four_star_percent": int((total_reviews and four_star_rating.count()/total_reviews or 0) * 100),
        "five_star_percent": int((total_reviews and five_star_rating.count()/total_reviews or 0) * 100),
    }
    return render(request, "reviews.html", context)
    

@login_required(login_url="authentication:login_user")
def add_review(request, id):
    post = PostProperti.objects.get(pk=id)
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.user = request.user
        review.post = PostProperti.objects.get(pk=id)
        review.save()
        messages.success(request, 'Your review has been successfully added!')
        return HttpResponseRedirect(reverse('review:show_reviews', kwargs={"id": id}))
    else:
        messages.error(request, 'Please complete all input fields to continue.')

    context = {'form': form, "post": post}
    return render(request, "add_review.html", context)

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
