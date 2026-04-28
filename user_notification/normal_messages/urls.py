from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.user_notifications, name='notifications'),
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('normal_messages.urls')),
]