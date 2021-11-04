#!/usr/bin/env python
# coding: utf-8

# <img src="netflix_icon.png" style="width: 600px;" />
# <br>
# 
# # Netflix Movies and TV Shows
# 
# **About this Dataset:** [Netflix](https://en.wikipedia.org/wiki/Netflix) is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, as of mid-2021, they have over 200M Subscribers globally. This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc [<sup id="fn1-back">1</sup>](#fn1).
# 
# Other than the dataset and description (above) given, the tasks, descriptions under the tasks, and summaries are all written and created by me.

# <hr>
# 
# ### Tasks:
# 
# 1. Give an updated list removing all the blank spaces in the cast and director(s) column.
# 2. How many movies came out in 2021 vs. 2020, and vs. 2019?
# 3. How many TV shows between those same years?
# 4. How has Netflix been impacted by COVID-19?
# 5. What is the rating distribution like?
# 6. What month is the most movies and TV shows released in 2017, 2019, and 2021?
# 7. What TV shows on Netflix only lasted one season?
# 8. What type of genre is the most popular in both movies and TV shows?
# 9. How many TV shows were created outside the United States, and what countries are they?
# 
# <hr>

# The `netflix_titles.csv` contains the following headers:
# 
# <table>
#     <tr>
#         <th>show_id</th>
#         <th>type</th>
#         <th>title</th>
#         <th>director</th>
#         <th>cast</th>
#         <th>country</th>
#         <th>date_added</th>
#         <th>release_year</th>
#         <th>rating</th>
#         <th>duration</th>
#         <th>listed_in</th>
#         <th>description</th>
#     </tr>
# </table>

# In[1]:


import csv

netflix_type = []
netflix_title = []
netflix_director = []
netflix_cast = []
netflix_country = []
netflix_date_added = []
netflix_release_year = []
netflix_rating = []
netflix_duration = []
netflix_listed_in = []
netflix_description = []

with open('netflix_titles.csv', encoding="utf8") as netflix_titles:
    netflix_reader = csv.DictReader(netflix_titles)
    for row in netflix_reader:
        #print(row['title'])
        netflix_type.append(row['type'])
        netflix_title.append(row['title'])
        netflix_director.append(row['director'])
        netflix_cast.append(row['cast'])
        netflix_country.append(row['country'])
        netflix_date_added.append(row['date_added'])
        netflix_release_year.append(row['release_year'])
        netflix_rating.append(row['rating'])
        netflix_duration.append(row['duration'])
        netflix_listed_in.append(row['listed_in'])
        netflix_description.append(row['description'])

        
netflix_show_id = []
for number in range(0, len(netflix_title)):
    #print(number)
    netflix_show_id.append(number)

#print(netflix_director)   


#The 'netflix_titles.csv' is now imported into the notebook as 'netflix_reader' with UTF-8 encoded.        


# Here we are printing out all the movie titles from the `netflix_titles.csv` document as an example to ensure each column was added into a list (type, title, director, cast, country, etc.).
# 
# Now the movie titles are in the `netflix_title` list.

# In[4]:


#This is to check to make sure it's printing out correctly.
for title in netflix_title:
    print(title)


# <br>

# ## 1. Updated List of Movies and TV Shows
# 
# We want an updated list removes all the blank spaces in the **director** and **cast** lists from the `netflix_titles.csv`. After getting rid of the empty spaces in the lists: `netflix_director` and `netflix_cast`; we will create a dictionary that contains the `netflix_show_id`, `netflix_title`, `updated_netflix_director`, `updated_netflix_cast`, and `netflix_release_year`.

# In[117]:


def update_movie_list():
    
    
    updated_netflix_director = []
    updated_netflix_cast = []
    netflix_dictionary = {}
    updated_movie_list = []
   

    for index in range(0, len(netflix_show_id)): 
        #print(index)
        netflix_dictionary.update({
            "ID": netflix_show_id[index],
            "Type" : netflix_type[index],
            "Title": netflix_title[index],
            "Director(s)": netflix_director[index],
            "Cast": netflix_cast[index],
            "Year Released": netflix_release_year[index]
        })
        #print(movie_dictionary)
        #print("")
    
        updated_movie_list.append(netflix_dictionary.copy())
    #print(movie_list)
    
    #This removes the dictionary if it doesn't contain a director or directors.
    updated_movie_list = [director for director in updated_movie_list if director['Director(s)'] != '']
    #This removes the dictionary if it doesn't contain any cast members.
    updated_movie_list = [cast for cast in updated_movie_list if cast['Cast'] != '']
    
    #print(movie_list)
    for dictionary in updated_movie_list:
        print(dictionary)
        print("")
         
    
update_movie_list()


# The data above now shows the updated list of movies and TV shows that only contain cast members, and a director(s); meaning there won't be any blank slots in the cast members or directors column.

# <br>
# <hr>

# ## 2. Number of Movies That Came Out in 2021, 2020, and 2019
# 
# We want to know how many total movies were released* in those three years, and which year had the most movies added to Netflix. For this question, the `updated_movie_list` will not be used as we want to know **all** the movies that came out during those 3 years, regardless of if there's any cast members or director(s) or not.
# 
# *This does not mean the movie was produced and released that year, but just released on Netflix.

# In[6]:


count_of_movies = []

def movies_that_came_out():
    
    all_movies = []
    movies_2021 = []
    movies_2020 = []
    movies_2019 = []
    movie_dictionary = {}
    
    
    for index in range(0, len(netflix_show_id)):
        movie_dictionary.update({
            "ID" : netflix_show_id[index],
            "Year Released" : netflix_release_year[index],
            "Type" : netflix_type[index],
            "Movie" : netflix_title[index]
        })
        #print(movie_dictionary)
    
        all_movies.append(movie_dictionary.copy())
    #Takes out all the Types that are TV Show
    all_movies = [movie for movie in all_movies if movie["Type"] != "TV Show"]
    #print(all_movies)
    #for movie in all_movies:
        #print(movie)
    
    movies_2021 = all_movies.copy()
    #Takes out all the movies that weren't released in 2021
    movies_2021 = [movie for movie in movies_2021 if movie["Year Released"] == "2021"]
    #print(movies_2021)
    num_movies_2021 = len([movie for movie in movies_2021 if isinstance(movie, dict)])
    #print(num_movies_2021)
    
    movies_2020 = all_movies.copy()
    #Removes all the movies that weren't released in 2020
    movies_2020 = [movie for movie in movies_2020 if movie["Year Released"] == "2020"]
    #print(movies_2020)
    num_movies_2020 = len([movie for movie in movies_2020 if isinstance(movie, dict)])
    #print(num_movies_2020)
    
    movies_2019 = all_movies.copy()
    movies_2019 = [movie for movie in movies_2019 if movie["Year Released"] == "2019"]
    #print(movies_2019)
    num_movies_2019 = len([movie for movie in movies_2019 if isinstance(movie, dict)])
    #print(num_movies_2019)
    
    
    movies_2021_dict = {}
    movies_2021_dict[2021] = num_movies_2021
    #print(movies_2021_dict)
    
    movies_2020_dict = {}
    movies_2020_dict[2020] = num_movies_2020
    #print(movies_2020_dict)
    
    movies_2019_dict = {}
    movies_2019_dict[2019] = num_movies_2019
    #print(movies_2019_dict)
    
    count_of_movies.append(movies_2021_dict)
    count_of_movies.append(movies_2020_dict)
    count_of_movies.append(movies_2019_dict)
    #print(count_of_movies)
    for movies in count_of_movies:
        #print(movies)
        for year, m in movies.items():
            print("In " + str(year) + ", " + str(m) + " movies came out.")
        
movies_that_came_out()    


# <br>
# <hr>

# ## 3. Number of TV Shows That Came Out in 2021, 2020, and 2019
# 
# Just as the previous question above, now we want to know the TV shows that were released* during those 3 years. We will continue to use the `netflix_title` list, as we want the most accurate number.
# 
# *Due to how Netflix releases TV shows, each new season will also be considered as "newly released". So this data is based more on when the most recent season was released, not necessarily the entire TV show itself.

# In[7]:


count_of_tv = []

