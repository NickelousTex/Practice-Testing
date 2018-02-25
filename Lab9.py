### Lab 9 ###
## Teixeira ##



## Question 1 ##
print (" Maximum of numbers: \n ")
       
def num():  
    num1 = 1
    num2 = 3
    num3 = 5
    
def maximum():
    num()
    if (num1 > num2) and (num1 > num3) :
       print "The largest number is: ", num1 
    elif (num2 > num1) and (num2 > num3) :
            print "The largest number is: ", num2 
    elif (num3 > num1) and (num3 > num2) :
            print "The largest number is: ", num3 

#maximum()


##Question 2 ##
print ("\n \n Estimate your paycheck: \n")
def paycheck():
     hours = int (input("Enter the hours you worked: "))
     pay = int (input("Enter your hourly pay: :"))
     payrate = pay * hours
     

def totalpay(person):
    paycheck()
    print (person +" your total pay for the week is :" + payrate)

#name = str (input ("Enter your name: "))

#totalpay (name) 



## Question 3 ##
print ("\n \n Find the hypotonus of a triangle: \n ")
def triangle():
    a = input ("Enter one side of the triangle: ")
    b = input ("Enter the othe side of the triangle: ")

def formula():
    c2 = (a * a) + (b * b)
    hypot = c2 **(.5)

def tell():
    print (hypot)

## Question 4 ##
print (" \n \n Distance converstion: \n")
def distance():
    distance = input ("Enter a distance in meters: ")
distance()
def kilo():
    kilo = distance *0.001
    
def inches():
    inches = distance * 39.37

def feet():
    feet = distance * 3.281

while choice:
    print ("""
1. Convert to Kilometeres \t
2. Convert to inchese \t
3. Convert to feet \t
4. ReEnter distance \t
5. Exit""")
    choice = input ("Enter your choice: ")
    if choice == "1":
       print ("Kilometers: ", kilo)
    elif choice == "2":
        print ("inches: ",  inches)
    elif choice == "3":
        print ("feet: ", feet)
    elif choice == "4":
        distance()
    elif choice == "5":
        print ("Goodbye")
        exit 
    elif choice !="":
        print ("Not a valid entry, please type a number 1 thru 5")
    




## Question 5 ##
print ("\n \n \n Let's determin your BMI: \n")
def BMI():
    weight = input ("Enter your weight in pounds :")
    height = input ("Enter your height in inches :")

    BMI = (weight*703) / (height**2)

    if BMI > 25 :
        print ("You are considered overweight")
    elif BMI < 18.5 :
        print ("You are considered underweight")
    else:
        print ("You weight is considered optimal")
BMI()

    
