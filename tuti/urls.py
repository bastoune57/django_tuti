from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('articles/', include('books.urls')),
    path('admin/', admin.site.urls),
        ]
