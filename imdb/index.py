from imdb import IMDb
ia = IMDb()

movie = ia.get_movie('0044229')
print "Name of the movie: ", movie
for i in movie['cast']:
    print "Cast: ", i
    writer = ia.search_person(i['name'])[0]
    ia.update(writer)
    print "Movies cast %s:" % writer
    try:
        for movie_name in writer['aka']:
            print movie_name
    except Exception as error:
        print error
