from django.urls import path
from .views import MovieList,MovieDetail,MovieGenre,MovieCategory,MovieLanguage,MovieYear,MovieSearch

app_name = "movie"

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    # path('all_movies/', AllMovies.as_view(), name='all_movie_list'),
    # path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('genre/<str:genre>', MovieGenre.as_view(), name='movie_genre'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('year/<str:year>', MovieYear.as_view(), name='movie_year'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    
]
