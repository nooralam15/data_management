#Data management assignment

#Create a global variabe array 
movies = [{"title": "The Shining", "genre": "horror", "year": 1980, "rating": 93}, {"title": "Daddy's Home", "genre": "comedy", "year": 2015, "rating": 49}, {"title": "The Notebook", "genre": "romance", "year": 2004, "rating": 85}, {"title": "Love Rosie", "genre": "romance", "year": 2014, "rating": 63}, {"title": "21 Jump Street", "genre": "comedy", "year": 2012, "rating": 82}, {"title": "Super Bad", "genre": "comedy", "year": 2007, "rating": 87}, {"title": "Back to the Future", "genre": "sci-fi", "year": 1985, "rating": 94}, {"title": "The Excorsist", "genre": "horror", "year": 1973, "rating": 87}, {"title": "Texas Chainsaw Massacre", "genre": "horror", "year": 1974, "rating": 82}, {"title": "The Hunger Games", "genre": "sci-fi", "year": 2012, "rating": 81}, {"title": "Titanic", "genre": "romance", "year": 1997, "rating": 69}, {"title": "Avatar", "genre": "sci-fi", "year": 2009, "rating": 82}, {"title": "American Psycho", "genre": "horror", "year": 2000, "rating": 85}, {"title": "The Dark Knight", "genre": "action", "year": 2008, "rating": 94}, {"title": "G.I. Jane", "genre": "action", "year": 1997, "rating": 51}, {"title": "The Wolf of Wall Street", "genre": "comedy", "year": 2013, "rating": 83}, {"title": "Joker", "genre": "action", "year": 2019, "rating": 88}, {"title": "The Conjuring", "genre": "horror", "year": 2013, "rating": 83}]

#Create a global favorites list
favorites = []


# Convert data to a json string
json_string = json.dumps(favorites)

# The data as a JSON string may be easily saved to a file
file = open("data.txt", "w")
file.write(json_string)
file.close()

# Load a JSON string from a file
file = open("data.txt", "r")
json_string_from_file = file.read()
file.close()

# the loads() method will convert a json string to data
data2 = json.loads(json_string_from_file)
for data in data2:
    print(data)

#Create a function that will remove from favorites
def removeFromFavorites(title):
    for data in favorites: 
        if data == title:
            favorites.remove(title)
        else: 
            print("title not found")


#Create a function that will add to favorites
def addToFavorites(title):
    for info in movies: 
        if info["title"] == title:
            favorites.append(title)   
        else: 
            print("title not found")
            

#Create a function that will display movies by genre
def displayGenre(genre):
    for i in range(len(movies)):
        if movies[i]["genre"] == genre:
            print(genre + ": " + movies[i]["title"])

#create a function that will display all the movie data
def allMovies():
    for info in movies:
        print(info)
    

#Create a menu function
def menu():
    #Create a looping variable that will rerun the menu
    loop = True
    while loop: 

        userInp = int(input("Enter the number to access the menu option \n 1. All movie info \n 2. Display by Genre \n 3. Add movie to favorite list \n 4. Remove movie from favorites \n 5. Display Favorites \n 6. Logout  \n"))

        if userInp == 1:
            allMovies() 

        elif userInp == 2:
            genre = input("Pick a genre from the list: horror, romance, comedy, action, sci-fi: ")
            displayGenre(genre)

        elif userInp == 3:
            title = input("Enter a movie title to add to favorites: ")
            addToFavorites(title)

        elif userInp == 4:
            title = input("Enter a movie title to remove from favorites: ")
            removeFromFavorites(title)

    


menu()
    
