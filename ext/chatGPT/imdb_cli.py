import imdb
import webbrowser
import sys

print("IMDB Movie Search\n")
# create an IMDb access object
ia = imdb.IMDb()

# get the movie title from the command line argument
if len(sys.argv) > 1:
    title = ' '.join(sys.argv[1:])
else:
    title = input("Enter the movie title: ")
print(f"You're searching for: {title}")
'''
# ask the user for the movie title and year (optional)
title = input("Enter the movie title: ")
year = input("Enter the year (optional): ")

# search for the movie
results = ia.search_movie(title)
if year:
    # filter the results by year (if provided)
    results = [r for r in results if str(r.get('year')) == year]
'''

results = ia.search_movie(title)

# list the first 5 search results
print("Search Results:")
for i, r in enumerate(results[:5]):
    print(f"{i+1}. {r.get('title')} ({r.get('year')})")

# prompt the user to select the correct movie
selection = input("Select the correct movie (1-5): ")
movie = results[int(selection)-1]

print(f"You selected: {movie}")

# get the movie's details
ia.update(movie)
rating = movie.get('rating')
votes = movie.get('votes')
try:
  directors = movie.get('directors')
except:
  directors = "No directors found!"
cast = movie.get('cast')[0:5:1]
summary = movie.get('plot outline')

# display the movie's details
print(f"Rating: {rating}/10 ({votes} votes)")
try:
    print("Directors:", ", ".join([d.get('name') for d in directors])) 
except:
   print("No data found for directors")
print("Cast:", ", ".join([c.get('name') for c in cast]))
print("\033[1;32mSummary:", summary)

# ask the user if they want to watch the trailer
watch_trailer = input("\033[1;37mDo you want to watch the trailer? (y/n): ")
if watch_trailer.lower() == 'y':
    # open the movie's trailer in the web browser
    query = f"{movie.get('title')} {movie.get('year')} trailer"
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)


