import json
import requests

'''
Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. 
The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. 
It will be a python dictionary with just one key, ‘Similar’.
'''
def get_movies_from_tastedive(query):
    baseurl = "https://tastedive.com/api/similar"
    diction = {}
    diction['q'] = query
    diction['type'] = 'movies'
    diction['limit'] = 5
    resp = requests.get(baseurl, params=diction)
    resp_d = json.loads(resp.text)

    return resp_d

'''
Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the 
list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
'''
def extract_movie_titles(d):
    return [lst["Name"] for lst in d["Similar"]["Results"]]

'''
Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, 
called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, 
extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
'''

def get_related_titles(lst):
    new_lst = []
    for i in range(len(lst)):
        d = get_movies_from_tastedive(lst[i])
        for c in d["Similar"]["Results"]:
            if c["Name"] not in new_lst and c["Name"] != lst[i]:
                new_lst.append(c["Name"])
    return new_lst

'''
Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. 
The function should return a dictionary with information about that movie.
Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. 
You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order 
to extract existing data from the cache.
'''

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    diction = {}
    diction["t"] = title
    diction["r"] = "json"
    resp = requests.get(baseurl, params=diction)
    #resp_d = json.loads(resp.text)

    return resp.json()


print(get_movie_data("Venom"))

'''
Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. 
It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary 
for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
'''

def get_movie_rating(d):
    try:
        for source in d['Ratings']:
            print(source["Value"])
            if source['Source']=='Rotten Tomatoes':
                print(source['Value'][:-1])
                return int(source['Value'][:-1])
    except:
        return 0
    else:
        return 0

'''
Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. 
Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie 
titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten 
Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
'''

def get_sorted_recommendations(lst):
    unsorted_list = get_related_titles(lst)
    sorted_list = sorted(unsorted_list, key=lambda x: (get_movie_rating(get_movie_data(x)), x), reverse=True)
    return sorted_list




