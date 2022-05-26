#Data management assignment

#Import library 
import json

#Create global variabe arrays 
movies = [{"title": "The Shining", "genre": "horror", "year": 1980, "rating": 93}, {"title": "Daddy's Home", "genre": "comedy", "year": 2015, "rating": 49}, {"title": "The Notebook", "genre": "romance", "year": 2004, "rating": 85}, {"title": "Love Rosie", "genre": "romance", "year": 2014, "rating": 63}, {"title": "21 Jump Street", "genre": "comedy", "year": 2012, "rating": 82}, {"title": "Super Bad", "genre": "comedy", "year": 2007, "rating": 87}, {"title": "Back to the Future", "genre": "sci-fi", "year": 1985, "rating": 94}, {"title": "The Excorsist", "genre": "horror", "year": 1973, "rating": 87}, {"title": "Texas Chainsaw Massacre", "genre": "horror", "year": 1974, "rating": 82}, {"title": "The Hunger Games", "genre": "sci-fi", "year": 2012, "rating": 81}, {"title": "Titanic", "genre": "romance", "year": 1997, "rating": 69}, {"title": "Avatar", "genre": "sci-fi", "year": 2009, "rating": 82}, {"title": "American Psycho", "genre": "horror", "year": 2000, "rating": 85}, {"title": "The Dark Knight", "genre": "action", "year": 2008, "rating": 94}, {"title": "G.I. Jane", "genre": "action", "year": 1997, "rating": 51}, {"title": "The Wolf of Wall Street", "genre": "comedy", "year": 2013, "rating": 83}, {"title": "Joker", "genre": "action", "year": 2019, "rating": 88}, {"title": "The Conjuring", "genre": "horror", "year": 2013, "rating": 83}]

users = []

#Create a global favorites list
favorites = []

#Create a function adds data to the json file
def jsonAdd():
    # Convert data to a json string
    json_string = json.dumps(favorites)
    #store in a file
    file = open("data.txt", "w")
    file.write(json_string)
    file.close()


#Create a function that loads the json file and stores in a string
def loadjson():
    # Load a JSON string from a file
    file = open("data.txt", "r")
    json_string_from_file = file.read()
    file.close()
    #convert a json string to data
    data2 = json.loads(json_string_from_file)
    return data2

#Create a function that displays the json favroties list
def displayData(data):
    for info in data:
        print(info)

#cerate a linear search function
def linearSearch(movies, title):
    for element in movies:
        if element["title"] == title:
            return element
    return -1


#Create a function that will remove from favorites
def removeFromFavorites(title):
    results = linearSearch(movies, title)
    if results == -1:
        print("Title not found")
    else:
        favorites.remove(title)
        jsonAdd()
        print('title removed')


#Create a function that will add to favorites
def addToFavorites(title):
    results = linearSearch(movies, title)
    if results == -1:
        print("Title not found")
    else:
        favorites.append(title)
        jsonAdd()
        print('title added')
            

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
        #load the json file
        loadjson()

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

        elif userInp == 5:
            dataArray = loadjson()
            displayData(dataArray)



#Create a login check function 
def login():
    username = input("Enter username: ")
    result = linearSearch()
#Create a login menu
def loginMenu():
    userInp = int(input("Enter the number to access the menu option \n 1. Login \n 2. Sign Up \n 3. Exit \n "))

    if userInp == 1:
        login()

menu()
    