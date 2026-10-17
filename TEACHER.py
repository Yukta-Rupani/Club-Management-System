from prettytable import PrettyTable
def inst(conn, c1):
    try:
        ans = "y"
        while ans.lower() == "y":
            tch_id = input("Enter teacher ID: ")
            tch_name = input("Enter teacher name: ")
            club_id = input("Enter club ID: ")
            email = input("Enter email: ")
            query = "INSERT INTO teacher (tch_id , tch_name, club_id, email) VALUES (%s, %s, %s, %s)"
            values = (tch_id , tch_name, club_id, email)
            c1.execute(query, values)
            conn.commit()
            print("__RECORD SAVED__")

            ans = input("Do you want to add more? (y/n): ")
            if ans.lower() != "y":
                break
    except Exception as e:
        print("Error:", e)
        conn.rollback()
def update(conn, c1):
    c = 'y'
    while c.lower() == 'y':
        try:
            tid = input("Enter Teacher ID to update: ")
            c1.execute("SELECT * FROM teacher WHERE tch_id = %s", (tid,))
            if not c1.fetchall():
                print("No teacher found with that ID.")
            else:
                new_email = input("Enter new email: ")
                c1.execute("UPDATE teacher SET email = %s WHERE tch_id = %s", (new_email, tid))
                conn.commit()
            print("TEACHER updated successfully.")
            c = input("Continue updating another club? (y/n): ")
            if c.lower()=="n":
                break
        except Exception as e:
            print("Error: {e}")
def display(conn,c1):
    c1.execute("SELECT * FROM teacher")
    rows = c1.fetchall()
    if rows:
        table = PrettyTable(["teacher ID", "teacher Name", "club id", "email"])
        for row in rows:
            table.add_row(row)
            table.max_width = 20 
        print(table)
    else:
        print("No clubs found.\n")
def search (conn,c1):
    name = input("Enter teacher name to search: ")
    query = "SELECT * FROM teacher WHERE tch_name = %s"
    c1.execute(query, (name,))
    result = c1.fetchall()
    if result:
        table = PrettyTable(["teacher ID", "teacher Name", "club id", "email"])
        for row in result:
            table.add_row(row)
            table.max_width = 20 
        print(table)
    else:
        print("No records found.\n")
def delete(conn, c1):
    c = 'y'
    while c.lower() == 'y':
        try:
            print('Deleting teacher details')
            teacher_id = input("Enter the Teacher ID to remove: ")
            q = "DELETE FROM teacher WHERE tch_id = %s"
            c1.execute(q, (teacher_id,))
            if c1.rowcount == 0:
                print("No teacher found with ID", teacher_id)
            else:
                conn.commit()
                print('Teacher record deleted successfully!')
            c = input('Continue deleting? (y/n): ')
        except Exception as e:
            print(f"An error occurred: {e}")

def menu(conn,c1):
    while True:
        print("""TEACHER MENU
1.INSERT
2.DISPLAY
3.SEARCH
4.DELETE 
5.UPDATE
6.EXIT""")
        ach=int(input("enter which function:"))
        if ach==1:
            inst(conn, c1)
        elif ach==2:
            display(conn,c1)
        elif ach==3:
            search(conn,c1)
        elif ach==4:
            delete(conn,c1)
        elif ach==5:
            update(conn, c1)
        elif ach==6:
            break
