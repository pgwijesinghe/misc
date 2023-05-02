import tkinter as tk
import imdb
import webbrowser
from tkinter import messagebox
import urllib.request

class MovieSearchGUI:
    def __init__(self):
        self.ia = imdb.IMDb()
        self.results = []

        # create the main window
        self.root = tk.Tk()
        self.root.title("Movie Search")

        # create the search frame
        self.search_frame = tk.Frame(self.root)
        self.search_label = tk.Label(self.search_frame, text="Search for a movie:")
        self.search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.year_entry = tk.Entry(self.search_frame, width=6)
        self.year_entry.pack(side=tk.LEFT, padx=10)
        self.year_label = tk.Label(self.search_frame, text="Year (optional):")
        self.year_label.pack(side=tk.LEFT)
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_movies)
        self.search_button.pack(side=tk.RIGHT)
        self.search_frame.pack(side=tk.TOP, fill=tk.X)

        # create the results frame
        self.results_frame = tk.Frame(self.root)
        self.results_label = tk.Label(self.results_frame, text="Results:")
        self.results_label.pack(side=tk.TOP)
        self.results_scrollbar = tk.Scrollbar(self.results_frame)
        self.results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_listbox = tk.Listbox(self.results_frame, yscrollcommand=self.results_scrollbar.set, width=50)
        self.results_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.results_listbox.bind('<<ListboxSelect>>', lambda event: self.display_movie_details())
        self.results_scrollbar.config(command=self.results_listbox.yview)
        self.results_frame.pack(side=tk.LEFT, fill=tk.Y)

        # create the details frame
        self.details_frame = tk.Frame(self.root)
        self.title_label = tk.Label(self.details_frame, font=("TkDefaultFont", 16))
        self.title_label.pack(side=tk.TOP, pady=10)
        self.details_label_frame = tk.Frame(self.details_frame)
        self.details_label_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.rating_label = tk.Label(self.details_label_frame)
        self.rating_label.pack(side=tk.TOP)
        self.votes_label = tk.Label(self.details_label_frame)
        self.votes_label.pack(side=tk.TOP)
        self.directors_label = tk.Label(self.details_label_frame)
        self.directors_label.pack(side=tk.TOP)
        self.cast_label = tk.Label(self.details_label_frame, wraplength=400)
        self.cast_label.pack(side=tk.TOP, pady=10)
        self.summary_label = tk.Label(self.details_label_frame, wraplength=400)
        self.summary_label.pack(side=tk.TOP, pady=10)
        self.trailer_button = tk.Button(self.details_label_frame, text="Watch Trailer", command=self.watch_trailer)
        self.trailer_button.pack(side=tk.BOTTOM)
        self.details_frame.pack(side=tk.LEFT, fill=tk.Y)

    def search_movies(self):
        # clear the previous results
        self.results = []
        self.results_listbox.delete(0, tk.END)
        self.title_label.config(text="")
        self.rating_label.config(text="")
        self.votes_label.config(text="")
        self.directors_label.config(text="")
        self.cast_label.config(text="")
        self.summary_label.config(text="")

        # get the user's search query and optional year
        query = self.search_entry.get().strip()
        year = self.year_entry.get().strip()

        # search for movies
        if year:
            results = self.ia.search_movie(query, year=int(year))
        else:
            results = self.ia.search_movie(query)

        # display the first five results in the listbox
        for i in range(5):
            if i >= len(results):
                break
            movie = results[i]
            self.results.append(movie)
            self.results_listbox.insert(tk.END, movie.summary())

    def display_movie_details(self):
        # get the selected movie from the listbox
        selection = self.results_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        movie = self.results[index]

        # get the movie details
        self.ia.update(movie)
        title = movie['title']
        rating = movie.get('rating')
        votes = movie.get('votes')
        directors = ", ".join([d['name'] for d in movie.get('directors', [])])
        cast = ", ".join([c['name'] for c in movie.get('cast', [])])
        summary = movie.get('plot outline')

        # update the GUI with the movie details
        self.title_label.config(text=title)
        poster_url = movie.get('full-size cover url')
        if rating:
            self.rating_label.config(text="Rating: {:.1f}/10".format(rating))
        if votes:
            self.votes_label.config(text="Votes: {:,}".format(votes))
        if directors:
            self.directors_label.config(text="Directors: {}".format(directors))
        if cast:
            self.cast_label.config(text="Cast: {}".format(cast))
        if summary:
            self.summary_label.config(text="Summary: {}".format(summary))

    def watch_trailer(self):
        # open the movie trailer in the default web browser
        selection = self.results_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        movie = self.results[index]
        query = "{} {} trailer".format(movie['title'], movie['year'])
        url = "https://www.youtube.com/results?search_query={}".format(query)
        webbrowser.open_new(url)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = MovieSearchGUI()
    gui.run()

