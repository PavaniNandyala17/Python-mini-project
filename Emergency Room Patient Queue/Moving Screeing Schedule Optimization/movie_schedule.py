def sort_key(movie): 
return (movie [2], - movie [3]) # Sort by end time, then by popularity(descending) 
def movie_screening_schedule(movies): 
movies.sort(key=sort_key) 
selected, end_time, popularity = [], 0, 0 
 for name, start, end, pop in movies: 
        if start >= end_time: 
            selected.append(name) 
   end_time, popularity = end, popularity + pop 
    return selected, popularity 
# Taking input dynamically 
num_movies = int (input ("Enter the number of movies: ")) 
movies = [] 
for _ in range(num_movies): 
    name = input ("Enter movie name: ") 
    start = int (input ("Enter start time: ")) 
    end = int (input ("Enter end time: ")) 
    popularity = int (input ("Enter popularity score: ")) 
    movies.append((name, start, end, popularity)) 
# Process the schedule 
selected_movies, total_popularity = movie_screening_schedule(movies) 
# Display results 
print ("Selected Movies:", selected_movies) 
print ("Total Popularity:", total_popularity) 
