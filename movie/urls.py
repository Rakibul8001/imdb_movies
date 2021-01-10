from django.urls import path
from .views import MovieList, MovieDetail,MovieCategory,MovieLanguage,MovieYear,MovieSearch

app_name = "movie"

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    # path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('year/<str:year>', MovieYear.as_view(), name='movie_year'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    
]
