from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib import messages
from home.models import Profile
from .forms import PostModelForm, CommentModelForm

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/deletepost.html'
    successs_url = reverse_lazy('home:home')
    
    def get_Object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request, 'You are not the author of this post')
        return obj

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'posts/updatepost.html'
    # fields = ['content', 'image']
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)

        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, 'You are not the author of this post')
            return super().form_invalid(form)