def tv_that_came_out():
   
    all_tv_shows = []
    tv_2021 = []
    tv_2020 = []
    tv_2019 = []
    tv_dictionary = {}
    
    
    for index in range(0, len(netflix_show_id)):
        tv_dictionary.update({
            "ID": netflix_show_id[index],
            "Year Released" : netflix_release_year[index],
            "Type" : netflix_type[index],
            "TV Show" : netflix_title[index]
        })
        #print(tv_dictionary)
        all_tv_shows.append(tv_dictionary.copy())
    #print(all_tv_shows)
    
    #Removes all the types that are Movie.
    all_tv_shows = [tv for tv in all_tv_shows if tv["Type"] != "Movie"]
    #for tv in all_tv_shows:
        #print(tv)

    tv_2021 = all_tv_shows.copy()
    #Removes all the tv shows that weren't released in 2021
    tv_2021 = [tv for tv in tv_2021 if tv["Year Released"] == "2021"]
    num_tv_2021 = len([tv for tv in tv_2021 if isinstance(tv, dict)])
    #print(num_tv_2021)
    
    tv_2020 = all_tv_shows.copy()
    #Removes all the tv shows that weren't released in 2020
    tv_2020 = [tv for tv in tv_2020 if tv["Year Released"] == "2020"]
    num_tv_2020 = len([tv for tv in tv_2020 if isinstance(tv, dict)])
    #print(num_tv_2020)
    
    tv_2019 = all_tv_shows.copy()
    tv_2019 = [tv for tv in tv_2019 if tv["Year Released"] == "2019"]
    num_tv_2019 = len([tv for tv in tv_2019 if isinstance(tv, dict)])
    #print(num_tv_2019)
    
    
    tv_2021_dict = {}
    tv_2021_dict[2021] = num_tv_2021
    #print(tv_2021_dict)
    
    tv_2020_dict = {}
    tv_2020_dict[2020] = num_tv_2020
    #print(tv_2020_dict)
    
    tv_2019_dict = {}
    tv_2019_dict[2019] = num_tv_2019
    #print(tv_2019_dict)
    
    count_of_tv.append(tv_2021_dict)
    count_of_tv.append(tv_2020_dict)
    count_of_tv.append(tv_2019_dict)
    #print(count_of_tv)
    for tv in count_of_tv:
        #print(tv)
        for year, shows in tv.items():
            print("In " + str(year) + ", " + str(shows) + " TV shows came out.")
    
        
tv_that_came_out()


# <br>
# <hr>

# ## 4. How Has Netflix Been Impacted By COVID-19?
# 
# We will be using the results from questions two and three to answer this question.

# In[22]:


from matplotlib import pyplot as plt
import numpy as np 

#print(count_of_tv)
#print(count_of_movies)
updated_tv_value = []
updated_tv_key = []

updated_movie_value = []
updated_movie_key = []

for tv in count_of_tv:
    #print(tv)
    tv_value = tv.values()
    new_tv_value = list(tv_value)
    #print(new_tv_value)
    updated_tv_value.append(new_tv_value[0])
    
    tv_key = tv.keys()
    new_tv_key = list(tv_key)
    #print(new_tv_key)
    updated_tv_key.append(new_tv_key[0])
updated_tv_value.reverse()
updated_tv_key.reverse()
#print(updated_tv_value)
#print(updated_tv_key)

for movie in count_of_movies:
    movie_value = movie.values()
    new_movie_value = list(movie_value)
    #print(new_movie_value)
    updated_movie_value.append(new_movie_value[0])
    
    movie_key = movie.keys()
    new_movie_key = list(movie_key)
    #print(new_movie_key)
    updated_movie_key.append(new_movie_key[0])
updated_movie_value.reverse()    
#print(updated_movie_value)
#print(updated_movie_key)


#----------------------------------------------------------------------------------------------#
#GRAPH

#x-axis
x = updated_tv_key #updated_movie_key is identical, so no need to use both

#y-axis
y = updated_tv_value
y_2 = updated_movie_value

x_axis = np.arange(len(x))

bar1 = plt.bar(x_axis - 0.2 ,y, 0.4, color='#eca1a6', edgecolor="gray") #Can use HTML HEX colors
bar2 = plt.bar(x_axis + 0.2, y_2, 0.4, color=(0.2, 0.4, 0.6, 0.6), edgecolor="gray")

plt.rcParams["figure.figsize"]=(10, 9)
plt.rcParams["font.size"]= 12.0

#This will give you the x-axis labels as 2019, 2020, 2021
plt.xticks(x_axis, x)
plt.legend((bar1, bar2), ('TV Shows', 'Movies'))

plt.title("Number of TV Shows Released vs. Number of Movies Released")
plt.xlabel("Year Released")
plt.ylabel("Number of Netflix Titles Released")

#This shows the value on top of the bars
for index, value in enumerate(y):
    plt.text(x_axis[index] - 0.25, value + 5.0, str(value))

for index, value in enumerate(y_2):
    plt.text(x_axis[index] + 0.13, value + 5.0, str(value))
    
plt.show()


# ### Summary
# 
# Based on the data from the two questions above (from both movies and TV shows), Netflix had released many movies and TV shows because of the lockdown; making it very easy for people to access their content.
# 
# In **2019**, it's suggested that because of the lockdown, it was very difficult to continue filming TV shows, therefore, there wasn't a lot of TV shows that were released during 2019; but many movies (not necessarily released that specific year), both old and new, were able to be released.
# 
# In **2020**, after the lockdown had been lifted; filming for TV shows and movies were able to resume, allowing for Netflix to go ahead and release more TV shows that were originally on hold. Since there were more TV shows released, it seems like Netflix didn't need to worry about releasing as many movies as the previous year.
# 
# In **2021**, it has simply been the same as the year 2020. There has been more TV shows than movies that have been released, however, there has been a lower count of both TV shows and movies during this year, which may be due to other streaming services pushing out more content.
#     
# We could assume that 2019 was the best year to release content for both movies and TV shows, however, movies would do a lot better than the TV shows.

# <br>
# <hr>

# ## 5. Rating Distribution in Movies and TV
# 
# We want to know how the ratings: TV-MA, TV-14, TV-PG, TV-G, TV-Y7, TV-Y are distributed in TV shows; and the ratings: R, PG-13, PG, G, NR, UR for movies*. 
# <table>
#     <tr>
#         <th></th>
#         <th>TV Show Rating</th>
#         <th>Movie Rating</th>
#         <th></th>
#     </tr>
#     <tr>
#         <td>For Mature Audiences</td>
#         <td>TV-MA</td>
#         <td>R</td>
#         <td></td>
#     </tr>
#     <tr>
#         <td>For 14+</td>
#         <td>TV-14</td>
#         <td>PG-13</td>
#         <td></td>
#     </tr>
#     <tr>
#         <td>Parental Guidance Suggested</td>
#         <td>TV-PG</td>
#         <td>PG</td>
#         <td></td>
#     </tr>
#     <tr>
#         <td>For All Ages</td>
#         <td>TV-G</td>
#         <td>G</td>
#         <td></td>
#     </tr>
#     <tr>
#         <td>For Children 7+</td>
#         <td>TV-Y7</td>
#         <td></td>
#         <td></td>
#     </tr>
#     <tr>
#         <td>For Young Children</td>
#         <td>TV-Y</td>
#         <td></td>
#         <td></td>
#     </tr>
#     <tr>
#         <td></td>
#         <td></td>
#         <td>NR</td>
#         <td>Not Rated**</td>
#     </tr>
#     <tr>
#         <td></td>
#         <td></td>
#         <td>UR</td>
#         <td>Unrated***</td>
#     </tr>
# </table>
# 
# <br>
# 
# We will be using `netflix_type` and `netflix_rating` to determine how many movies and shows in the industry have been marketed to difference age groups.
# 
# <br>
# <br>
# 
# <div>*TV ratings are assigned by the <i>TV Parental Guidelines</i>, while movie ratings are done by the <i>Motion Picture Association of America (MPAA)</i> in the United States. Different countries will have their own rating system, but due to the data, we will be using the American standard.</div>
# <div>**<b>Not Rated</b> means that it has not yet been rated by the <i>MPAA</i>. This does not mean it is necessarily worse than an 'R' rating; many International Films tend to have a 'NR' rating.</div>
# <div>***<b>Unrated</b> means it contains scenes that were cut from the movie that might have earned a stricter rating by <i>MPAA</i>.</div>

