import sqlite3, time, sys

def login():
    while True:
        username = input("Please enter your username: " )
        password = input("Please enter your password: ")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user, [(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome " + i[2])
                break

        else:
            print("Username and password not recognized")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                break

def newUser():
    foundUser = 0;
    while foundUser == 0:
        username = input("Please enter a username")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser, [(username)])

        if cursor.fetchall():
            print("Username is already taken")
        else:
            foundUser = 1
    firstName = input("Enter your first name")
    surName = input("Enter your surName")
    password1 = input("Please enter a password")
    password2 = input("Please reenter a password")
    while password1 != password2:
        print("Your passwords did not match, please try again.")
        password1 = input("Please enter a password")
        password2 = input("Please reenter a password")

    queryToInsert = """INSERT INTO user(username,firstname,surname,password)VALUES(?,?,?,?)""";
    cursor.execute(queryToInsert, [(username), (firstName), (surName), (password1 )])
    db.commit()



def menu():
    while True:
        print("Welcome to my system")
        menu = ('''
        1 - Create New User
        2 - Login to system
        3 - Exit system\n''')

        userChoice = input(menu)

        if userChoice == "1":
            newUser()
        elif userChoice == "2":
            login()
        elif userChoice == "3":
            sys.exit
        else:
            print("That command is not recognized")

menu()