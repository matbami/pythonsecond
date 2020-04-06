import random
import string


# random string generator function
def randomStringwithDigitsAndSymbols(stringLength):

    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(password_characters) for i in range(stringLength))

finaloutput = []

#counter to know number of users
i = 1

#main program function
def program():

    firstname = input('Please enter your Firstname: ')
    lastname = input('Please enter your Lastname: ')
    email = input('Please enter a valid email: ')


    w =(firstname[0:2])

    s =(lastname[-2:len(lastname)])
    
    #concatenate firstname and lastname with random string
    randompassword = w+s+randomStringwithDigitsAndSymbols(5)
    print('YOUR PASSWORD IS ==> ' +randompassword)

    question = input('Do you like password? (Y/N) ').lower()
    


    #if user doesnt input required text, keep asking question
    while(question!='n' and question!='y' ):
        question = input('Do you like password?(Y/N) ').lower()
      

    if(question=='n'):
        newpassword= input('Enter new password? ')
        while(len(newpassword)<=7):
            print('Error! please provide password greater than 7 characters')
            newpassword= input('Enter new password? ')  
        finalpassword = newpassword
    if(question=='y'):
        finalpassword = randompassword


    
    #print final output
    finaloutput.append('user'+str(i)+'==> {Firstname:' + firstname+ ', Lastname:' + lastname+ ', Email:' + email + ', Password:' + finalpassword+'}') 



print('REGISTER YOUR USERS ===>> TYPE "y" for YES or "n" for NO' )

user = input('ENTER A USER? (Y/N) ').lower()



while(user == 'y'):

    program()
    
    i+=1
    user = input('ENTER ANOTHER USER? (Y/N) ').lower()
 


print(finaloutput)