# In[15]:


#This function is for TV rating ONLY

Count_All_TV_Ratings = []

def tv_rating_distribution():
    
    tv_shows = []
    tv_shows_dict = {}
    
    TV_MA = []
    TV_14 = []
    TV_PG = []
    TV_G = []
    TV_Y7 = []
    TV_Y = []
    
    Count_TV_MA = []
    Count_TV_14 = []
    Count_TV_PG = []
    Count_TV_G = []
    Count_TV_Y7 = []
    Count_TV_Y = []
    
    
    for index in range(0, len(netflix_show_id)):
        tv_shows_dict.update({
            "Title" : netflix_title[index],
            "Type" : netflix_type[index],
            "Rating" : netflix_rating[index]
        })
        #print(tv_shows_dict)
        tv_shows.append(tv_shows_dict.copy()) 
    #print(tv_shows)
    
    tv_shows = [tv for tv in tv_shows if tv["Type"] == "TV Show"]
    #print(tv_shows)
    
    
    TV_MA = tv_shows.copy()
    TV_MA = [tv for tv in TV_MA if tv["Rating"] == "TV-MA"]
    #print(TV_MA)
    num_TV_MA = len([tv for tv in TV_MA if isinstance(tv, dict)])
    #print(num_TV_MA)
    
    TV_14 = tv_shows.copy()
    TV_14 = [tv for tv in TV_14 if tv["Rating"] == "TV-14"]
    #print(TV_14)
    num_TV_14 = len([tv for tv in TV_14 if isinstance(tv, dict)])
    #print(num_TV_14)
    
    TV_PG = tv_shows.copy()
    TV_PG = [tv for tv in TV_PG if tv["Rating"] == "TV-PG"]
    #print(TV_PG)
    num_TV_PG = len([tv for tv in TV_PG if isinstance(tv, dict)])
    
    TV_G = tv_shows.copy()
    TV_G = [tv for tv in TV_G if tv["Rating"] == "TV-G"]
    #print(TV_G)
    num_TV_G = len([tv for tv in TV_G if isinstance(tv, dict)])
    
    TV_Y7 = tv_shows.copy()
    TV_Y7 = [tv for tv in TV_Y7 if tv["Rating"] == "TV-Y7"]
    #print(TV_Y7)
    num_TV_Y7 = len([tv for tv in TV_Y7 if isinstance(tv, dict)])
    
    TV_Y = tv_shows.copy()
    TV_Y = [tv for tv in TV_Y if tv["Rating"] == "TV-Y"]
    #print(TV_Y)
    num_TV_Y = len([tv for tv in TV_Y if isinstance(tv, dict)])
    
    
    TV_MA_dict = {}
    TV_MA_dict["TV-MA"] = num_TV_MA
    #print(TV_MA_dict)
    Count_TV_MA.append(TV_MA_dict)
    #print(Count_TV_MA)
    
    TV_14_dict = {}
    TV_14_dict["TV-14"] = num_TV_14
    #print(TV_14_dict)
    Count_TV_14.append(TV_14_dict)
    #print(Count_TV_14)
    
    TV_PG_dict = {}
    TV_PG_dict["TV-PG"] = num_TV_PG
    #print(TV_PG_dict)
    Count_TV_PG.append(TV_PG_dict)
    #print(Count_TV_PG)
    
    TV_G_dict = {}
    TV_G_dict["TV-G"] = num_TV_G
    #print(TV_G_dict)
    Count_TV_G.append(TV_G_dict)
    #print(Count_TV_G)
    
    TV_Y7_dict = {}
    TV_Y7_dict["TV-Y7"] = num_TV_Y7
    #print(TV_Y7_dict)
    Count_TV_Y7.append(TV_Y7_dict)
    #print(Count_TV_Y7)
    
    TV_Y_dict = {}
    TV_Y_dict["TV-Y"] = num_TV_Y
    #print(TV_Y_dict)
    Count_TV_Y.append(TV_Y_dict)
    #print(Count_TV_Y)
    
    
    Count_All_TV_Ratings.append(TV_MA_dict)
    Count_All_TV_Ratings.append(TV_14_dict)
    Count_All_TV_Ratings.append(TV_PG_dict)
    Count_All_TV_Ratings.append(TV_G_dict)
    Count_All_TV_Ratings.append(TV_Y7_dict)
    Count_All_TV_Ratings.append(TV_Y_dict)
    
    for tv_rating in Count_All_TV_Ratings:
        #print(tv_rating)
        for key, value in tv_rating.items():
            print("There are " + str(value) + " TV shows rated " + key + ".")
            
tv_rating_distribution()    


# <br>

# In[87]:


Count_All_Movie_Ratings = []

def movie_rating_distribution():
    
    movies = []
    movies_dict = {}
    
    R = []
    PG_13 = []
    PG = []
    G = []
    NR = []
    UR = []
    
    for index in range(0, len(netflix_show_id)):
        movies_dict.update({
            "Title" : netflix_title[index],
            "Type" : netflix_type[index],
            "Rating" : netflix_rating[index]
        })
        movies.append(movies_dict.copy())
    #print(movies) 
    
    movies = [m for m in movies if m["Type"] == "Movie"]
    #print(movies)
    
    R = movies.copy()
    R = [m for m in movies if m["Rating"] == "R"]
    #print(R)
    num_R = len([m for m in R if isinstance(m, dict)])
    #print(num_R)
    
    PG_13 = movies.copy()
    PG_13 = [m for m in movies if m["Rating"] == "PG-13"]
    #print(PG_13)
    num_PG_13 = len([m for m in PG_13 if isinstance(m, dict)])
    #print(num_PG_13)
    
    PG = movies.copy()
    PG = [m for m in movies if m["Rating"] == "PG"]
    #print(PG)
    num_PG = len([m for m in PG if isinstance(m, dict)])
    #print(num_PG)
    
    G = movies.copy()
    G = [m for m in movies if m["Rating"] == "G"]
    #print(G)
    num_G = len([m for m in G if isinstance(m, dict)])
    #print(num_G)
    
    NR = movies.copy()
    NR = [m for m in movies if m["Rating"] == "NR"]
    #print(NR)
    num_NR = len([m for m in NR if isinstance(m, dict)])
    #print(num_NR)
    
    UR = movies.copy()
    UR = [m for m in movies if m["Rating"] == "UR"]
    #print(UR)
    num_UR = len([m for m in UR if isinstance(m, dict)])
    #print(num_UR)
    
    
    R_dict = {}
    R_dict["R"] = num_R
    Count_R.append(R_dict)
    #print(Count_R)
    
    PG_13_dict = {}
    PG_13_dict["PG-13"] = num_PG_13
    Count_PG_13.append(PG_13_dict)
    #print(Count_PG_13)
    
    PG_dict = {}
    PG_dict["PG"] = num_PG
    Count_PG.append(PG_dict)
    #print(Count_PG)
    
    G_dict = {}
    G_dict["G"] = num_G
    Count_G.append(G_dict)
    #print(Count_G)
    
    NR_dict = {}
    NR_dict["NR"] = num_NR
    Count_NR.append(NR_dict)
    #print(Count_NR)
    
    UR_dict = {}
    UR_dict["UR"] = num_UR
    Count_UR.append(UR_dict)
    #print(Count_UR)
    
    
    Count_All_Movie_Ratings.append(R_dict)
    Count_All_Movie_Ratings.append(PG_13_dict)
    Count_All_Movie_Ratings.append(PG_dict)
    Count_All_Movie_Ratings.append(G_dict)
    Count_All_Movie_Ratings.append(NR_dict)
    Count_All_Movie_Ratings.append(UR_dict)
    
    for movie in Count_All_Movie_Ratings:
        #print(movie)
        for key, value in movie.items():
            print("There are " + str(value) + " movies rated " + key + ".")
    
