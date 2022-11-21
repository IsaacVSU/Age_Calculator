#Imports the function from the tkinter GUI and Datetime
import tkinter as tk
from tkinter import * 
from tkinter.messagebox import showinfo
import datetime
from datetime import datetime


dt = datetime.now() #GET CURRENT DATE, HOUR<(military), minutes, seconds, and miniseconds now

App = Tk()
App.geometry('400x400') #Creating the GUI 
App.title('Age Calculator App')
NameLabels = Label(App, text = 'Welcome to the Age Calculator!',bg='Aqua').place(x=105, y=10)
App.configure(bg='Orange')
NameLabel = Label(App,text = 'Enter your Date of Birth',bg='Aqua').place(x=70,y=50)

#String entered Label
Dayv = tk.StringVar()
Monthv = tk.StringVar()
Yearv = tk.StringVar()

#Creating the labels for the widgets for Month, Year, and day.
Day = tk.Label(text = 'Day *Enter as DD', bg='Aqua',width=18)
Day.place(x=20,y=85)
Month = tk.Label(text = 'Month *Enter as MM',bg='Aqua',width=18)
Month.place(x=20,y=115)
Year = tk.Label(text='Year *Enter as YYYY',bg='Aqua',width=18)
Year.place(x=20,y=145)

#Entry for the user to input the information
Day1 = Entry(App, textvariable=Dayv).place(x=180,y=85)
Day2= Entry(App, textvariable=Monthv).place(x=180,y=115)
Day3=Entry(App, textvariable=Yearv).place(x=180,y=145)

#Check function for if it is a leap yr
def is_leapyr(x):
    if(x%400==0 and x%100==0):
        return True
    elif(x%4==0 and x % 100 !=0):
        return True
    else:
        return False

#Dictionary for amount of days in a month:
YearM = {
    1: 31, 
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

#HELPER FUNCTIONS
def var():
    x1Str = Dayv.get() #Saves Birth-DAY as string
    x2Str = Monthv.get() # Saves Birth-Month as a string
    x3Str = Yearv.get() #Saves Birth-Year as a string
    return (x1Str + x2Str + x3Str) #return statement DD MM YYYY 

def Yrage(d, m, y):
    age = dt.year - y #Age if bday already happened in the year
    if(dt.month<m):
        age-=1
    elif(dt.month==m and dt.day<d): #checks if the day happened or not in a month
        age-=1
    return age

def horo(d,m):
    #Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn,Aquarius, pisces, 
    if((m==3 and d>=21) or (m==4 and d<=19)):
        return "♈Aries♈"
    if((m==4 and d>=20)or(m==5 and d<=20)):
        return "♉Taurus♉"
    if((m==5 and d>=21) or(m==6 and d<=20)):
        return "♊Gemini♊"
    if((m==6 and d>=21) or (m==7 and d<=22)):
        return "♋Cancer♋"
    if((m==7 and d>=23) or(m==8 and d<=22)):
        return "♌Leo♌"
    if((m==8 and d>=23) or (m==9 and d<=22)):
        return "♍Virgo♍"
    if((m==9 and d>=23) or (m==10 and d<=22)):
        return "♎Libra♎"
    if((m==10 and d>=23) or (m==11 and d<=21)):
        return "♏Scorpio♏"
    if((m==11 and d>=22) or (m==12 and d<=21)):
        return "♐Sagittarius♐"
    if((m==12 and d>=22) or (m==1 and d<=19)):
        return "♑Capricorn♑"
    if((m==1 and d>=20) or (m==2 and d<=18)):
        return "♒Aquirius♒"
    if((m==2 and d>=19) or(m==3 and d>=20)):
        return "♓Pisces♓"

def daysAlive(d, m,y):
    days_A = (dt.year-y) * 365
    x1 = 0
    count=0
    sum = 0
    for xxxx in range(y, dt.year): #checks for leap year
        if(is_leapyr(xxxx)):
            count+=1
    if(dt.month==m):
            x1 = d-dt.day #get the amount of days and subtract it from days alive
            if(dt.day==d):
                print("HAPPY B-DAY")
    elif(dt.month<m): #b-day didn't happen yet this year
        x1 = YearM[dt.month]- dt.day + d 
        if(dt.month+1!=m): #Add all days between the two months and subtract them.
            for i in range(dt.month+1, m):
                x1 += YearM[i]
    elif(dt.month>m): #checks if bday happened already
        sum = dt.day
        if(is_leapyr(dt.year) and 2<dt.month): #check if february happened already if leep year
            sum+=1
        sum += YearM[m]-d
        for i in range(m+1, dt.month):
            sum += YearM[i] 
    days_A = days_A + count + sum - x1 #Formula daysAlive = (current year - birthYr) * 365 + (#LeapYrs-365) + or - totalDays
    return days_A

def hrAlive(p1):
    hr_A = ((p1 * 24) + dt.hour) #days * (hrs per day) + todays hours
    return hr_A
 
def minAlive(p2):
    min_A = ((p2*60) + dt.minute) #hours * (minutes per hour) + minutes now
    return min_A

def secAlive(p3):
    sec_A = ((p3*60)+dt.second)
    return sec_A

def msAlive(p4):
    ms_A = ((p4*1000)+(dt.microsecond* 10**-3))
    return ms_A

#Pressing CALCULATE button
def calculate():
    str1 = var()
    if(str1[0]=='0'): #Remove '0' from DD ex: 02
        day = str1[1:2]
    else:
        day = str1[0:2]
    dayInt = int(day) #Gives me an int days
    if(str1[2]=='0'): #Same thing for months(remove '0')
        month = str1[3:4]
    else:
        month = str1[2:4]
    monthInt = int(month) #Gives me int months
    yearInt = int(str1[4:]) #Gives me the int year
    Horoscope = horo(dayInt, monthInt)
    Age = Yrage(dayInt, monthInt, yearInt) 
    DayA = daysAlive(dayInt,monthInt, yearInt) #Days alive
    hrA = hrAlive(DayA) #hours alive
    minA = minAlive(hrA) #minutes alive
    secA = secAlive(minA) # seconds alive
    msA = msAlive(secA)
    msg = f"Horoscope: {Horoscope}\nYears Old: {Age}\nDays Alive: {DayA:,}\nHours Alive: {hrA:,}\nMinutes Alive: {minA:,}\nSeconds Alive: {secA:,}\nMiliseconds Alive: {msA:,}" 
    showinfo("Age calcs:", msg)

cal_button=Button(App,
    text="Calculate",
    width=17,
    height=2,
    bg="Aqua",
    fg="Black",
    command=calculate
 ).place(x=70,y=185)


App.mainloop()
