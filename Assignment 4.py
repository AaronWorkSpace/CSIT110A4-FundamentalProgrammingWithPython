#Done by: Aaron Lim
#Mod: CSIT110
#student ID (UOW): 5985171
#Date: 16/11/2018 (DD/MM/YYYY)

import os.path

#For menu
#Check if user enter 1/2/3 before returning choice
#check if file exist
#check if user want to open another file

#For option 1
#Check if user enter ! to exit
#Check special symbol except !
#Check if user actually input something into first name
#Check if user actually input something into last name
#Check if user don't enter numeric number in the name (The first name and last name cannot consist of numbers)

#Using assignment 3 function, checking if it is SDDDDDDDL
#S represents the letter S
#N represents an integer
#L represents a letter (B to L)
#check if string length is 9
#checking if first letter is S
#check last letter is letter from B to L
#checking if all letters are numeric, if not return false, if it is + 1 to i

#Using assignment 3 function, checking if the student id letter is valid
#checking if div and last letter matches

#Checking if student id is already register

#for option 2
#Check if user enter ! to exit
#check if the list is already emptied
#check if user want to exit deletion page
#Checking if student is inside the list

#for option 3
#just write no need check

import csv

def menu():
    #Check if user enter 1/2/3 before returning choice
    #else it will keep looping
    ok = True
    while(ok == True):
        print('Student Records Management System')
        print('1. Insert a new student')
        print('2. Delete a student')
        print('3. Save data to file and exit')
        choice = input('Enter choice: ')
        if(choice == '1' or choice == '2' or choice == '3'):
            print()
            return choice
        else:
            print('----------------------------------------')
            print('Invalid input, please enter 1 or 2 or 3.')
            print('----------------------------------------')

def isValidStudentIDFormat(studID):
    #variable to check on second checking
    lastLetter = 'BCDEFGHIJKL'
    #check if string length is 9
    #if not return false
    if(len(studID) == 9):
        #Convert 1st and last letter to capital letters
        firstL = studID[0]
        lastL = studID[8]
        #checking if first letter is S
        #if not return false
        if(firstL == 'S'):
            #check last letter is letter from B to L
            #if not return false
            if lastL in lastLetter:
                #checking if all letters are numeric, if not return false, if it is + 1 to i
                if(studID[1:8].isnumeric()):
                    return True, ''
                else:
                    #Not every values between 1st and last alphabets are digits.
                    return False, "Not every value inbetween 1st and last alphabet are digits"
            else:
                #Invalid letter(s)
                return False, "Invalid last letter (Not between B and L)"
        else:
            return False, "The first letter is not S"
    else:
        #Length is not 9
        return False, "Length is not 9"

def isValidStudentIDLetter(studID):   
    multiply = 0
    lastLetter = "BCDEFGHIJKL"
    #adding all multiplication into 1 variable, multiply
    multiply += int(studID[1]) * 2    
    i = 2
    j = 7
    while(i <= 7):
        multiply += int(studID[i]) * j
        j -= 1
        i += 1
    #div is a variable to check get the remainder of % 11
    div = multiply % 11
    #variable for last letter (extraction)
    lastL = studID[8].upper()
    #checking if div and last letter matches
    if ((div == 0 and lastL == "B") or
        (div == 1 and lastL == "C") or
        (div == 2 and lastL == "D") or
        (div == 3 and lastL == "E") or
        (div == 4 and lastL == "F") or
        (div == 5 and lastL == "G") or
        (div == 6 and lastL == "H") or
        (div == 7 and lastL == "I") or
        (div == 8 and lastL == "J") or
        (div == 9 and lastL == "K") or
        (div == 10 and lastL == "L")):
        return True, ""
    else:
         #is invalid as the last letter should be the letter above
        return False, "The last letter is invalid as the last letter should be {0}".format(lastLetter[div])   

def checkNum(name):
    i = 0
    while(i < len(name)):
        if(name[i].isnumeric()):
            return False
        i += 1
    else:
        return True