movie_rating_distribution()    


# <br>

# In[177]:


from matplotlib import pyplot as plt
import numpy as np 

tv_rating_key = []
tv_rating_value = []

movie_rating_key = []
movie_rating_value = []

for tv in Count_All_TV_Ratings:
    #print(tv)
    for key, value in tv.items():
        tv_rating_key.append(key)
        tv_rating_value.append(value)
        
#print(tv_rating_key)
#print(tv_rating_value)

for m in Count_All_Movie_Ratings:
    #print(m)
    for key, value in m.items():
        movie_rating_key.append(key)
        movie_rating_value.append(value)
        
#print(movie_rating_key)
#print(movie_rating_value)


#-------------------------------------------------------------------------#
#GRAPH

pie_one = np.array(tv_rating_value)
label_one = tv_rating_key

pie_two = np.array(movie_rating_value)
label_two = movie_rating_key

myexplode = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
colors = ['#b2b2b2', '#f4e1d2', '#f18973', '#bc5a45', '#92a8d1', '#667292']
    
                            #rows, columns
fig, (p1, p2) = plt.subplots(1, 2, figsize=(17, 17))

p1.pie(pie_one, labels = label_one, autopct = '%1.2f%%', startangle=50, explode=myexplode, colors=colors)
p2.pie(pie_two, labels = label_two, autopct = '%1.2f%%',startangle=50, explode=myexplode, colors=colors)
p1.set_title('TV Ratings', pad = 20)
p2.set_title('Movie Ratings', pad = 20)

plt.show()


# ### Summary
# 
# Now that we have the data and graph, we can see that almost half of the TV ratings are 'TV-MA', and more than half of the movie ratings are 'R'; which are meant for mature adults. Although there are some movies and shows for a younger age range, it is recommended for those who are younger than 13 should not use Netflix.
# 
# We could safely assume that Netflix is supposed to be a streaming service meant for those who are 17 and older, with some TV shows and movies meant for those 13 and older.

# <br>
# <hr>

# ## 6. Find the Most Popular Month for Released Movies in 2018
# 
# In order to find the most popular month, we will be using `netflix_date_added`; and since we are only finding the movies most popular release month, we will need to use `netflix_type` as well. All we want to see, is which month(s) in **2018** was the had the most movies released.

# In[30]:


from datetime import datetime
import dateutil.parser

year_2018_movie = []
count_all_movies_2018 = []

def popular_month_movie():
    
    movie_dict = {}
    movie_list = []
    
    updated_netflix_date_added = []
    netflix_month_added = []
    netflix_year_added = []
    
    jan_2018 = []
    feb_2018 = []
    mar_2018 = []
    apr_2018 = []
    may_2018 = []
    jun_2018 = []
    jul_2018 = []
    aug_2018 = []
    sep_2018 = []
    oct_2018 = []
    nov_2018 = []
    dec_2018 = []
    
    for date in netflix_date_added:
        if date != '' and date != "TV-PG": #for some reason it's bugging out with 'TV-PG' appearing as a date
            new_date_format = dateutil.parser.parse(date).strftime("%B %Y")
            month_format = dateutil.parser.parse(date).strftime("%b")
            year_format = dateutil.parser.parse(date).strftime("%Y")
        #print(new_date_format)
        updated_netflix_date_added.append(new_date_format)
        netflix_month_added.append(month_format)
        netflix_year_added.append(year_format)
    #print(updated_netflix_date_added)
            
    
    for index in range(0, len(netflix_show_id)):
        movie_dict.update({
            "Title": netflix_title[index],
            "Type": netflix_type[index],
            "Date Added": updated_netflix_date_added[index],
            "Month": netflix_month_added[index],
            "Year" : netflix_year_added[index]
        })
        #print(movie_dict)
        movie_list.append(movie_dict.copy())
    #print(movie_list)
    
    movie_list = [m for m in movie_list if m["Type"] == "Movie"]
    #print(movie_list)
    updated_movie_list = [m for m in movie_list if m["Date Added"]]
    #print(updated_movie_list)
    
    year_2018_movie = [m for m in updated_movie_list if m["Year"] == '2018']
    #print(year_2018_movie)
    
    jan_2018 = [m for m in year_2018_movie if m["Month"] == "Jan"]
    num_jan = len([m for m in jan_2018 if isinstance(m, dict)])
    #print(num_jan)
    jan_dict = {}
    jan_dict["Jan"] = num_jan
    
    feb_2018 = [m for m in year_2018_movie if m["Month"] == "Feb"]
    num_feb = len([m for m in feb_2018 if isinstance(m, dict)])
    #print(num_feb)
    feb_dict = {}
    feb_dict["Feb"] = num_feb
    
    mar_2018 = [m for m in year_2018_movie if m["Month"] == "Mar"]
    num_mar = len([m for m in mar_2018 if isinstance(m, dict)])
    #print(num_mar)
    mar_dict = {}
    mar_dict["Mar"] = num_mar
    
    apr_2018 = [m for m in year_2018_movie if m["Month"] == "Apr"]
    num_apr = len([m for m in apr_2018 if isinstance(m, dict)])
    apr_dict = {}
    apr_dict["Apr"] = num_apr
    
    may_2018 = [m for m in year_2018_movie if m["Month"] == "May"]
    num_may = len([m for m in may_2018 if isinstance(m, dict)])
    may_dict = {}
    may_dict["May"] = num_may
    
    jun_2018 = [m for m in year_2018_movie if m["Month"] == "Jun"]
    num_jun = len([m for m in jun_2018 if isinstance(m, dict)])
    jun_dict = {}
    jun_dict["Jun"] = num_jun
    
    jul_2018 = [m for m in year_2018_movie if m["Month"] == "Jul"]
    num_jul = len([m for m in jul_2018 if isinstance(m, dict)])
    jul_dict = {}
    jul_dict["Jul"] = num_jul
    
    aug_2018 = [m for m in year_2018_movie if m["Month"] == "Aug"]
    num_aug = len([m for m in aug_2018 if isinstance(m, dict)])
    aug_dict = {}
    aug_dict["Aug"] = num_aug
    
    sep_2018 = [m for m in year_2018_movie if m["Month"] == "Sep"]
    num_sep = len([m for m in sep_2018 if isinstance(m, dict)])
    sep_dict = {}
    sep_dict["Sep"] = num_sep
    
    oct_2018 = [m for m in year_2018_movie if m["Month"] == "Oct"]
    num_oct = len([m for m in oct_2018 if isinstance(m, dict)])
    oct_dict = {}
    oct_dict["Oct"] = num_oct
    
    nov_2018 = [m for m in year_2018_movie if m["Month"] == "Nov"]
    num_nov = len([m for m in nov_2018 if isinstance(m, dict)])
    nov_dict = {}
    nov_dict["Nov"] = num_nov
    
    dec_2018 = [m for m in year_2018_movie if m["Month"] == "Dec"]
    num_dec = len([m for m in dec_2018 if isinstance(m, dict)])
    dec_dict = {}
    dec_dict["Dec"] = num_dec
    
    
    count_all_movies_2018.append(jan_dict)
    count_all_movies_2018.append(feb_dict)
    count_all_movies_2018.append(mar_dict)
    count_all_movies_2018.append(apr_dict)
    count_all_movies_2018.append(may_dict)
    count_all_movies_2018.append(jun_dict)
    count_all_movies_2018.append(jul_dict)
    count_all_movies_2018.append(aug_dict)
    count_all_movies_2018.append(sep_dict)
    count_all_movies_2018.append(oct_dict)
    count_all_movies_2018.append(nov_dict)
    count_all_movies_2018.append(dec_dict)
    
    for movies in count_all_movies_2018:
        #print(movies)
        for key, value in movies.items():
            print("There are " + str(value) + " movies in " + key + " 2018.")
        
    
popular_month_movie()    


# <br>

# In[79]:


from matplotlib import pyplot as plt
import numpy as np 

#x-axis
key_movie_2018 = []

#y-axis
value_movie_2018 = []

for movie in count_all_movies_2018:
    #print(movie)
    for key, value in movie.items():
        key_movie_2018.append(key)
        value_movie_2018.append(value)
        
