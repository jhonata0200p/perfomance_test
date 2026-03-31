from services.services import getOption
from services.crud import registerStudent, showStudents, searchStudent, updateStudent, deleteStudent, createCSV, readCSV
from services.options import options
import os
 
 #folder name and path of file
folder = "data"
path = os.path.join(folder, "data.csv")
students = []

#Upload the CSV file and save the information in the students dictionary list
readCSV(path, students)



#Interactive menu

if __name__ == "__main__":

    while True:

        option =  getOption(options)

        if option == 1:
            
            try:  
                while True:
                    id = int(input("Enter your number of C.C or T.I \n"))
                    name = input("Enter your name \n").lower()
                    age = int(input("Enter you age \n"))
                    program = input("Enter the program you belong to: \n")
                    state = input("Enter the state of student: active or inactive\n")


                    if state not in ["active", "inactive"]:
                        print("the estate must be active or inactive, try again")
                        continue

                    if id < 0 or age < 0:
                        print("The values cannot be negative")
            
                #Call the registerStudent function after validating the data
                    student = registerStudent(id, name, age, program, state)
                    students.append(student)
                    print("student add successfully!")
                    break

            except ValueError:
                print("Value incorrect")

        
        elif option == 2:
            showStudents(students)

        elif option == 3:
            try:
                id = int(input("Enter id of the student you wish to found \n"))

                negative = True
                if id < 0:
                    print("the id cannot be negative")
                    negative = False


                #Call the searchStudent function after validating the data
                if negative:
                    student_found = searchStudent(id, students)
                    print(student_found)
            
            except ValueError:
                print("value incorrect")

        
        elif option == 4:
            try:
                id = int(input("Enter id of the student you wish to found \n"))

                negative = True
                if id < 0:
                    print("id cannot be negative")
                    negative = False

                #Call the updateStudent function after validating the data
                if negative:
                    updateStudent(id,students)

            except ValueError:
                print("value incorrect")

        elif option == 5:
            try:
                id = int(input("Enter id of the student you wish to delete \n"))

                negative = True
                if id < 0:
                    print("the id cannot be negative")
                    negative = False
                #Call the deleteStudent function after validating the data
                if negative:
                    deleteStudent(id, students)
            
            except ValueError:
                print("value incorrect")        
            
        elif option == 6:
            #Save the information in a CSV file
            createCSV(path, students)


        elif option == 7:
            print("good bye!")
            break