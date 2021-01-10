from .models import Movie

def slider_movies(request):
    movies = Movie.objects.all().order_by('-created')
    return {'slider_movies':movies}