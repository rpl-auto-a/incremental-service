from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post_properti.models import PostProperti
from django.core import serializers
from .forms import PostPropertiForm

# Create your views here.



# Method edit post properti
@login_required
def edit_post(request, post_id):
    post = PostProperti.objects.get(pk=post_id)

    if request.method == 'POST':
        edit_form = PostPropertiForm(request.POST, request.FILES, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('post_detail', post_id=post.id)     # Placeholder sementara untuk kembali ke halaman post detail

        else:
            edit_form = PostPropertiForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': edit_form, 'post_properti': post})    # Placeholder sementara untuk kembali ke halaman edit post

# Method untuk show post yang dibuat user yang sedang login
@login_required
def show_user_post(request):
    user_logged_in = request.user
    data_post_properti = PostProperti.objects.filter(user=user_logged_in)

    context = {
        'list_todolist_user' : data_post_properti,
    }
    return render(request, context)

# Method untuk mencari post berdasarkan nama properti
def search_post_by_name(request):
    if request.method == 'POST':
        searched_post = request.POST.get('searched_post')
        posts = PostProperti.objects.filter(nama_properti__icontains=searched_post)
        return render(request, 'search_post.html', {'posts': posts, 'searched_post': searched_post})
    else:
        return render(request, 'search_post.html')