#print(key_movie_2018)
#print(value_movie_2018)



#-------------------------------------------------------------------------#
#GRAPH
x_axis = np.arange(len(key_movie_2018))
color = ['#ECDB54', '#E94B3C', '#6F9FD8', '#944743', '#DBB1CD', '#EC9787', '#00A591', '#6B5B95', '#6C4F3D', '#EADEDB', '#BC70A4', '#BFD641']

f, ax = plt.subplots(figsize=(15, 7))

plt.xlabel('Months')
plt.ylabel('Amount of Movies Released')
plt.title('Movies Released in 2018')

plt.bar(key_movie_2018, value_movie_2018, color=color)
for index, value in enumerate(value_movie_2018):
    plt.text(x_axis[index] - 0.15, value + 2.0, str(value))
    
plt.grid(color='#B4B7BA', linestyle='--', linewidth=1, axis='y', alpha=1)

plt.show()


# ### Summary
# 
# As we can see from the data above, **October** was the month were the most movies were released on Netflix. It seems like **October, November, and December** all have very high numbers when movies were released on Netflix; which we could assume that Netflix was releasing more movies due to the winter holidays, so viewers would have plenty of options to watch.
# 
# **March** came in the second highest, which could easily be due to prepare for the upcoming summer months when many viewers are no longer in school, making it more easier for them to have many options to watch when the summer arrives. **July and August** also have a high count of movies released, which could also be due to the summer months.
# 
# Surprisingly, **June** has the lowest number of movies released even though June is the month that is considered to be the beginning of summer vacation.

# <br>
# <hr>

# ## 7. TV Shows That Only Have One Season
# 
# We are going to create a list to figure out what TV shows have **one season**\* using `netflix_titles` and `netflix_duration`. It would also be useful to include the amount of shows the have one season as well.
# 
# \*This is **not** TV shows that lasted **only** one season, but TV shows that have only one season so far. There may be more seasons for some of them in the future (or not), but as of now with the data, it will only be shown as having one season.

# In[114]:


count_seasons_tv = []

def one_season_tv():
    
    tv_show_list = []
    one_season_list = []
    one_season_dict = {}
    
    count_one_season = {}
    count_rest_tv = {}
    
    for index in range(0, len(netflix_show_id)):
        one_season_dict.update({
            "Title": netflix_title[index],
            "Type": netflix_type[index],
            "Duration" : netflix_duration[index]
        })
        #print(one_season_dict)
        tv_show_list.append(one_season_dict.copy())
    #print(tv_show_list)
    
    tv_show_list = [tv for tv in tv_show_list if tv["Type"] == "TV Show"]
    #print(tv_show_list)
    num_all_tv_shows = len([tv for tv in tv_show_list if isinstance(tv, dict)])
    #print(num_all_tv_shows)
    
    one_season_list = [tv for tv in tv_show_list if tv["Duration"] == "1 Season"]
    #print(one_season_list)
    num_one_season = len([tv for tv in one_season_list if isinstance(tv, dict)])
    #print(num_one_season)
    
    num_rest_tv_shows = num_all_tv_shows - num_one_season
    
    count_one_season["One Season"] = num_one_season
    count_seasons_tv.append(count_one_season)
    
    count_rest_tv["Two or More Seasons"] = num_rest_tv_shows
    count_seasons_tv.append(count_rest_tv)
    
    #print("Out of " + str(num_all_tv_shows) + " TV Shows, " + str(num_one_season) + " have one season.")
    #print("")
    
    print("TV Shows with One Season:")
    for tv in one_season_list:
        for key, value in tv.items():
            if key == "Title":
                print("- " + value)
    
one_season_tv()    


# In[148]:


from matplotlib import pyplot as plt
import numpy as np 

season_key = []
season_value = []

for show in count_seasons_tv:
    #print(show)
    for key, value in show.items():
        season_key.append(key)
        season_value.append(value)

#print(season_key)
#print(season_value)


#--------------------------------------------------------------------
#GRAPH

def my_format(x):
    return '{:.0f}%\n\n{:.0f} Shows'.format(x, total * x/100)

plt.figure(figsize=(8, 8))
total = 2676

pie_values = np.array(season_value)
colors = ['lavender', '#FDAC53']
wedge_props = {"linewidth": 1, "edgecolor": "gray"}

#autopct = lambda p: '{:.0f} Shows'.format(p * total/100) also works to get the value as well
plt.pie(pie_values, labels = season_key, autopct = my_format, 
        colors = colors, wedgeprops = wedge_props, textprops={'fontsize': 15})
plt.title("TV Show Seasons", fontsize = 20)

plt.show()


# ### Summary
# 
# From the data and graph, we can see that there are 1,793 TV shows (67%) listed, which is the majority, that have a duration of at least one season compared to the 883 TV shows (33%) that have two or more seasons.
# 
# So from this data, we could assume that most of the TV shows that are released on Netflix will mostly likely have only one season, with a small chance of having another season.

# <br>
# <hr>

# ## 8. Find the Most Popular Genre of Movies and TV Shows
# 
# We want to find what was the most popular genre in both movies and TV shows. We'll be using `netflix_listed_in` to find the different genres; and because there are multiple genres listed to each TV show and movie, we will only be taking the first genre listed and using that to create the data. 
# 
# Also, since we're finding both movies and TV shows, we'll need to use `netflix_type` as well.

# In[3]:


updated_netflix_genre = []

genre_tv_list = []
genre_list_length = []

def popular_genre_tv():
    
    tv_show_list = []
    tv_dict = {}
    
    int_tv_show_list = []
    crime_tv_show_list = []
    docu_tv_show_list = []
    tv_dram_show_list = []
    british_tv_show_list = []
    tv_com_list = []
    kid_tv_list = []
    real_tv_list = []
    anime_ser_list = []
    action_adventure_list = []
    comedy_talkshow_list = []
    classic_cult_list = []
    romantic_tv_list = []
    horror_tv_list = []
    spanish_tv_list = []
    scifi_fantasy_list = []
    
    for genre in netflix_listed_in:
        genre = genre.split(",")
        #print(genre[0])
        updated_netflix_genre.append(genre[0])
    #print(updated_netflix_genre)  
    
    for index in range(0, len(netflix_show_id)):
        tv_dict.update({
            "Title" : netflix_title[index],
            "Type" : netflix_type[index],
            "Genre" : updated_netflix_genre[index]
        })
        #print(tv_dict)
        tv_show_list.append(tv_dict.copy())
    #print(tv_show_list)
    
    tv_show_list = [tv for tv in tv_show_list if tv["Type"] == "TV Show"]
    #print(tv_show_list)
    
    updated_tv_show_list = [tv for tv in tv_show_list if tv["Genre"] != '']
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if key == "Genre":
                #print(value)
                genre_tv_list.append(value)
        #print(show)
    #print(genre_tv_list)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "International TV Shows":
                int_tv_show_list.append(value)
    international_tv_shows = len(int_tv_show_list)
    #print(international_tv_shows)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Crime TV Shows":
                crime_tv_show_list.append(value)
    crime_tv_shows = len(crime_tv_show_list)
    #print(crime_tv_shows)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Docuseries":
                docu_tv_show_list.append(value)
    docuseries = len(docu_tv_show_list)
    #print(docuseries)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "TV Dramas":
                tv_dram_show_list.append(value)
    tv_dramas = len(tv_dram_show_list)
    #print(tv_dramas)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "British TV Shows":
                british_tv_show_list.append(value)
    british_tv_shows = len(british_tv_show_list)
    #print(british_tv_shows)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "TV Comedies":
                tv_com_list.append(value)
    tv_comedies = len(tv_com_list)
    #print(tv_comedies)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Kids' TV":
                kid_tv_list.append(value)
    kids_tv = len(kid_tv_list)
    #print(kids_tv)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Reality TV":
                real_tv_list.append(value)
    reality_tv = len(real_tv_list)
    #print(reality_tv)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Anime Series":
                anime_ser_list.append(value)
    anime_series = len(anime_ser_list)
    #print(anime_series)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "TV Action & Adventure":
                action_adventure_list.append(value)
    tv_action_adventure = len(action_adventure_list)
    #print(tv_action_adventure)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Stand-Up Comedy & Talk Shows":
                comedy_talkshow_list.append(value)
    standup_comedy_talkshows = len(comedy_talkshow_list)
    #print(standup_comedy_talkshows)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Classic & Cult TV":
                classic_cult_list.append(value)
    classic_cult_tv = len(classic_cult_list)
    #print(classic_cult_tv)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Romantic TV Shows":
                romantic_tv_list.append(value)
    romantic_tv_shows = len(romantic_tv_list)
    #print(romantic_tv_shows)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "TV Horror":
                horror_tv_list.append(value)
    tv_horror = len(horror_tv_list)
    #print(tv_horror)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "Spanish-Language TV Shows":
                spanish_tv_list.append(value)
    spanish_language_tv_shows = len(spanish_tv_list)
    #print(spanish_language_tv_shows)
    
    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "TV Sci-Fi & Fantasy":
                scifi_fantasy_list.append(value)
    tv_scifi_fantasy = len(scifi_fantasy_list)
    #print(tv_scifi_fantasy)
    
    
    genre_list_length.append(international_tv_shows)
    genre_list_length.append(crime_tv_shows)
    genre_list_length.append(docuseries)
    genre_list_length.append(tv_dramas)
    genre_list_length.append(british_tv_shows)
    genre_list_length.append(tv_comedies)
    genre_list_length.append(kids_tv)
    genre_list_length.append(reality_tv)
    genre_list_length.append(anime_series)
    genre_list_length.append(tv_action_adventure)
    genre_list_length.append(standup_comedy_talkshows)
    genre_list_length.append(classic_cult_tv)
    genre_list_length.append(romantic_tv_shows)
    genre_list_length.append(tv_horror)
    genre_list_length.append(spanish_language_tv_shows)
    genre_list_length.append(tv_scifi_fantasy)
    
    
