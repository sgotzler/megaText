from imdb import IMDb

i = IMDb()
s = i.search_movie('the honeymooners')
m = i.get_movie(s[0].movieID)
i.update(m, ['main'])
print m.movieID, m.get('genres'), m.get('runtimes'), m.get('year'), m.get('distributors'), m.get('seasons')
