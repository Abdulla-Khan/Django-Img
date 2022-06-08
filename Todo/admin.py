from django.contrib import admin
from .models import PostFeed, Todo


class PostImage(admin.StackedInline):
    model = PostFeed


@admin.register(Todo)
class Todo(admin.ModelAdmin):
    inlines = [PostImage]

    class Meta:
        model = Todo
