import django_filters
from todo_posts.models import Todo_post


class Todo_postFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Todo_post
        fields = ['priority', 'is_ready', ]

    @property
    def qs(self):
        parent = super(Todo_postFilter, self).qs
        author = getattr(self.request, 'user', None)

        return parent.filter(author=author)
