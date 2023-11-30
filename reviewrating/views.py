from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reviewrating.models import Review
from post_properti.models import PostProperti
from django.core import serializers

# Create your views here.
@login_required
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

def get_reviews(request, post_id):
    post = PostProperti.objects.get(pk=post_id)
    reviews = Review.objects.filter(post=post_id)

def reviews_json(request, post_id):
    reviews = Review.objects.filter(post=post_id)
    return HttpResponse(serializers.serialize('json', reviews))

def delete_review(request, id):
    try:
        review = Review.objects.get(pk=id)

        if request.user == review.user:
            review.delete()
            return JsonResponse({'message': 'Review deleted successfully'}, status=200)
        else:
            return JsonResponse({'message': 'You are not authorized to delete this review'}, status=403)
    except Review.DoesNotExist:
        return JsonResponse({'message': 'Review not found'}, status=404)
    