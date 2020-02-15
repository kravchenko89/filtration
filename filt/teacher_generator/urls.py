from django.contrib import admin
from django.urls import path, include
import humans.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comm/', include('humans.urls')),
]

handler404 = humans.views.handler404
handler500 = humans.views.handler500