# jf361_ids706_mp5
[![Python SQL CRUD CI](https://github.com/siyiia/jf361_ids706_mp5/actions/workflows/cicd.yml/badge.svg)](https://github.com/siyiia/jf361_ids706_mp5/actions/workflows/cicd.yml)

## Project Introduction
This project is to create Python script interacting with SQL database


## Project Requirments
- Connect to a SQL database
- Perform CRUD operations
- Write at least two different SQL queries

## Project Setup
1. **Connect to SQL database**:
To connect to a SQL database, use the following code snippet. If the specified database (`db_name`) doesn't exist, SQLite will automatically create one:
    ```python
    import sqlite3
    db_name = "student.db"
    conn = sqlite3.connect(db_name)
    ```
   Screenshot of successfully connect to a SQL database
   <p>
     <img width="400" src="screenshots/connect.png" />
   </p>

2. **Perform CRUD operations**
   1. **[C] Create operation**: use `INSERT` INTO SQL queries to insert a new record.
         ```
         conn.execute("INSERT INTO students (column_name1, column_name2, column_name3) VALUES (?, ?, ?)", (column_name1_value, column_name2_value, column_name3_value))
         conn.commit()
         ```
      Screenshot of successfully perform **Create operation**
      <p>
        <img width="400" src="screenshots/C.png" />
      </p>
   2. **[R] Read operation**: use `SELECT` SQL queries to read the records from the database.
         ```
         conn.execute("SELECT * FROM table_name")
         ```
      Screenshot of successfully perform **Read operation**
      <p>
        <img width="400" src="screenshots/R.png" />
      </p>
   3. **[U] Update operation**: use `UPDATE` SQL queries to modify the data in a table.
         ```
         conn.execute("UPDATE table_name SET column_name = ? WHERE primary_key = ?", (column_name_value, primary_key_value))
         conn.commit()
         ``` 
      Screenshot of successfully perform **Update operation**
      <p>
        <img width="400" src="screenshots/U.png" />
      </p>
   4. **[D] Delete operation**: use `DELETE FROM` SQL queries to remove records.
         ```
         conn.execute("DELETE FROM table_name WHERE primary_key = ?", (primary_key_value,))
         conn.commit()
         ```
      Screenshot of successfully perform **Delete operation**
      <p>
        <img width="400" src="screenshots/D.png" />
      </p>
3. **Write two different SQL queries**
   1. Count number of rows in a table
        ```
        conn.execute("SELECT COUNT(*) FROM table_name")
      ```
      Screenshot of the results of above SQL query
      <p>
        <img width="400" src="screenshots/Q1.png" />
      </p>
   2. Get rows where a column's value is greater than a specified threshold
        ```
      conn.execute("SELECT * FROM table_name WHERE column_name > ?", (threshold_value,))
      ```
      Screenshot of the results of above SQL query
      <p>
        <img width="400" src="screenshots/Q2.png" />
      </p>
   
## Summary Screenshot of Successful Database Operations
<p>
  <img width="300" src="screenshots/total.png" />
</p>