popular_genre_tv()


# In[4]:


genre_movie_list = []
genre_movie_length = []

def popular_genre_movie():
    
    movie_list = []
    movie_dict = {}
    
    doc_movie_list = []
    child_fam_movie_list = []
    drama_movie_list = []
    comedy_movie_list = []
    thriller_movie_list = []
    horror_movie_list = []
    action_adv_movie_list = []
    int_movie_list = []
    scifi_fantasy_movie_list = []
    classic_movie_list = []
    standup_comedy_movie_list = []
    anime_movie_list = []
    cult_movie_list = []
    independ_movie_list = []
    music_movie_list = []
    romantic_movie_list = []
    lgbtq_movie_list = []
    sport_movie_list = []
    
    for index in range(0, len(netflix_show_id)):
        movie_dict.update({
            "Title" : netflix_title[index],
            "Type" : netflix_type[index],
            "Genre" : updated_netflix_genre[index]
        })
        movie_list.append(movie_dict.copy())
    #print(movie_list)
    
    movie_list = [m for m in movie_list if m["Type"] == "Movie"]
    #print(movie_list)
    
    updated_movie_list = [m for m in movie_list if m["Genre"] != '']
    for movie in updated_movie_list:
        for key, value in movie.items():
            if key == "Genre":
                #print(value)
                genre_movie_list.append(value)
        #print(movie)
    #print(genre_movie_list)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Documentaries":
                doc_movie_list.append(value)
    documentaries = len(doc_movie_list)
    #print(documentaries)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Children & Family Movies":
                child_fam_movie_list.append(value)
    children_family_movies = len(child_fam_movie_list)
    #print(children_family_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Dramas":
                drama_movie_list.append(value)
    dramas = len(drama_movie_list)
    #print(dramas)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Comedies":
                comedy_movie_list.append(value)
    comedies = len(comedy_movie_list)
    #print(comedies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Thrillers":
                thriller_movie_list.append(value)
    thrillers = len(thriller_movie_list)
    #print(thrillers)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Horror Movies":
                horror_movie_list.append(value)
    horror_movies = len(horror_movie_list)
    #print(horror_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Action & Adventure":
                action_adv_movie_list.append(value)
    action_adventure = len(action_adv_movie_list)
    #print(action_adventure)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "International Movies":
                int_movie_list.append(value)
    international_movies = len(int_movie_list)
    #print(international_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Sci-Fi & Fantasy":
                scifi_fantasy_movie_list.append(value)
    scifi_fantasy = len(scifi_fantasy_movie_list)
    #print(scifi_fantasy)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Classic Movies":
                classic_movie_list.append(value)
    classic_movies = len(classic_movie_list)
    #print(classic_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Stand-Up Comedy":
                standup_comedy_movie_list.append(value)
    standup_comedy = len(standup_comedy_movie_list)
    #print(standup_comedy)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Anime Features":
                anime_movie_list.append(value)
    anime_features = len(anime_movie_list)
    #print(anime_features)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Cult Movies":
                cult_movie_list.append(value)
    cult_movies = len(cult_movie_list)
    #print(cult_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Independent Movies":
                independ_movie_list.append(value)
    independent_movies = len(independ_movie_list)
    #print(independent_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Music & Musicals":
                music_movie_list.append(value)
    music_musicals = len(music_movie_list)
    #print(music_musicals)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Romantic Movies":
                romantic_movie_list.append(value)
    romantic_movies = len(romantic_movie_list)
    #print(romantic_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "LGBTQ Movies":
                lgbtq_movie_list.append(value)
    lgbtq_movies = len(lgbtq_movie_list)
    #print(lgbtq_movies)
    
    for movie in updated_movie_list:
        for key, value in movie.items():
            if value == "Sports Movies":
                sport_movie_list.append(value)
    sports_movies = len(sport_movie_list)
    #print(sports_movies)
    
    
    genre_movie_length.append(documentaries)
    genre_movie_length.append(children_family_movies)
    genre_movie_length.append(dramas)
    genre_movie_length.append(comedies)
    genre_movie_length.append(thrillers)
    genre_movie_length.append(horror_movies)
    genre_movie_length.append(action_adventure)
    genre_movie_length.append(international_movies)
    genre_movie_length.append(scifi_fantasy)
    genre_movie_length.append(classic_movies)
    genre_movie_length.append(standup_comedy)
    genre_movie_length.append(anime_features)
    genre_movie_length.append(cult_movies)
    genre_movie_length.append(independent_movies)
    genre_movie_length.append(music_musicals)
    genre_movie_length.append(romantic_movies)
    genre_movie_length.append(lgbtq_movies)
    genre_movie_length.append(sports_movies)
    
    
popular_genre_movie()


# In[45]:


from matplotlib import pyplot as plt
import numpy as np 

#labels for tv
tv_genre_list = list(dict.fromkeys(genre_tv_list))
tv_genre_list.remove("TV Shows")
#print(tv_genre_list)

#x-axis for tv
#print(genre_list_length)


#labels for movie
movie_genre_list = list(dict.fromkeys(genre_movie_list))
movie_genre_list.remove("Movies")
#print(movie_genre_list)

#x-axis for movie
#print(genre_movie_length)

#--------------------------------------------------------#
#GRAPH

mycolors_one = ['#F29BCB', '#2A2359', '#0634BF', '#0460D9', '#F2BFBB', '#0AA6A6', '#D95829', '#D92A1A', '#0D0D0D', '#C04BF2', '#52B5F2', '#1B3940', '#F2A341', '#F26B6B', '#8C4552', '#D9D7D8']
mycolors_two = ['#F29BCB', '#2A2359', '#0634BF', '#0460D9', '#F2BFBB', '#0AA6A6', '#D95829', '#D92A1A', '#0D0D0D', '#C04BF2', '#52B5F2', '#1B3940', '#F2A341', '#F26B6B', '#8C4552', '#D9D7D8', '#73655D', '#F2845C']

                                    #rows, columns
fig, (chart1, chart2) = plt.subplots(2, 1, figsize=(15, 15))
                                    
chart1.barh(tv_genre_list, genre_list_length, color = mycolors_one)
chart2.barh(movie_genre_list, genre_movie_length, color = mycolors_two)

chart1.set_title("TV Show Genres", fontsize = 15)
chart2.set_title("Movie Genres", fontsize = 15)

