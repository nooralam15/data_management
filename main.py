#Data management assignment

#Create a global variabe array 
movies = [{"title": "The Shining", "genre": "horror", "year": 1980, "rating": 93}, {"title": "Daddy's Home", "genre": "comedy", "year": 2015, "rating": 49}, {"title": "The Notebook", "genre": "Romance", "year": 2004, "rating": 85}, {"title": "Love Rosie", "genre": "romance", "year": 2014, "rating": 63}, {"title": "21 Jump Street", "genre": "comedy", "year": 2012, "rating": 82}, {"title": "Super Bad", "genre": "comedy", "year": 2007, "rating": 87}, {"title": "Back to the Future", "genre": "sci-fi", "year": 1985, "rating": 94}, {"title": "The Excorsist", "genre": "horror", "year": 1973, "rating": 87}, {"title": "Texas Chainsaw Massacre", "genre": "horror", "year": 1974, "rating": 82}, {"title": "The Hunger Games", "genre": "sci-fi", "year": 2012, "rating": 81}, {"title": "Titanic", "genre": "roamnce", "year": 1997, "rating": 69}, {"title": "Avatar", "genre": "sci-fi", "year": 2009, "rating": 82}, {"title": "American Psycho", "genre": "horror", "year": 2000, "rating": 85}, {"title": "The Dark Knight", "genre": "action", "year": 2008, "rating": 94}, {"title": "G.I. Jane", "genre": "action", "year": 1997, "rating": 51}, {"title": "The Wolf of Wall Street", "genre": "comedy", "year": 2013, "rating": 83}, {"title": "Joker", "genre": "action", "year": 2019, "rating": 88}, {"title": "The Conjuring", "genre": "horror", "year": 2013, "rating": 83}]


#create a function that will organize and display the data from A-Z
def alphabeticalOrg():
    

#Create a menu function
def menu():
     userInp = int(input("Enter the number to display the data \n 1. A-Z \n 2. Most Recent \n 3. Oldest \n 4. Rating \n 5. Genre \n 6. Exit  \n"))

     if userInp == 1:
         alphabeticalOrg() 
    


menu()
for i in range(len(movies)):
    print(movies[i]["title"])