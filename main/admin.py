from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category')
    list_display_links = ('id', 'title', 'author', 'category')
    search_fields = ('title', 'author', 'category')
    filter_horizontal = ('tags',)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email')
    list_display_links = ('id', 'phone', 'email')
    search_fields = ('phone', 'email')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name', 'email', 'phone')
    search_fields = ('name', 'email')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Resume)
admin.site.register(Skills)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
