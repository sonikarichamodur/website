from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import Http404
from blog.models.comment import Comment
from blog.models.post import Post
from django.contrib.auth.mixins import PermissionRequiredMixin


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the username
        comments = Comment.objects.filter(post=self.kwargs['pk'])
        context['comments'] = comments
        return context


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/create_post.html'
    login_url = reverse_lazy('login')
    permission_required = "post.post_gui_can_post"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/create_post.html'
    login_url = reverse_lazy('login')
    permission_required = "post.post_gui_can_update"

    def test_func(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('login')
    permission_required = "post.post_gui_can_delete"

    def test_func(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user
