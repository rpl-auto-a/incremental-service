from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from post_properti.models import PostProperti
from django.core import serializers
from userData.models import UserData

# Create your views here.
@login_required
def add_favorite(request, post_id):
    if request.method == 'POST':
        try:
            user = request.user
            post = PostProperti.objects.get(pk=post_id)
            user_data = UserData.objects.get(user=user)
            user_data.postFavorit.add(post)
            user_data.save()
            return JsonResponse({'message': 'Post added to favorites successfully'}, status=200)
        except PostProperti.DoesNotExist:
            return JsonResponse({'message': 'Post not found'}, status=404)
    return HttpResponseNotFound()

@login_required
def delete_favorite(request, id):
    try:
        user = request.user
        user_data = UserData.objects.get(user=user)
        post = PostProperti.objects.get(pk=id)
        user_data.postFavorit.remove(post)
        user_data.save()
        return JsonResponse({'message': 'Post deleted from favorites successfully'}, status=200)
    except PostProperti.DoesNotExist:
        return JsonResponse({'message': 'Post not found'}, status=404)
    
@login_required
def favorites_json(request):
    user = request.user
    user_data = UserData.objects.get(pk=user.id)
    favorites = user_data.postFavorit.all()
    return HttpResponse(serializers.serialize('json', favorites), content_type='application/json')