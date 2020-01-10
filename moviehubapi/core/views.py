from django.shortcuts import render
from django.conf import settings
import requests
from .forms import SearchForm

# Create your views here.
def homepage(request):
    KEY = settings.MOVIEDB_API_KEY
    is_cached = ('trendings' in request.session)
    

    if not is_cached:
        TRENDING_PATTERN = 'https://api.themoviedb.org/3/trending/all/day?api_key={key}'
        r = requests.get(TRENDING_PATTERN.format(key=KEY))
        request.session['trendings'] = r.json()
    
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    MOVIE_GENRES = 'https://api.themoviedb.org/3/genre/movie/list?api_key={key}'
    DISCOVER_PATTERN = 'https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=en-US'
    POPULAR_MOVIES = 'https://api.themoviedb.org/3/movie/popular?api_key={key}'
    d = requests.get(DISCOVER_PATTERN.format(key=KEY))
    rated_movies= d.json()

    p = requests.get(POPULAR_MOVIES.format(key=KEY))
    popular_movies= p.json()

    
    trendings = request.session['trendings']
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    config = t.json()
    g = requests.get(MOVIE_GENRES.format(key=KEY))
    genre_movies = g.json()
    context = {
        'trendings': trendings['results'],
        'base_url': config['images']['base_url'],
        'backdrop_sizes' : config['images']['backdrop_sizes'][2],
        'genre_movies': genre_movies['genres'],
        'rated_movies': rated_movies['results'],
        'popular_movies': popular_movies['results'],
        'sizes' : config['images']['poster_sizes'][2],
        'is_cached': is_cached
    } 
    
    return render(request, 'core/templates/homepage.html', context)

def genderlist(request):
    
    KEY = settings.MOVIEDB_API_KEY
    POPULAR_MOVIES = 'https://api.themoviedb.org/3/movie/popular?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    r = requests.get(POPULAR_MOVIES.format(key=KEY))
    gender_datas = r.json()
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    config = t.json()
    
    context = {
        'gender': discover_datas['results'],
        'base_url': config['images']['base_url'],
        'sizes' : config['images']['poster_sizes'][2],
    }
    return render(request, 'core/templates/mostRatedMovies.html', context)

def mostrated(request):
    
    KEY = settings.MOVIEDB_API_KEY
    DISCOVER_PATTERN = 'https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=en-US'
    RATED_TV = 'https://api.themoviedb.org/3/tv/top_rated?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    r = requests.get(DISCOVER_PATTERN.format(key=KEY))
    tv = requests.get(RATED_TV.format(key=KEY))
    discover_datas = r.json()
    serie_datas = tv.json()
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    config = t.json()
    
    context = {
        'discover_datas': discover_datas['results'],
        'serie_datas': serie_datas['results'],
        'base_url': config['images']['base_url'],
        'sizes' : config['images']['poster_sizes'][2],
    }
    return render(request, 'core/templates/mostRatedMovies.html', context)

def mostpopular(request):
    
    KEY = settings.MOVIEDB_API_KEY
    POPULAR_MOVIES = 'https://api.themoviedb.org/3/movie/popular?api_key={key}'
    POPULAR_TV = 'https://api.themoviedb.org/3/tv/popular?api_key={key}'
    POPULAR_PERSON = 'https://api.themoviedb.org/3/person/popular?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    r = requests.get(POPULAR_MOVIES.format(key=KEY))
    s = requests.get(POPULAR_TV.format(key=KEY))
    p = requests.get(POPULAR_PERSON.format(key=KEY))
    popular_movies = r.json()
    popular_series = s.json()
    popular_persons = p.json()
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    config = t.json()
    
    context = {
        'popular_movies': popular_movies['results'],
        'popular_series': popular_series['results'],
        'popular_persons': popular_persons['results'],
        'base_url': config['images']['base_url'],
        'sizes' : config['images']['poster_sizes'][2],
    }
    return render(request, 'core/templates/mostpopularMovies.html', context)



def movie_detail(request, pk):
    
    KEY = settings.MOVIEDB_API_KEY
    DETAILS_PATTERN = 'https://api.themoviedb.org/3/movie/{pk}?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    MOVIE_CREDIT = 'https://api.themoviedb.org/3/movie/{pk}/credits?api_key={key}'
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    r = requests.get(DETAILS_PATTERN.format(key=KEY, pk=pk))
    m = requests.get(MOVIE_CREDIT.format(key=KEY, pk=pk))

    movie = r.json()
    config = t.json()
    credits = m.json()

    
    #movie_img_url = "{0}{1}{2}".format(base_url, sizes[2], rel_path)
    
    context = {
        'title': movie['title'],
        'overview': movie['overview'],
        'homepage': movie['homepage'],
        'base_url': config['images']['base_url'],
        'sizes' : config['images']['poster_sizes'][2],
        'profile_sizes' : config['images']['profile_sizes'][1],
        'backdrop_sizes' : config['images']['backdrop_sizes'][2],
        'rel_path' : movie['poster_path'],
        'genres': movie['genres'],
        'production_companies': movie['production_companies'],
        'movie': movie,
        'credits': credits['cast']
    }
    return render(request, 'core/templates/movie_detail.html', context)

