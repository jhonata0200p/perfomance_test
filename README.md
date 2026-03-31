# Student Management System with Data Persistence

This project allows you to perform CRUD operations, first saving them in a dictionary list, then saving them to a CSV file for later use.

## Structure

-main.py: main file to run the entire program
-services/: Folder to store the CRUD, the options menu, and other services
-crud.py: file that contains all the CRUD operations
-options.py: file that contains a list that is used for the options menu
-services.py: This file can store different services; in this case, it contains the menu function.
-data/: folder to store the CSV file

##Requirements
- Python 3.x

##Use
Run the main.py file to start the program:

```bash
python main.py
```

Follow the on-screen instructions to manage your records.


## Explanation of important instructions

###with open(path, "r", newline="", encoding="utf-8") as f:
It is used to read the contents of the CSV file before starting the program, allowing for easier manipulation of the information.

###path = os.path.join(folder, "data.csv")
It's used to combine the folder name with the file name; it's very useful for ensuring the path is spelled correctly regardless of the operating system where it's run.

###def getOption (options):
That's the function of the menu, very useful because it's scalable.

###with open(path, "w", newline="" ,encoding="utf-8") as f:
It is used to create the CSV file with the updated information, so that it can be read later and always be available.

### File CSV
It's a file that allows us to save information in a way very similar to Excel.

###visual example

- **CSV:**
  | id  | name   | age  | program |  status |
  |-----|--------|------| --------|---------|
  | 1111| Jhona  | 23   |  react  | active  |


  #Autor

  Jhonatan Miranda


