from django.urls import path
from .views import MovieList, MovieDetail,MovieCategory

app_name = "movie"

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
]
