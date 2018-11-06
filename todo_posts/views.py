from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from . import models


class Todo_postListView(ListView):
    model = models.Todo_post
    template_name = 'todo_post_list.html'
    login_url = 'account_login'

    def get_queryset(self):
        todo_post_list = models.Todo_post.objects.filter(author=self.request.user)
        return todo_post_list


class Todo_postDetailView(DetailView):
    model = models.Todo_post
    template_name = 'todo_post_detail.html'
    login_url = 'account_login'


class Todo_postCreateView(LoginRequiredMixin, CreateView):
    model = models.Todo_post
    template_name = 'todo_post_new.html'
    fields = ['title', 'body', ]
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Todo_postUpdateView(UpdateView):
    model = models.Todo_post
    fields = ['title', 'body', ]
    template_name = 'todo_post_edit.html'
    login_url = 'account_login'


class Todo_postDeleteView(DeleteView):
    model = models.Todo_post
    template_name = 'todo_post_delete.html'
    success_url = reverse_lazy('todo_post_list')
    login_url = 'account_login'
