from django.contrib import admin
from .models import Post

#Register a model in admin panel and allow to interact with it
#with admin user
admin.site.register(Post)