def checkSym(name):
    #symbol to check
    symbols = '~`!@#$%^&*()_-+={[}]:;"<,>.?/'
    symbol = "'"    
    for characters in name:
        for sym in symbols:
            if(sym == characters):
                return False
            if(characters == symbol):   
                return False
    return True

def checkSpace(name):
    #check space
    for characters in name:
        if(characters == ' '):
            return False
    return True

def option1(count, studFName, studLName, studentID):
    #Inserting student into the list
    #Check if user actually input something into first name
    #else it will keep looping
    #Check if user enter ! to exit
    print('Insert a new student')
    
    ok = False
    while(ok == False):
        print('Please input the data accordingly, name without space / numbers / symbols except !')
        print('Enter ! if you want to exit')
        fName = input('Enter first name: ')
        if(fName == '!'):
            print('-'*31) 
            return count, studFName, studLName, studentID
        if not fName.isalpha():
            noSpace = checkSpace(fName)
            if(noSpace == False):
                print()
                print('Please refrain from using blank')
                print('-'*31) 
            else:
                #Check if there is symbol in the name
                noSymbol = checkSym(fName)
                if(noSymbol == False):
                    print()
                    print('Please refrain from using symbol')
                    print('-'*31) 
                else:
                    #Check if there is number in the name
                    noNum = checkNum(fName)
                    if(noNum == False):
                        print()
                        print('Please refrain from using numbers in name')
                        print('-'*31) 
                        ok = False            
        else:
            ok = True
            print('-'*31) 

    ok = False
    #Check if user actually input something into last name
    #else it will keep looping    
    while(ok == False):
        print('Please input the data accordingly, name without space / numbers / symbols except !')
        print('Enter ! if you want to exit')
        lName = input('Enter last name: ')
        if(lName == '!'):
            print('-'*31) 
            return count, studFName, studLName, studentID
        if not lName.isalpha():
            noSpace = checkSpace(lName)
            if(noSpace == False):
                print()
                print('Please refrain from using blank')
                print('-'*31) 
            else:
                #Check if there is symbol in the name
                noSymbol = checkSym(lName)
                if(noSymbol == False):
                    print()
                    print('Please refrain from using symbol')
                    print('-'*31) 
                else:
                    #Check if there is number in the name
                    noNum = checkNum(lName)
                    if(noNum == False):
                        print()
                        print('Please refrain from using numbers in name')
                        print('-'*31) 
                        ok = False            
        else:
            ok = True
            print('-'*31) 
    #it will keep looping as long as ok is false
    ok = False
    while(ok == False):
        print('Please input the data accordingly, SDDDDDDDL')
        print('"S" represent "S" for first letter')
        print('"D" represent digits')
        print('"L" represent letter from "B" to "L"')
        print()
        print('Enter ! if you want to exit')      
        studID = input('Enter student ID: ')
        if(studID == '!'):
            print('-'*31) 
            return count, studFName, studLName, studentID  
        #Converting all letters to uppercase
        studID = studID.upper()
        #Using assignment 3 function, checking if it is SDDDDDDDS
        ok, message = isValidStudentIDFormat(studID)
        if(ok == True):
            #Using assignment 3 function, checking if the student id letter is valid
            ok, message = isValidStudentIDLetter(studID)
            #Checking if student id is already register
            for studentid in studentID:
                if(studentid == studID):
                    ok = False
                    message = 'Student ID had been used'
        #if either not SDDDDDDDS or invalid last letter or used student ID
        #The loop will re-run again
        if(ok == False):
            print()
            print(message)
            print('Please try again')
            print('-'*31) 
    #Once it is true, it exit the loop
    #append first name, last name, student id to individual list
    studFName.append(fName)
    studLName.append(lName)
    studentID.append(studID)
    #count is increased by 1
    count += 1
    print()
    print('New Student Record Inserted')
    print('-'*31) 
    #returning count and all list
    return count, studFName, studLName, studentID

