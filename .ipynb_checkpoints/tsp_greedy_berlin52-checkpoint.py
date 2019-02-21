import turtle as t
import math 

def berlin52():
    return [[565,575],[25,185],[345,750],[945,685],[845,655],
    [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
    [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
    [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
    [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
    [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
    [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
    [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
    [830,610],[605,625],[595,360],[1340,725],[1740,245]]

def dist1(i,j):
    '''
    returns: Entfernung zwischen der i-ten und j-ten Stadt
    '''
    x1,y1 = cities[i][0], cities[i][1]
    x2,y2 = cities[j][0], cities[j][1]
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))


def dist(tour):
    '''
    tour: Liste mit einer Anordnung der Städteindizes
    returns: Länge der Tour
    '''
    summe = 0
    for i in range(len(cities)-1):
         summe += dist1(tour[i],tour[i+1])
    return summe + dist1(tour[-1],tour[0])

def nearest(i,iset):
    '''
    iset: set von indizes, aus denen die nächstgelegene Stadt zu cities[i]
        gesucht wird
    '''
    bestIndex = -1
    bestDist = float('inf')
     
    for k in iset:
        if dist1(k,i) < bestDist:
            bestDist = dist1(k,i)
            bestIndex = k

    return bestIndex

def greedy(start=0):
    iset = set(range(len(cities)))
    k = start
    tour = []
    
    while iset:
        tour.append(k)
        iset.remove(k)
        k = nearest(k,iset)
    return tour

def showCities(start = 0, label = False):
    t.tracer(False)
    t.hideturtle()
    for i in range(len(cities)):
        x, y  = cities[i][0], cities[i][1]
        t.penup()
        t.setposition(x,y)
        t.pendown()
        if i == start:
            t.dot(12,'red')
        else:
            t.dot(8,'black')
        if label: t.write(i)
        t.update()

def showTour(tour):
    t.hideturtle()
    t.tracer(True)
    t.speed(2)
    t.penup()
    x0 = cities[tour[0]][0]
    y0 = cities[tour[0]][1]
    t.setposition(x0,y0)
    t.pendown()
    for i in range(1,len(tour)):
        x = cities[tour[i]][0]
        y = cities[tour[i]][1]
        t.goto(x,y)
    t.goto(x0,y0)
    t.up()
    t.goto(50,50)
    t.down()
    t.write(round(dist(tour)))
    
t.setworldcoordinates(0, 0, 1800, 1200)
start = 39
cities = berlin52()
showCities(start)

tour = greedy(start)
showTour(tour)
t.mainloop()

        
        