oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# solution a
oscar_winners.add("Emma Watson")
print(oscar_winners)
# solution b
clon_oscar_winners = oscar_winners.copy()
clon_oscar_winners.remove('Meryl Streep')
clon_oscar_winners.clear()
print(clon_oscar_winners)

# solution c
if 0 == len(titanic_actors & dark_knight_actors):
    print(" There is no common actors")
else:
    print(titanic_actors & dark_knight_actors)#titanic_actors.intersection(dark_knight_actors)

# solution d
print(iron_man_actors)
print(len(iron_man_actors))
print(avengers_actors)
print(len(avengers_actors))
if 0 == len(iron_man_actors & avengers_actors):
    print(" There is no common actors")
else:
    print(iron_man_actors & avengers_actors)#iron_man_actors.intersection(avengers_actors)

# solution e
if actor_list.issubset(oscar_winners):
    print(" Yes they all win in oscar")
else:
    print(" Not all they actors are win in oscar")

# solution f
if actor_list.issuperset(avengers_actors):
    print(" Yes actor list contain all avengers actors")
else:
    print(" No actor list are not contain all avengers actors")

# solution g
if len(movie_cast) != 0:# set not empty
    actor = movie_cast.pop()
    print(f" movie_cast after removing {actor} :")

# solution h
if len(movie_cast) != 0:# set not empty
    movie_cast.remove('Matt Damon')
    print(f" movie_cast after removing Matt Damon {movie_cast}:")

# solution i
print(f" Actor which no win in oscar: {titanic_actors - oscar_winners}")
# titanic_actors.difference(oscar_winners)

# solution j
print(f" The actor which play in only one movie: {titanic_actors ^ dark_knight_actors}")
# titanic_actors.symmetric_difference(dark_knight_actors)

# solution k
oscar_winners |= {'Cate Blanchett', 'Daniel Day-Lewis'}


# solution l
titanic_actors |= dark_knight_actors
print(titanic_actors)



