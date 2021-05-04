def organizer(**people):
    isim = []
    yaş = []
    for x, y in people.items():
        isim.append(people.keys())
        yaş.append(people.values())
        print( x, "yaşı" , y)
organizer(ayşe = 35, ahmet = 28, hatçe = 40, yusuf = 12)