from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post_properti.models import PostProperti
from userData.models import UserData
from django.core import serializers
from django.urls import reverse

from userData.models import UserData
from .forms import PostPropertiForm, FilterForm

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        user = request.user
        nama_properti = request.POST.get("nama")
        deskripsi_properti = request.POST.get("deskripsi")
        foto_properti = request.POST.get("foto")
        kota_properti = request.POST.get("kota")
        negara_properti = request.POST.get("negara")
        kode_pos_properti = request.POST.get("kodepos")

        post = PostProperti(
            user = user,
            nama_properti = nama_properti,
            deskripsi_properti = deskripsi_properti,
            foto_properti = foto_properti,
            kota_properti = kota_properti,
            negara_properti = negara_properti,
            kode_pos_properti = kode_pos_properti,
        )

        post.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def new_post(request):
    if request.method == "POST":
        user = request.user
        nama = request.POST.get('nama', '')
        deskripsi = request.POST.get('deskripsi', '')
        foto = request.POST.get('foto', '')
        kota = request.POST.get('kota', '')
        negara = request.POST.get('negara', '')
        kodepos = request.POST.get('kodepos', '')

        if not (nama and deskripsi and foto and kota and negara and kodepos):
            return HttpResponseBadRequest("Missing required fields")

        form_data = {
            'user': user,
            'nama_properti': nama,
            'deskripsi_properti': deskripsi,
            'foto_properti': foto,
            'kota_properti': kota,
            'negara_properti': negara,
            'kode_pos_properti': kodepos,
        }

        form = PostPropertiForm(form_data)

        if form.is_valid():
            post_properti_instance = form.save(commit=False)
            post_properti_instance.user = request.user
            post_properti_instance.save()
            return redirect(reverse('show_user_posts'))
        else:
            return render(request, "new_post.html", {'form': form})

    return render(request, "new_post.html")

def show_all_posts(request):
    return render(request, 'all_posts.html')

def show_post_detail(request, id):
    post = PostProperti.objects.get(pk=id)
    user_data = UserData.objects.get(user=post.user)

    context = {
        'post': post,
        'nomor_wa' : user_data.nomorWA
    }

    return render(request, 'post_detail.html', context)

def all_posts_json(request):
    posts = PostProperti.objects.all()
    return HttpResponse(serializers.serialize('json', posts))

# Method edit post properti
@login_required
def edit_post(request, id):
    post = PostProperti.objects.get(pk=id)

    if request.method == 'POST':
        edit_form = PostPropertiForm(request.POST, request.FILES, instance=post)
        if edit_form.is_valid():
            try:
                edit_form.save()
                messages.success(request, 'Post updated successfully.')
                return redirect('show_user_posts')
            except Exception as e:
                messages.error(request, f'Error updating post: {e}')
        else:
            messages.error(request, 'Error updating post. Please correct the form errors.')
    else:
        edit_form = PostPropertiForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': edit_form, 'post_properti': post})

# Method untuk show post yang dibuat user yang sedang login
@login_required
def show_user_posts(request):
    user_logged_in = request.user
    data_post_properti = PostProperti.objects.filter(user=user_logged_in)

    context = {
        'list_properti' : data_post_properti,
    }
    return render(request, 'show_user_posts.html', context)

# Method untuk mencari post berdasarkan nama properti
def search_post_by_name(request):
    if request.method == 'POST':
        searched_post = request.POST.get('searched_post')
        posts = PostProperti.objects.filter(nama_properti__icontains=searched_post)

        if posts.exists():
            messages.success(request, 'Search successful.')
        else:
            messages.info(request, 'Properti yang anda cari tidak tersedia.')

        return render(request, 'search_post.html', {'posts': posts, 'searched_post': searched_post})
    else:
        return render(request, 'search_post.html')

# Method untuk memfilter post berdasarkan negara dan kota
# @login_required
def filter_posts(request):
    form = FilterForm()

    negara_choices = PostProperti.objects.values_list('negara_properti', flat=True).distinct()
    form.fields['negara'].choices = [(negara, negara) for negara in negara_choices]

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            negara = form.cleaned_data['negara']
            kota_choices = PostProperti.objects.filter(negara_properti=negara).values_list('kota_properti', flat=True).distinct()
            form.set_kota_choices([(kota, kota) for kota in kota_choices])

            kota = form.cleaned_data['kota'] if 'kota' in form.cleaned_data else None

            if kota:
                posts = PostProperti.objects.filter(negara_properti=negara, kota_properti=kota)
            else:
                posts = PostProperti.objects.filter(negara_properti=negara)

            return render(request, 'filtered_posts.html', {'posts': posts, 'form': form})

    return render(request, 'filter_posts.html', {'form': form})