def tvserie_detail(request, pk):
    
    KEY = settings.MOVIEDB_API_KEY
    TVSERIES_PATTERN = 'https://api.themoviedb.org/3/tv/{pk}?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    TVSERIE_CREDIT = 'https://api.themoviedb.org/3/tv/{pk}/credits?api_key={key}'
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    r = requests.get(TVSERIES_PATTERN.format(key=KEY, pk=pk))
    m = requests.get(TVSERIE_CREDIT.format(key=KEY, pk=pk))

    tvserie = r.json()
    config = t.json()
    tvseries_credits = m.json()

    
    #movie_img_url = "{0}{1}{2}".format(base_url, sizes[2], rel_path)
    
    context = {
        'name': tvserie['name'],
        'overview': tvserie['overview'],
        'homepage': tvserie['homepage'],
        'base_url': config['images']['base_url'],
        'sizes' : config['images']['poster_sizes'][2],
        'profile_sizes' : config['images']['profile_sizes'][1],
        'backdrop_sizes' : config['images']['backdrop_sizes'][2],
        'rel_path' : tvserie['poster_path'],
        'genres': tvserie['genres'],
        'production_companies': tvserie['production_companies'],
        'tvserie': tvserie,
        'tvseries_credits': tvseries_credits['cast']
    }
    return render(request, 'core/templates/tvserie_detail.html', context)

def person_detail(request, pk):
    
    KEY = settings.MOVIEDB_API_KEY
    PERSON_DETAILS = 'https://api.themoviedb.org/3/person/{pk}?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    PERSON_MOVIE_CREDITS = ' https://api.themoviedb.org/3/person/{pk}/movie_credits?api_key={key}'
    
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    r = requests.get(PERSON_DETAILS.format(key=KEY, pk=pk))
    m = requests.get(PERSON_MOVIE_CREDITS.format(key=KEY, pk=pk))
    

    person = r.json()
    config = t.json()
    movie_credits = m.json()
    

    
    #movie_img_url = "{0}{1}{2}".format(base_url, sizes[2], rel_path)
    
    context = {
        'person': person,
        'base_url': config['images']['base_url'],
        'profile_sizes' : config['images']['profile_sizes'][1],
        'movie_credits' : movie_credits['cast'],

    }
    return render(request, 'core/templates/person_detail.html', context)

def searchmovie(request):
    KEY = settings.MOVIEDB_API_KEY
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    config = t.json()
    search_result = {}
    if 'word' in request.GET:
        word = request.GET['word']
        endpoint = 'https://api.themoviedb.org/3/search/multi?api_key={key}&query={word_id}'
        url = endpoint.format(key=KEY, word_id=word)
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)
        search_result = response.json()
        search_result['success'] = search_was_successful

    context = {
    
        'search_result': search_result['results'],
        'base_url': config['images']['base_url'],
        'sizes' : config['images']['poster_sizes'][2],
        'profile_sizes' : config['images']['profile_sizes'][1],
        
    }
    return render(request, 'core/templates/search.html', context)

def season_detail(request, pk, season_number):
    
    KEY = settings.MOVIEDB_API_KEY
    
    SEASON_DETAILS = 'https://api.themoviedb.org/3/tv/{pk}/season/{season_number}?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    PERSON_SEASON_CREDITS = ' https://api.themoviedb.org/3/tv/{pk}/season/{season_number}/credits?api_key={key}'
    
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    r = requests.get(SEASON_DETAILS.format(key=KEY, pk=pk, season_number=season_number))
    m = requests.get(PERSON_SEASON_CREDITS.format(key=KEY, pk=pk, season_number=season_number))
    

    
    season = r.json()
    config = t.json()
    season_credits = m.json()
    

    
    #movie_img_url = "{0}{1}{2}".format(base_url, sizes[2], rel_path)
    
    context = {
        
        'season': season,
        'base_url': config['images']['base_url'],
        'profile_sizes' : config['images']['profile_sizes'][1],
        'still_sizes' : config['images']['still_sizes'][1],
        'sizes' : config['images']['poster_sizes'][2],
        'season_credits' : season_credits['cast'],

    }
    return render(request, 'core/templates/season_detail.html', context)

def episode_detail(request, pk, season_number, episode_number):
    
    KEY = settings.MOVIEDB_API_KEY
    
    EPISODE_DETAILS = 'https://api.themoviedb.org/3/tv/{pk}/season/{season_number}/episode/{episode_number}?api_key={key}'
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    PERSON_EPISODE_CREDITS = ' https://api.themoviedb.org/3/tv/{pk}/season/{season_number}/episode/{episode_number}/credits?api_key={key}'
    IMAGE_EPISODE = 'https://api.themoviedb.org/3/tv/{pk}/season/{season_number}/episode/{episode_number}/images?api_key={key}'
    
    
    t = requests.get(CONFIG_PATTERN.format(key=KEY))
    r = requests.get(EPISODE_DETAILS.format(key=KEY, pk=pk, season_number=season_number, episode_number=episode_number))
    m = requests.get(PERSON_EPISODE_CREDITS.format(key=KEY, pk=pk, season_number=season_number, episode_number=episode_number))
    n = requests.get(IMAGE_EPISODE.format(key=KEY, pk=pk, season_number=season_number, episode_number=episode_number))
    
    episode = r.json()
    config = t.json()
    episode_credits = m.json()
    episode_image = n.json()
    

    
    #movie_img_url = "{0}{1}{2}".format(base_url, sizes[2], rel_path)
    
    context = {
        'episode_image': episode_image['stills'],
        'episode': episode,
        'base_url': config['images']['base_url'],
        'profile_sizes' : config['images']['profile_sizes'][1],
        'still_sizes' : config['images']['still_sizes'][1],
        'sizes' : config['images']['poster_sizes'][2],
        'episode_credits' : episode_credits['cast'],

    }
    return render(request, 'core/templates/episode_detail.html', context)