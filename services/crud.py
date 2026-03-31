import csv


#Save the information supplied by the user in the form of a dictionary to be saved in the students list

def registerStudent(id, name, age, program, state):
    student = {
        "id" : id,
        "name" : name,
        "age": age,
        "program" : program,
        "state" : state
    }

    return student

#runs through students to be shown
def showStudents(students):
    if not students:
        print("There is not students \n")
    
    for i, student in enumerate(students, start=1):
        print(f"{i} - {student}")


#search for a student based on their ID

def searchStudent(id, students):
    
    found = False
    student_searched = []

    if not students:
        print("There is not students")
    
    for student in students:
        if student["id"] == id:
            student_searched.append(student)
            found = True
    if not found:
        print("studen not fount")

    return student_searched

#Update a student's information based on their ID
def updateStudent(id,students):
     while True:
        try:
            student_update = None

            #When it finds a match, it saves it in the student_update variable to be modified.
            for student in students:
                if student["id"] == id:
                    student_update = student
                    break
        
            if student_update is None:
                print("student not found")
                return
        
            new_age = int(input("Enter the new age: \n"))
            new_program = input("Enter the new program: \n").lower()
            new_state = input("Enter the new state: active or inactive :\n")
                
            
            if new_state not in ["active", "inactive"]:
                    print("the estate must be active or inactive, try again")
                    continue
            
            if new_age < 0:
                    print("the new age cannot be negative, try again")
                    continue
        
        #Modify the information
            student_update["age"] = new_age
            student_update["program"] = new_program
            student_update["state"] = new_state
            
            print("student update successfully \n")
            break
        
        except ValueError:
            print("Value incorrect")
            break


# deletes a student's information based on their id
def deleteStudent(id, students):
    student_delete = None

    #finds the information and stores it in a variable
    for student in students:
        if student["id"] == id:
            student_delete = student
    
    if student_delete is None:
        print("student not found")
        return
    
    #Delete the information with a remove command in the original dictionary list
    else:
        students.remove(student_delete)
        print("student deleted successfully")


#Function that creates the CSV file with the information found in the students dictionary list
def createCSV(path, students):
    with open(path, "w", newline="" ,encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age", "program", "state"])
        writer.writeheader()
        writer.writerows(students)

#Read the CSV information, verifying that everything is saved correctly for use.
def readCSV(path, students):
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = {
                "id" : int(row["id"]),
                "name" : row["name"],
                "age" : int(row["age"]),
                "program" : row["program"],
                "state" : row["state"]
            }
            students.append(student)