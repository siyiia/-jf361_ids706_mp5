import os
import sqlite3


# Function to connect to the database
def connect_db(db_name="student.db"):
    conn = sqlite3.connect(db_name)
    print(f"Connected to {db_name}")
    return conn


# Function to create a table (Create operation)
def create_table(conn):
    try:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS students
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      major TEXT NOT NULL);"""
        )
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


# Function to insert data into the table (Create operation)
def insert_student(conn, name, age, major):
    try:
        conn.execute(
            "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
            (name, age, major),
        )
        conn.commit()
        print("Record inserted successfully")
    except sqlite3.Error as e:
        print(f"Error inserting record: {e}")


# Function to read data from the table (Read operation)
def fetch_students(conn):
    cursor = conn.execute("SELECT * FROM students")
    print("ID | Name | Age | Major")
    for row in cursor:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


# Function to update a record (Update operation)
def update_student_age(conn, student_id, new_age):
    try:
        conn.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
        conn.commit()
        print(f"Updated {student_id} student's age to {new_age}")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")


# Function to update a record (Update operation)
def update_student_major(conn, student_id, new_major):
    try:
        conn.execute(
            "UPDATE students SET major = ? WHERE id = ?", (new_major, student_id)
        )
        conn.commit()
        print(f"Updated {student_id} student's major to {new_major}")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")


# Function to delete a record (Delete operation)
def delete_student(conn, student_id):
    try:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print(f"Deleted student with ID {student_id}")
    except sqlite3.Error as e:
        print(f"Error deleting record: {e}")


# Count number of students
def count_students(conn):
    cursor = conn.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    print(f"Total number of students: {count}")


# Get students above a certain age
def get_students_above_age(conn, age):
    cursor = conn.execute("SELECT * FROM students WHERE age > ?", (age,))
    print(f"Students older than {age}:")
    for row in cursor:
        print(f"{row[0]} | {row[1]} | {row[2]}")


def main():
    db_name = "student.db"
    if os.path.exists(db_name):
        os.remove(db_name)

    conn = connect_db(db_name)
    create_table(conn)

    insert_student(conn, "Alice", 22, "MIDS")
    insert_student(conn, "Bob", 21, "ECE")
    insert_student(conn, "Charlie", 25, "BME")

    fetch_students(conn)

    update_student_age(conn, 1, 23)
    update_student_major(conn, 2, "CS")
    fetch_students(conn)

    delete_student(conn, 2)
    fetch_students(conn)

    count_students(conn)
    get_students_above_age(conn, 22)

    conn.close()


if __name__ == "__main__":
    main()
