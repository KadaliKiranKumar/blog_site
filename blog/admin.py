from django.contrib import admin
from blog.models import Blog, Author, Entry, Websites

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Websites)