def option2(count, studFName, studLName, studentID):
    while(True):
        ok = True
        #Deleting student from the list
        #check if user want to exit deletion page
        if(len(studentID) == 0):
            print('There is no student ID, please insert before deleting, will be returning to main page')
            print('-'*31)  
            return count, studFName, studLName, studentID  
        print('List of students')
        #providing the user with student ID
        print('{0:<15}{1:<15}{2:<15}'.format('First name', 'Last name', 'Student ID'))
        j = 0
        for student in studentID:
            print('{0:<15}{1:<15}{2:<15}'.format(studFName[j], studLName[j], student))
            j += 1              
        print()
        print('Delete a student')
        studID = input('Enter student id to delete or ! to exit: ')
        if(studID == '!'):
            print('-'*31) 
            return count, studFName, studLName, studentID 
        i = 0
        #converting all letters from student id to uppercase
        studID = studID.upper()
        #using a for loop to go through student id one by one
        #Checking if student is inside the list
        for studentid in studentID:
            #if student id is studID, it will break
            #uses i as counter
            if(studentid == studID):
                ok = True
                break
            i += 1
        #It did not enter break, ok is false (student id is not found)
        else:
            ok = False
        #Checking if student id is not found, ok is false
        #if found, it will return the count and lists straightaway
        if(ok == False):
            print()
            print('Student id not found. Here are the ID(s)')
            print('-'*31)  
        else:
            #If found, ok is true, it will delete the student first name, last name, student id
            #by using the counter
            del studFName[i]
            del studLName[i]
            del studentID[i]
            #count is decreased by 1
            count -= 1
            print()
            print('Student Record Deleted')
            print('-'*31)     
            return count, studFName, studLName, studentID 
    
def writeData(count, studFName, studLName, studentID, filePath):
    #Writing the data, code provided in assignment 4 sheet  
    with open(filePath, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'student_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #Counter for list
        i = 0
        #Comparing counter with number of students
        while(i < count):
            #writing each cell with first_name/last_name/student_id
            #with list information
            writer.writerow({'first_name': studFName[i], 
                             'last_name': studLName[i], 
                             'student_id': studentID[i]})
            #Increment counter by 1 every time 1 is written
            i += 1
    
    print('Data file saved')   
    print('-'*31) 
    
def userChoice():
    fileOk = True
    while(fileOk is True):
        #user input which file they want to use
        while True:
            filePath = input('Please enter file name or ! to exit: ')
            #check if file exist
            if(os.path.isfile(filePath)):
                ok = True
                print('-'*31) 
                break
            elif(filePath == '!'):
                ok = False
                fileOk = False
                print('-'*31) 
                print('Thank you for using Students Records Management System')  
                break
            else:
                print('There is no such file')
                print('-'*31) 
        #lists for individual first name, last name and student ID
        studFName = []
        studLName = []
        studentID = []     
        #for counting the number students
        count = 0
        #Code provided in assignment 4, reading the csv and appending to the list accordingly
        #Increment count by 1 every single time it run through the loop
        #Assuming all student ID from the file is valid
        if(ok == True):
            with open(filePath) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    studFName.append(row['first_name'])
                    studLName.append(row['last_name'])
                    studentID.append(row['student_id'])
                    count += 1
        
        #checking which choice user input, false and will exit the loop and terminate the program
        while(ok == True):
            choice = menu()
            if(choice == '1'):
                count, studFName, studLName, studentID = option1(count, studFName, studLName, studentID)
            elif(choice == '2'):
                count, studFName, studLName, studentID = option2(count, studFName, studLName, studentID)
            else:
                writeData(count, studFName, studLName, studentID, filePath)
                ok = False
        while(fileOk == True):
            user = input('Open another file(y/n): ')
            user = user.lower()
            if(user == 'y'):
                print('-'*31) 
                fileOk = True
                break
            elif(user == 'n'):
                fileOk = False
                print('-'*31) 
                print('Thank you for using Students Records Management System')
            else:
                print('-'*31) 
                print('Invalid input, please enter y or n')

userChoice()
