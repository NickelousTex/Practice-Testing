###Calculator###

##John Teixeira##


#Make the whole thing a function:
def calculator():
#First need to define numbers to be inputed 
    num_1 = float( input('Enter a number: '))
    num_2 = float (input ('Enter a number: '))

# check to verify we got the right thing [Reference for later]

    #print ('{}+ {} = ' .format(num_1 , num_2))
    #print (num_1 + num_2)
    

# Operators for the calculator

    operator = input("What would you like to do?: [+ - x /] ?:  ")

    if operator == "+":
        print (num_1 + num_2)

    elif operator == "-":
        print (num_1 - num_2)

    elif operator == "x":
        print (num_1 * num_2)

    elif operator == "/":
        print (num_1 / num_2)
calculator()

#Need to have more options for input


def again():
    once_more = input ("Do you want to run again?:  ")

    if once_more == "yes" or "y" or "Y" or "Yes" or "YES":
        calculator()
    elif once_more == "no" or 'n' or 'No' or "N" or "NO":
        print ("Cool see you later!")
    else:
        again() 
again()    
        





               
