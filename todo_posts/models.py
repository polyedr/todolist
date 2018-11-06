from django.db import models
from django.conf import settings
from django.urls import reverse


class Todo_post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'
    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )

    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_post_detail', args=[str(self.id)])


class Comment(models.Model):
    todo_post = models.ForeignKey(
        Todo_post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('todo_post_list')
