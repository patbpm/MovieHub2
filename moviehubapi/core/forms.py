from django import forms
from django.conf import settings
import requests

class SearchForm(forms.Form):
    word = forms.CharField(max_length=100)
    
    def search(self):
        KEY = settings.MOVIEDB_API_KEY
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://api.themoviedb.org/3/search/multi?api_key={key}&query={word_id}'
        url = endpoint.format(key=KEY, word_id=word)
        
        response = requests.get(url)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The TMDB API is not available at the moment. Please try again later.'
        return result