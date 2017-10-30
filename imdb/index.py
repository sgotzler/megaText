from imdb import IMDb
<<<<<<< HEAD
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
=======

i = IMDb()
s = i.search_movie('the honeymooners')
m = i.get_movie(s[0].movieID)
i.update(m, ['main'])
print m.movieID, m.get('genres'), m.get('runtimes'), m.get('year'), m.get('distributors'), m.get('seasons')
>>>>>>> 5ac636a427236c7456fd3458bf67283a595632ee
