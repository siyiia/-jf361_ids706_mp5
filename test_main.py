import os
import pytest
from main import (
    connect_db,
    create_table,
    insert_student,
    update_student_age,
    update_student_major,
    delete_student,
)


@pytest.fixture
def setup_db():
    db_name = "test_student.db"
    if os.path.exists(db_name):
        os.remove(db_name)
    conn = connect_db(db_name)
    create_table(conn)
    yield conn
    conn.close()
    if os.path.exists(db_name):
        os.remove(db_name)


def test_database_connection():
    conn = connect_db("test_student.db")
    assert conn is not None
    conn.close()


def test_create_table(setup_db):
    conn = setup_db
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='students';"
    )
    table_exists = cursor.fetchone()
    assert table_exists is not None


def test_insert_student(setup_db):
    conn = setup_db
    insert_student(conn, "Test Student", 20, "Test Major")
    cursor = conn.execute("SELECT * FROM students WHERE name='Test Student'")
    student = cursor.fetchone()
    assert student[1] == "Test Student"
    assert student[2] == 20
    assert student[3] == "Test Major"


def test_update_student_age(setup_db):
    conn = setup_db
    insert_student(conn, "Test Student", 20, "Test Major")
    update_student_age(conn, 1, 21)
    cursor = conn.execute("SELECT age FROM students WHERE id=1")
    updated_age = cursor.fetchone()[0]
    assert updated_age == 21


def test_update_student_major(setup_db):
    conn = setup_db
    insert_student(conn, "Test Student", 20, "Test Major")
    update_student_major(conn, 1, "New Major")
    cursor = conn.execute("SELECT major FROM students WHERE id=1")
    updated_major = cursor.fetchone()[0]
    assert updated_major == "New Major"


def test_delete_student(setup_db):
    conn = setup_db
    insert_student(conn, "Test Student", 20, "Test Major")
    delete_student(conn, 1)
    cursor = conn.execute("SELECT * FROM students WHERE id=1")
    deleted_student = cursor.fetchone()
    assert deleted_student is None


def test_count_students(setup_db):
    conn = setup_db
    insert_student(conn, "Test Student 1", 20, "Test Major")
    insert_student(conn, "Test Student 2", 22, "Test Major")
    insert_student(conn, "Test Student 3", 25, "Test Major")
    cursor = conn.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    assert count == 3


def test_get_students_above_age(setup_db):
    conn = setup_db
    insert_student(conn, "Test Student 1", 20, "Test Major")
    insert_student(conn, "Test Student 2", 22, "Test Major")
    insert_student(conn, "Test Student 3", 25, "Test Major")
    cursor = conn.execute("SELECT * FROM students WHERE age > 21")
    students_above_age = cursor.fetchall()
    assert len(students_above_age) == 2
    assert students_above_age[0][1] == "Test Student 2"
    assert students_above_age[1][1] == "Test Student 3"


if __name__ == "__main__":
    pytest.main()
