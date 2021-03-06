from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
import requests
from .models import Profile, Relationship
from .forms import ProfileModelForm
from posts.forms import PostModelForm, CommentModelForm
from posts.models import Post, Like
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.models import User

API_KEY = '985d088b7d85476a9e834a2d8870b5b3' #newsapi.org

def home(request):
    if request.user.is_authenticated:
        qs = Post.objects.all()
        profile = Profile.objects.get(user=request.user)
        post_added = False

        #post form and comment form
        p_form = PostModelForm()
        c_form = CommentModelForm()

        if 'p_form_submit' in request.POST:
            p_form = PostModelForm(request.POST, request.FILES)
            if p_form.is_valid():
                instance = p_form.save(commit=False)
                instance.author = profile
                instance.save()
                print("Done bro")
                p_form = PostModelForm()
                post_added = True

        if 'c_form_sumbit' in request.POST:
            c_form = CommentModelForm(request.POST)
            if c_form.is_valid():
                instance = c_form.save(commit=False)
                instance.user = profile
                instance.post = Post.objects.get(id=request.POST.get('post_id'))
                instance.save()
                print("Comment Posted")
                c_form = CommentModelForm()

        context = {
            'qs': qs,
            'profile' : profile,
            'p_form': p_form,
            'c_form': c_form,
            'post_added': post_added,
        }
        return render(request, 'home/home.html', context)

    else:
        return redirect('/')

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Dislike'
            else:
                like.value = 'Like'

        else:
            like.value = 'Like'

            post_obj.save()
            like.save()

        data = {
            'value': like.value,
            'likes': post_obj.liked.all().count(),
        }
        return JsonResponse(data, safe=False)


    return redirect('home')


def newspaper(request):
    if request.user.is_authenticated:
        query = request.GET.get('query')
        url = f'https://newsapi.org/v2/everything?q=({query} AND india)&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

        context = {
            'articles': articles
        }
        return render(request, 'home/newspaper.html', context)
    else:
        return redirect('/')

def marketplace(request):
    if request.user.is_authenticated:
        return render(request, 'home/marketplace.html')
    else:
        return redirect('/')

def notifications(request):
    if request.user.is_authenticated:
        return render(request, 'home/notifications.html')
    else:
        return redirect('/')

def profile(request):
    if request.user.is_authenticated: 
        obj = Profile.objects.get(user=request.user)

        context = {
            'obj': obj,
        }
        return render(request, 'home/profile.html', context)
                                   
    else:
        return redirect('/')

def logout_view(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('/')

def settings(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
        done = False

        if form.is_valid():
            form.save()
            return redirect('/profile')

        context = {
            'form': form,
            'done': done,
        }
        return render(request, 'home/settings.html', context)
    else:
        return redirect('/')

def invited_received_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        qs = Relationship.objects.invitations_received(profile)

        context = {
            'qs': qs,
        }  

        return render(request, 'home/notifications.html', context)
    else:
        return redirect('/')

def profile_list_view(request):
    if request.user.is_authenticated:
        user=request.user
        qs = Profile.objects.get_all_profiles(user)

        context = {
            'qs': qs,
        }  

        return render(request, 'home/profile_list.html', context)
    else:
        return redirect('/')

def invite_profile_list_view(request):
    if request.user.is_authenticated:
        user=request.user
        qs = Profile.objects.get_all_profiles_to_invite(user)

        context = {
            'qs': qs,
        }  

        return render(request, 'home/invite_list.html', context)
    else:
        return redirect('/')

class ProfileListView(ListView):
    model = Profile
    template_name = 'home/profile_list.html'
    context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileListView, self).get_context_data(*args, **kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for i in rel_r:
            rel_receiver.append(i.receiver.user)
        for i in rel_s:
            rel_sender.append(i.sender.user)
            
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True

        return context

def send_invatation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pk = request.POST.get('profile_pk')
            user = request.user
            sender = Profile.objects.get(user=user)
            receiver = Profile.objects.get(pk=pk)
            rel = Relationship.objects.create(sender=sender, receiver=receiver, status='send')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('/all-profiles')
    else:
        return redirect('/')