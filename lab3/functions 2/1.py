def func_1(movies):
    s = input()
    for i in movies:  #if the input name matches the name of a movie in the list and if its imdb score is above 5.5
        if(s == i["name"] and i["imdb"] > 5.5):
            return True
    return False

def func_2(movies):
    a = []   #empty list to store movie names
    for i in movies:
        if(i["imdb"] > 5.5):   #if imdb is above 5.5
            a.append(i["name"])            #condition is met append to the list
    return a

def func_3(movies):
    s = input()
    a = []     #empty list to store movie names
    
    for i in movies:
        if(s == i["category"]):  #if the category of the movie matches the input category
            a.append(i["name"])            #condition is met append to the list
    return a

def func_4(movies):
    a = []
    c = 0   #variable to store the total imdb score
    d = 0   #variable to store the count of movies
    
    print("How many films your list includes?")
    p = int(input())
    
    for i in range(p): 
        s = input()
        a.append(s) 
    
    for i in movies:
        if(i["name"] in a):  #if the name of the movie is in the list provided by the user
            c += i["imdb"]   #condition is met add the imdb score to c
            d += 1           #the count of movies 
    return c/d

def func_5(movies):
    s = input()
    c = 0      #variable to store the total imdb score
    d = 0      #variable to store the count of movies
    
    
    for i in movies:
        if(s == i["category"]):  #if the category of the movie matches the input category
            c += i["imdb"]       #condition is met add the imdb score of the movie to c
            d += 1               #the count of movies
    return c/d

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(func_4(movies))

 