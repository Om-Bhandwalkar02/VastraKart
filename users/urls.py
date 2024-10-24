from django.urls import path, include
from . import views

urlpatterns = [
path('accounts/', include('django.contrib.auth.urls')),
path('register/', views.register, name='register'),

]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check_username'),
]

urlpatterns += htmx_urlpatterns