for index, value in enumerate(genre_list_length):
    chart1.text(value + 3.0, index - 0.1, str(value))

for index, value in enumerate(genre_movie_length):
    chart2.text(value + 4.0, index - 0.15, str(value))

plt.show()


#---------------------------------------------------
#If I wanted to make the chart a pie graph, I could use this code below


#first_pie = np.array(genre_list_length)
#first_labels = [f'{tv_genre_list} - {genre_list_length:.0f}' for tv_genre_list, genre_list_length in zip(tv_genre_list, genre_list_length)]
#myexplode_one = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
#mycolors_one = ['#F29BCB', '#2A2359', '#0634BF', '#0460D9', '#F2BFBB', '#0AA6A6', '#D95829', '#D92A1A', '#0D0D0D', '#C04BF2', '#52B5F2', '#1B3940', '#F2A341', '#F26B6B', '#8C4552', '#D9D7D8']

#second_pie = np.array(genre_movie_length)
#second_labels = [f'{movie_genre_list} - {genre_movie_length:.0f}' for movie_genre_list, genre_movie_length in zip(movie_genre_list, genre_movie_length)]
#myexplode_two = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
#mycolors_two = ['#F29BCB', '#2A2359', '#0634BF', '#0460D9', '#F2BFBB', '#0AA6A6', '#D95829', '#D92A1A', '#0D0D0D', '#C04BF2', '#52B5F2', '#1B3940', '#F2A341', '#F26B6B', '#8C4552', '#D9D7D8', '#73655D', '#F2845C']

#fig, (pie1, pie2) = plt.subplots(2, 1, figsize=(32, 32))
#pie1.pie(first_pie, explode = myexplode_one, colors = mycolors_one)
#pie2.pie(second_pie, explode = myexplode_two, colors = mycolors_two)

#pie1.set_title("TV Show Genres", fontsize=20)
#pie2.set_title("Movie Genres", fontsize=20)

#pie1.legend(first_labels)
#pie2.legend(second_labels)

#plt.show()


# ### Summary
# 
# In the *TV Show Genres* graph, it is shown that a majority of TV shows are part of the **International TV Shows** genre; while in the *Movie Genres* graph, the majority of movies are in the **Dramas** genre with **Comedies** coming in close to Dramas. Therefore, we could safely assume that a TV show released onto Netflix will most likely be an international TV show; while a movie released onto Netflix will most likely be a drama or a comedy*.
# 
# \*It must be noted that in the TV Show category, there was a *TV Show* genre which was deleted because "TV Show" is not a genre; however, it may be that many TV shows were put into that category. In the Movie category, there was also a genre called "Movie" which was deleted as well.

# <br>
# <hr>

# ## 9. Find TV Shows That Were Created Outside the United States.
# 
# We want to know what TV shows were created and filmed from other countries other than the United States; as well as finding out how many TV shows each country has released on Netflix. We will need to use `netflix_country` to find the different countries*. Also, since we are only finding TV shows, we will need to use `netflix_type` to remove all the movies as well.
# 
# *Because there are some Netflix titles that have more than one country where it was filmed, we will only use the first country listed as the first country is where the majority of the movie was filmed.

# In[106]:


country_list = []
number_of_countries = []

