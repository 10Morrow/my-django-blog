from django.contrib import admin
from django.urls import path
from django.urls import include

app_name = 'basic'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_blog.urls')),
    path('user/', include('users.urls')),
]
