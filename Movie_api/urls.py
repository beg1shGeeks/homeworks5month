from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('api/v1/directors/', views.director_list_api_view),
    path('admin/', admin.site.urls),
    path('api/v1/directors/<int:id>/', views.director_detail_api_view),
    path('api/v1/products/', views.movie_list_api_view),
    path('api/v1/products/<int:id>/', views.movie_detail_api_view),
    path('api/v1/reviews/', views.review_list_api_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
]