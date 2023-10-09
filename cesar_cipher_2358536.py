#PREPARED BY KRITIKA ADHIKARI
#university id : 2358536
#college id : np03cs4s230274

def welcome():
#defining a welcome() function
# this function welcomes the user and tells about the program
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
    
#defining a enter_message() function which takes input from the user and works accordingly
#in this function user are asked for their choice of mode, incase of invalid answer an error is showed using except
#after all the operation are done and the input is taken and evaluated, mode, message and shift are returned
    
    message=input("Would you like to encrypt (e) or decrypt (d): ")
    
    while message!="e" and message!="d":
        print("Error: Choose e or f")
        message=input("Would you like to encrypt (e) or decrypt (d): ")
        
    modechoice= input("Would you like to read from a file (f) or the console (c)? ")
    
    while modechoice!="f" and modechoice!="c":
        print("Invalid Mode")
        modechoice= input("Would you like to read from a file (f) or the console (c)? ")

    else:
        if modechoice=="f":
            filename=input("Enter a filename: ")
            is_file(filename)
            while not is_file(filename):
                    print("Invalid Filename")
                    filename = input("Enter a filename: ")
            new=process_file(filename, message)
            write_messages(new)
            print("Output result is shown in result.txt")

        elif modechoice=="c":
            if message=="e":
                usermsg=(input("What message would you like to encrypt:"))
                upper=str.upper(usermsg)

                while True:
                    try:
                        shift = int(input("What is the shift number: "))
                        break
                    except ValueError:
                        print("Invalid Shift")
                print(f"the result is displayed below")
                print(encrypt(upper, shift))

            elif message=="d":
                usermsg=(input("What message would you like to decrypt:"))
                upper=str.upper(usermsg)

                while True:
                    try:
                        shift = int(input("What is the shift number: "))
                        break
                    except ValueError:
                        print("Invalid Shift")
                print(f"The result is displayed below")
                print(decrypt(upper, shift))
                return filename, usermsg, shift

    return message



#3
#defining function for encrypting
#this isnt running in loop, if the user wants to encrypt a text, the user will have to write encrypt('wordofchoice', shiftnumber)
#this function is used to encrypt text
#the times the albhabets are to be shifted is taken from user then it is calculated accordinly

def encrypt(text, shift):
    result=""
    for i in text:
        if i.isalpha():
            new_char = chr((ord(i) - 65 + shift) % 26 + 65)
            result +=new_char
        else:
            result +=i
    return result



#4
#defining function for decrypting
#this decrypts the given argument
def decrypt(text, shift):
 
    result=""
    for i in text:
        if i.isalpha():
            new_char = chr((ord(i) - 65 - shift) % 26 + 65)
            result +=new_char
        else:
            result +=i
    return result


#1
#function for processing file
#this function takes 2 parameters
#this reads the text in the file
def process_file(filename, message):
    strings = []
    shift_num=input("what is the shift number:")
    shift = int(shift_num)
    with open(filename, "r") as file:
        for text in file:
            if message == "e":
                encrypted= encrypt(text, shift)
                strings.append(encrypted)
            elif message =="f":
                decrypted = decrypt(text, shift)
                strings.append(decrypted)
    return strings


    
#2
#importing os for this function, this checks if a file exist or not
#importing this in order to make code optimized and faster and shorter
import os
def is_file (filename):
    return os.path.isfile(filename)

            
#3
#this function is used to write messages
def write_messages(new):
    with open("results.txt", "w") as file:
        for string in new:
            file.write(string)


#4
#this function is used as per the mode selection of the user
#if the user selects c then the user will be asked to enter the message in the console
#if user selects f then name of the file is asked
#the file is then verified using is_file too
#in case if the file doesnt exist then invalid filename is printed

def message_or_file():

    message= enter_message()
#this function does all of the work of enter_message so instead of making the program long, enter_message() has been called    

    
  #this function is built in a way that it implements all of the functions deined above
      
def main():
    message_or_file()
    while True:
           user_input = input("Would you like to encrypt or decrypt another message? (y/n):")
           if user_input == "y":
               main()
           elif user_input == "n":
                print("Thanks for using the program, goodbye!")
                exit()
    else:
        print("Invalid option, try again!")
         
welcome()
main()


#THE END
#DONE BY : KRITIKA ADHIKARI
        




























