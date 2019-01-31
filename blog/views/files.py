from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from blog.models.files import Files
from django.shortcuts import get_object_or_404

# class FilesView(generic.DetailView):
#     model = Files
#     template_name = 'blog/files.html'
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in the username
#         return context
#
# def filesGet(request,pk):
#     fil =get_object_or_404(Files,pk=pk)
#     return
#
#
# class FilesCreate(LoginRequiredMixin, CreateView):
#     model = Files
#     fields = ['title', 'filename']
#     template_name = 'blog/create_file.html'
#     login_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.fil =
#         form.instance.
#         return super().form_valid(form)
#
#
# class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'body']
#     template_name = 'blog/create_post.html'
#     login_url = reverse_lazy('login')
#
#     def test_func(self):
#         return Post.objects.get(id=self.kwargs['pk']).user == self.request.user
#
#
# class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:home')
#     login_url = reverse_lazy('login')
#
#     def test_func(self):
#         return Post.objects.get(id=self.kwargs['pk']).user == self.request.user
