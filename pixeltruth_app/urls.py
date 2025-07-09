from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('results/<int:image_id>/', views.results, name='results'),
    path('recent/', views.recent_results, name='recent_results'),  # if you add this view
]
