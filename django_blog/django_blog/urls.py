from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('main_blog.urls')),
    path('user/', include('users.urls')),
]