def international_tv_shows():
    
    tv_show_list = []
    tv_show_dict = {}
    
    updated_netflix_country = []
    
    countries = []
    s_africa_list = []
    india_list = []
    uk_list = []
    mex_list = []
    turk_list = []
    aus_list = []
    s_korea_list = []
    fin_list = []
    nigeria_list = []
    jap_list = []
    bel_list = []
    fra_list = []
    spa_list = []
    rus_list = []
    ire_list = []
    ita_list = []
    argen_list = []
    jor_list = []
    colombia_list = []
    israel_list = []
    taiwan_list = []
    ger_list = []
    can_list = []
    pol_list = []
    thai_list = []
    swe_list = []
    chi_list = []
    ice_list = []
    den_list = []
    phil_list = []
    uae_list = []
    nor_list = []
    leb_list = []
    uru_list = []
    egypt_list = []
    lux_list = []
    braz_list = []
    senegal_list = []
    neth_list = []
    sa_list = []
    kuwait_list = []
    indo_list = []
    belar_list = []
    chile_list = []
    pr_list = []
    austria_list = []
    cyp_list = []
    maur_list = []
    sing_list = []
    malay_list = []
    hk_list = []
    nz_list = []
    cro_list = []
    cr_list = []
    paki_list = []
    ukr_list = []
    swiss_list = []
    
    for country in netflix_country:
        country = country.split(",")
        #print(country[0])
        updated_netflix_country.append(country[0])
    #print(updated_netflix_country)
    
    for index in range(0, len(netflix_show_id)):
        tv_show_dict.update({
             "ID" : netflix_show_id[index],
             "Title": netflix_title[index],
             "Country" : updated_netflix_country[index],
             "Type" : netflix_type[index]
         })
        #print(tv_show_dict)
        tv_show_list.append(tv_show_dict.copy())
    #print(tv_show_list)
    
    
    tv_show_list = [tv for tv in tv_show_list if tv["Type"] == "TV Show"]
    #print(tv_show_list)
    
    updated_tv_show_list = [tv for tv in tv_show_list if tv["Country"] != '' and tv["Country"] != "United States"]
    #print(updated_tv_show_list)
    
    for show in updated_tv_show_list:
        #print(show)
        for key, value in show.items():
            if key == "Country":
                #print(value)
                countries.append(value)
    #print(countries)
    
    list_of_countries = list(dict.fromkeys(countries))
    #print(list_of_countries)
    for country in list_of_countries:
        #print(country)
        country_list.append(country)

    for show in updated_tv_show_list:
        for key, value in show.items():
            if value == "South Africa":
                s_africa_list.append(value)
            if value == "India":
                india_list.append(value)
            if value == "United Kingdom":
                uk_list.append(value)
            if value == "Mexico":
                mex_list.append(value)
            if value == "Turkey":
                turk_list.append(value)
            if value == "Australia":
                aus_list.append(value)
            if value == "South Korea":
                s_korea_list.append(value)
            if value == "Finland":
                fin_list.append(value)
            if value == "Nigeria":
                nigeria_list.append(value)
            if value == "Japan":
                jap_list.append(value)
            if value == "Belgium":
                bel_list.append(value)
            if value == "France":
                fra_list.append(value)
            if value == "Spain":
                spa_list.append(value)
            if value == "Russia":
                rus_list.append(value)
            if value == "Ireland":
                ire_list.append(value)
            if value == "Italy":
                ita_list.append(value)
            if value == "Argentina":
                argen_list.append(value)
            if value == "Jordan":
                jor_list.append(value)
            if value == "Colombia":
                colombia_list.append(value)
            if value == "Israel":
                israel_list.append(value)
            if value == "Taiwan":
                taiwan_list.append(value)
            if value == "Germany":
                ger_list.append(value)
            if value == "Canada":
                can_list.append(value)
            if value == "Poland":
                pol_list.append(value)
            if value == "Thailand":
                thai_list.append(value)
            if value == "Sweden":
                swe_list.append(value)
            if value == "China":
                chi_list.append(value)
            if value == "Iceland":
                ice_list.append(value)
            if value == "Denmark":
                den_list.append(value)
            if value == "Philippines":
                phil_list.append(value)
            if value == "United Arab Emirates":
                uae_list.append(value)
            if value == "Norway":
                nor_list.append(value)
            if value == "Lebanon":
                leb_list.append(value)
            if value == "Uruguay":
                uru_list.append(value)
            if value == "Egypt":
                egypt_list.append(value)
            if value == "Luxembourg":
                lux_list.append(value)
            if value == "Brazil":
                braz_list.append(value)
            if value == "Senegal":
                senegal_list.append(value)
            if value == "Netherlands":
                neth_list.append(value)
            if value == "Saudi Arabia":
                sa_list.append(value)
            if value == "Kuwait":
                kuwait_list.append(value)
            if value == "Indonesia":
                indo_list.append(value)
            if value == "Belarus":
                belar_list.append(value)
            if value == "Chile":
                chile_list.append(value)
            if value == "Puerto Rico":
                pr_list.append(value)
            if value == "Austria":
                austria_list.append(value)
            if value == "Cyprus":
                cyp_list.append(value)
            if value == "Mauritius":
                maur_list.append(value)
            if value == "Singapore":
                sing_list.append(value)
            if value == "Malaysia":
                malay_list.append(value)
            if value == "Hong Kong":
                hk_list.append(value)
            if value == "New Zealand":
                nz_list.append(value)
            if value == "Croatia":
                cro_list.append(value)
            if value == "Czech Republic":
                cr_list.append(value)
            if value == "Pakistan":
                paki_list.append(value)
            if value == "Ukraine":
                ukr_list.append(value)
            if value == "Switzerland":
                swiss_list.append(value)
    
    south_africa = len(s_africa_list)
    #print(south_africa)
    india = len(india_list)
    #print(india)
    united_kingdom = len(uk_list)
    #print(united_kingdom)
    mexico = len(mex_list)
    #print(mexico)
    turkey = len(turk_list)
    #print(turkey)
    australia = len(aus_list)
    #print(australia)
    south_korea = len(s_korea_list)
    #print(south_korea)
    finland = len(fin_list)
    #print(finland)
    nigeria = len(nigeria_list)
    #print(nigeria)
    japan = len(jap_list)
    #print(japan)
    belgium = len(bel_list)
    #print(belgium)
    france = len(fra_list)
    #print(france)
    spain = len(spa_list)
    #print(spain)
    russia = len(rus_list)
    #print(russia)
    ireland = len(ire_list)
    #print(ireland)
    italy = len(ita_list)
    #print(italy)
    argentina = len(argen_list)
    #print(argentina)
    jordan = len(jor_list)
    #print(jordan)
    colombia = len(colombia_list)
    #print(colombia)
    israel = len(israel_list)
    #print(israel)
    taiwan = len(taiwan_list)
    #print(taiwan)
    germany = len(ger_list)
    #print(germany)
    canada = len(can_list)
    #print(canada)
    poland = len(pol_list)
    #print(poland)
    thailand = len(thai_list)
    #print(thailand)
    sweden = len(swe_list)
    #print(sweden)
    china = len(chi_list)
    #print(china)
    iceland = len(ice_list)
    #print(iceland)
    denmark = len(den_list)
    #print(denmark)
    philippines = len(phil_list)
    #print(philippines)
    uae = len(uae_list)
    #print(uae)
    norway = len(nor_list)
    #print(norway)
    lebanon = len(leb_list)
    #print(lebanon)
    uruguay = len(uru_list)
    #print(uruguay)
    egypt = len(egypt_list)
    #print(egypt)
    luxembourg = len(lux_list)
    #print(luxembourg)
    brazil = len(braz_list)
    #print(brazil)
    senegal = len(senegal_list)
    #print(senegal)
    netherlands = len(neth_list)
    #print(netherlands)
    saudi_arabia = len(sa_list)
    #print(saudi_arabia)
    kuwait = len(kuwait_list)
    #print(kuwait)
    indonesia = len(indo_list)
    #print(indonesia)
    belarus = len(belar_list)
    #print(belarus)
    chile = len(chile_list)
    #print(chile)
    puerto_rico = len(pr_list)
    #print(puerto_rico)
    austria = len(austria_list)
    #print(austria)
    cyprus = len(cyp_list)
    #print(cyprus)
    mauritius = len(maur_list)
    #print(mauritius)
    singapore = len(sing_list)
    #print(singapore)
    malaysia = len(malay_list)
    #print(malaysia)
    hong_kong = len(hk_list)
    #print(hong_kong)
    new_zealand = len(nz_list)
    #print(new_zealand)
    croatia = len(cro_list)
    #print(croatia)
    czech_republic = len(cr_list)
    #print(czech_republic)
    pakistan = len(paki_list)
    #print(pakistan)
    ukraine = len(ukr_list)
    #print(ukraine)
    switzerland = len(swiss_list)
    #print(switzerland)
    
    
    number_of_countries.append(south_africa)
    number_of_countries.append(india)
    number_of_countries.append(united_kingdom)
    number_of_countries.append(mexico)
    number_of_countries.append(turkey)
    number_of_countries.append(australia)
    number_of_countries.append(south_korea)
    number_of_countries.append(finland)
    number_of_countries.append(nigeria)
    number_of_countries.append(japan)
    number_of_countries.append(belgium)
    number_of_countries.append(france)
    number_of_countries.append(spain)
    number_of_countries.append(russia)
    number_of_countries.append(ireland)
    number_of_countries.append(italy)
    number_of_countries.append(argentina)
    number_of_countries.append(jordan)
    number_of_countries.append(colombia)
    number_of_countries.append(israel)
    number_of_countries.append(taiwan)
    number_of_countries.append(germany)
    number_of_countries.append(canada)
    number_of_countries.append(poland)
    number_of_countries.append(thailand)
    number_of_countries.append(sweden)
    number_of_countries.append(china)
    number_of_countries.append(iceland)
    number_of_countries.append(denmark)
    number_of_countries.append(philippines)
    number_of_countries.append(uae)
    number_of_countries.append(norway)
    number_of_countries.append(lebanon)
    number_of_countries.append(uruguay)
    number_of_countries.append(egypt)
    number_of_countries.append(luxembourg)
    number_of_countries.append(brazil)
    number_of_countries.append(senegal)
    number_of_countries.append(netherlands)
    number_of_countries.append(saudi_arabia)
    number_of_countries.append(kuwait)
    number_of_countries.append(indonesia)
    number_of_countries.append(belarus)
    number_of_countries.append(chile)
    number_of_countries.append(puerto_rico)
    number_of_countries.append(austria)
    number_of_countries.append(cyprus)
    number_of_countries.append(mauritius)
    number_of_countries.append(singapore)
    number_of_countries.append(malaysia)
    number_of_countries.append(hong_kong)
    number_of_countries.append(new_zealand)
    number_of_countries.append(croatia)
    number_of_countries.append(czech_republic)
    number_of_countries.append(pakistan)
    number_of_countries.append(ukraine)
    number_of_countries.append(switzerland)
    
    
international_tv_shows()


# In[120]:


from matplotlib import pyplot as plt
import numpy as np 

#print(country_list)
#print(number_of_countries)

list_of_countries = {key:value for key, value in zip(country_list, number_of_countries)}
#print(list_of_countries)

new_list_of_countries = dict(sorted(list_of_countries.items(), key=lambda item: item[1]))
#print(new_list_of_countries)

countries = []
number_of_shows = []

for key, value in new_list_of_countries.items():
    #print(key + ' ' + str(value))
    countries.append(key)
    number_of_shows.append(value)
    
#print(countries)
#print(number_of_shows)

#------------------------------------------------------#
#GRAPH
fig, ax = plt.subplots(figsize=(15, 30))
mycolors = ['#F27999', '#D9296A', '#D5EFF2', '#F2B705', '#D98E04', '#CCCCFF', '#7D7DB3', '#FFCCB3', '#DAFFDE', '#91B386']

#the barh graph will print in reverse whatever is in the lists
plt.barh(countries, number_of_shows, align = 'center', height = 0.8, color = mycolors)

for index, value in enumerate(number_of_shows):
    plt.text(value + 1.0, index - 0.15, str(value))
    
plt.title("TV Shows on Netflix Outside the U.S.", fontsize = 15)

plt.show()


# ### Summary
# 
# Based on the graph, the United Kingdom has the most TV shows on Netflix, with Japan coming in second, and South Korea coming in third. However, I will note that if you add all the East Asian countries together (Japan, South Korea, Taiwan, China), you'll have at least 450 TV shows in the *East Asian* category.
# 
# So therefore, we could safely assume that there will be a high chance a TV show released on Netflix will be from the United Kingdom; or an East Asian country, most likely Japan or South Korea.

# <hr>
# 
# [<sup id="fn1">1</sup>](#fn1-back) Data and description are written by Shivam Bansal; which is provided by *[Kaggle](https://www.kaggle.com/shivamb/netflix-shows)*.
