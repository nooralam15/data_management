#Data management assignment

#Import library 
import json

#Create global variabe arrays 
movies = [{"title": "The Shining", "genre": "horror", "year": 1980, "rating": 93}, {"title": "Daddy's Home", "genre": "comedy", "year": 2015, "rating": 49}, {"title": "The Notebook", "genre": "romance", "year": 2004, "rating": 85}, {"title": "Love Rosie", "genre": "romance", "year": 2014, "rating": 63}, {"title": "21 Jump Street", "genre": "comedy", "year": 2012, "rating": 82}, {"title": "Super Bad", "genre": "comedy", "year": 2007, "rating": 87}, {"title": "Back to the Future", "genre": "sci-fi", "year": 1985, "rating": 94}, {"title": "The Excorsist", "genre": "horror", "year": 1973, "rating": 87}, {"title": "Texas Chainsaw Massacre", "genre": "horror", "year": 1974, "rating": 82}, {"title": "The Hunger Games", "genre": "sci-fi", "year": 2012, "rating": 81}, {"title": "Titanic", "genre": "romance", "year": 1997, "rating": 69}, {"title": "Avatar", "genre": "sci-fi", "year": 2009, "rating": 82}, {"title": "American Psycho", "genre": "horror", "year": 2000, "rating": 85}, {"title": "The Dark Knight", "genre": "action", "year": 2008, "rating": 94}, {"title": "G.I. Jane", "genre": "action", "year": 1997, "rating": 51}, {"title": "The Wolf of Wall Street", "genre": "comedy", "year": 2013, "rating": 83}, {"title": "Joker", "genre": "action", "year": 2019, "rating": 88}, {"title": "The Conjuring", "genre": "horror", "year": 2013, "rating": 83}]


#Create a function adds data to the json file
def jsonAdd():
    # Convert data to a json string
    json_string = json.dumps(users)
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
    #check to see if the data is empty 
    if json_string_from_file == "":
        return []
    else:
        #convert a json string to data
        data2 = json.loads(json_string_from_file)
        return data2

#Create a function that displays the json favroties list
def displayData(data):
    for info in data:
        print(info)


#Create a global array 
users = loadjson()

#cerate a linear search function
def linearSearch(array, item, instance):
    if instance == "movies":
        for element in array:
            if element["title"] == item:
                return element
        return -1
    elif instance == "users":
        for element in array:
            if element["username"] == item:
                return element
        return -1


#Create a function that will remove from favorites
def removeFromFavorites(title, userFavorites):
    results = linearSearch(title, "movies")
    if results == -1:
        print("Title not found")
    else:
        userFavorites.remove(title)
        jsonAdd()
        print('title removed')


#Create a function that will add to favorites
def addToFavorites(title, userFavorites):
    results = linearSearch(movies, title, "movies")
    if results == -1:
        print("Title not found")
    else:
        userFavorites.append(title)
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
def menu(userFavorites):
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
            addToFavorites(title, userFavorites)

        elif userInp == 4:
            title = input("Enter a movie title to remove from favorites: ")
            removeFromFavorites(title, userFavorites)

        elif userInp == 5:
            displayData(userFavorites)

        elif userInp == 6:
            return -1


#Create a signup function
def signup():
    loop = True
    while loop:
        username = input("Enter username: ")
        password = input("Enter password: ")
        users.append({"username": username, "password": password, "favorites": []})
        print("Signup complete")
        jsonAdd()
        loop = False
    
#Create a login check function 
def login():
    loop = True
    while loop:
        username = input("Enter username: ")
        result = linearSearch(users, username, "users")
        while result == -1:
            print("username not found")
            login()
        password = input("Enter password: ")
        while password != result["password"]:
            print("Wrong password")
            login()
        loopControl = menu(result["favorites"])
        if loopControl == -1:
            loop = False
    
#Create a login menu
def loginMenu():
    loop = True
    while loop:
        userInp = int(input("Enter the number to access the menu option \n 1. Login \n 2. Sign Up \n 3. Exit \n "))

        if userInp == 1:
            login()

        elif userInp == 2:
            signup()

        elif userInp == 3:
            quit()
loginMenu()
    
