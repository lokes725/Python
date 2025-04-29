import mysql.connector

def user_login():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='forloop',
            database='eticket'
        )

        cursor = connection.cursor()

        username = input("Enter a username: ")
        pwd = input("Enter password: ")

        # Password aur name dono fetch karo
        query = "SELECT password, name FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result:
            stored_password, name = result
            if stored_password == pwd:
                print(f"Login successful. Welcome, {name}!")
            else:
                print("Incorrect password")
        else:
            print("Username not found")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

user_login()
