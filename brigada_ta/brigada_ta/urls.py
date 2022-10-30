from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('objects.urls', namespace='objects')),
    path('admin/', admin.site.urls),
]
