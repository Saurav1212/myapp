import csv

global f,x
f=0
x=0

def city():
    global ci
    print("BOOKING TICKET MANAGEMENT")
    print("Welcome! Book your tickets here")
    print("Choose your city:-")
    print("1-Anand")
    print("2-Vadodara")
    print("3-Ahmedabad")
    place=int(input("Choose your city(1,2,3)"))
    if place==1:
        ci="Anand"
        theatre()
    elif place==2:
        ci="Vadodara"
        theatre()
    elif place==3:
        ci="Ahmedabad"
        theatre()
    else:
        print("Wrong Choice!")


def theatre():
    global f
    f=f+1
    print("Choose Cinema:-")
    print("1-Inox")
    print("2-PVR Cinemas")
    print("3-Gold Cinema")
    print("4-R&S Cinema:-")
    print("5-back")
    a=int(input("Choose Cinema(1,2,3,4,5)"))
    movie(a)
    return 0


def movie(theatre):
    global te
    if theatre==1:
        te="Inox"
        t_movie()
    elif theatre==2:
        te="PVR Cinemas"
        t_movie()
    elif theatre==3:
        te="Gold Cinema"
        t_movie()
    elif theatre==4:
        te="R&S Cinema"
        t_movie()
    elif theatre==5:
        city()
    else:
        print("Wrong Choice!")


def t_movie():
    global mov
    print("Choose Movie:-")
    print("1-Bahubali-The Conclusion")
    print("2-Fast and Furious 8")
    print("3-Avengers Endgame")
    print("4-Bhoot")
    print("5-back")
    movie=int(input("Choose your movie(1,2,3,4,5)"))
    if movie==1:
        mov="Bahubali-The Conclusion"
        screen()
    elif movie==2:
        mov="Fast and Furious 8"
        screen()
    elif movie==3:
        mov="Avengers Endgame"
        screen()
    elif movie==4:
        mov="Bhoot"
        screen()
    elif movie==5:
        theatre()
        return 0


def screen():
    global sc
    global ticket
    print("Choose Screen:-")
    print("1-Screen 1(SILVER)")
    print("2-Screen 2(GOLD)")
    print("3-Screen 3(PLATINUM)")
    print("4-Screen 4(CROWN)")
    a=int(input("Choose your screen(1,2,3,4)"))
    ticket=int(input("Number the tickets you want:"))
    sc=a
    timing(a)


def timing(a):
    time1={"1":"10:00 a.m.--1:15 p.m.",
           "2":"1:30 p.m.--4:45 p.m.",
           "3":"5:00 p.m.--8:15 p.m.",
           "4":"8:30 p.m.--11:45 p.m."}

    time2={"1": "9:00 a.m.--12:15 p.m.",
           "2":"12:30 p.m.--3:45 p.m.",
           "3":"6:00 p.m.--9:15 p.m.",
           "4":"9:30 p.m.--12:45 a.m."}

    time3={"1":"12:00 p.m.--3:15 p.m.",
           "2":"3:30 p.m.--6:45 p.m.",
           "3":"7:00 p.m.--10:15 p.m.",
           "4":"10:30 p.m.--1:45 a.m."}

    time4={"1":"10:00 a.m.--1:15 p.m.",
           "2":"1:30 p.m.--4:45 p.m.",
           "3":"5:00 p.m.--8:15 p.m.",
           "4":"8:30 p.m.--11:45 p.m."}
    if a==1:
        global x
        print("Choose your time:-")
        print(time1)
        t=input("Select your time(1,2,3,4)")
        x=time1[t]
        print("Successfull!enjoy movie at:-"+ x)
    elif a==2:
        print("Choose your time:-")
        print(time1)
        t = input("Select your time(1,2,3,4)")
        x = time2[t]
        print("Successfull!enjoy movie at:-" + x)
    elif a==3:
        print("Choose your time:-")
        print(time1)
        t = input("Select your time(1,2,3,4)")
        x = time3[t]
        print("Successfull!enjoy movie at:-" + x)
    elif a==4:
        print("Choose your time:-")
        print(time1)
        t = input("Select your time(1,2,3,4)")
        x = time4[t]
        print("Successfull!enjoy movie at:-" + x)
    return 0


city()
name=input("Enter your name:")
with open(name+'.csv','w')as csvfile:
    wrt=csv.writer(csvfile)
    wrt.writerow(["city : "+ci,"\n","theatre : "+te,"\n","movie : "+mov,"\n","screen : "+str(sc),"\n","time : "+str(x),"\n","Number of tickets : "+str(ticket)])
print("Number of ticket",ticket)
