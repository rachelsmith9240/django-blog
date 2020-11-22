from django.contrib import admin
from blogging.models import Post, Category


class PostsInLine(admin.TabularInline):
    model = Post.categories.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostsInLine,
    ]


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostsInLine,
    ]
    exclude = ("categories",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
