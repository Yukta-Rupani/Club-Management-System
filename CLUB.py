from prettytable import PrettyTable
def inst(conn, c1):
    try:
        ans = "y"
        while ans.lower() == "y":
            id_ = input("Enter club ID: ")
            name = input("Enter club name: ")
            desc_ = input("Enter description of club: ")
            tch = input("Enter name of teacher incharge: ")
            mem = int(input("Enter number of members: "))

            query = "INSERT INTO club (club_id, club_name, description, tch_incharge, mem_count) VALUES (%s, %s, %s, %s, %s)"
            values = (id_, name, desc_, tch, mem)
            c1.execute(query, values)
            conn.commit()
            print("__RECORD SAVED__")
            ans = input("Do you want to add more? (y/n): ")
            if ans.lower()=="y":
                pass
            else:
                break

    except:
        conn.rollback()
def update(conn, c1):
    c = 'y'
    while c.lower() == 'y':
        try:
            cid = input("Enter Club ID to update: ")
            c1.execute("SELECT * FROM club WHERE club_id = %s", (cid,))
            if not c1.fetchall():
                print("No club found with that ID.")
            else:
                print('''Update Club:
1. Teacher Incharge
2. Member Count
3. Exit''')

                while True:
                    ch = int(input("Enter choice: "))
                    if ch == 1:
                        new_tch = input("Enter new teacher incharge: ")
                        c1.execute("UPDATE club SET tch_incharge = %s WHERE club_id = %s", (new_tch, cid))
                    elif ch == 2:
                        new_mem = int(input("Enter new member count: "))
                        c1.execute("UPDATE club SET mem_count = %s WHERE club_id = %s", (new_mem, cid))
                    elif ch == 3:
                        break
                    else:
                        print("Invalid choice.")
                    conn.commit()
                    print("Club updated successfully.")
                    c = input("Continue updating another club? (y/n): ")
                    if c.lower()=="n":
                        break
        except Exception as e:
            print("Error: {e}")
def display(conn,c1):
    c1.execute("SELECT * FROM club")
    rows = c1.fetchall()
    if rows:
        table = PrettyTable(["Club ID", "Club Name", "Description", "Teacher Incharge", "Member Count"])
        for row in rows:
            table.add_row(row)
            table.max_width = 20 
        print(table)
    else:
        print("No clubs found.\n")
def search (conn,c1):
    name = input("Enter club name to search: ")
    query = "SELECT * FROM club WHERE club_name = %s"
    c1.execute(query, (name,))
    result = c1.fetchall()
    if result:
        table = PrettyTable(["Club ID", "Club Name", "Description", "Teacher Incharge", "Member Count"])
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
            print('Deleting club details')
            club_id = input("Enter the Club ID to remove: ")
            q = "DELETE FROM club WHERE club_id = %s"
            c1.execute(q, (club_id,))
            if c1.rowcount == 0:
                print("No club found with ID", club_id)
            else:
                conn.commit()
                print('Club record deleted successfully!')
            c = input('Continue deleting? (y/n): ')
        except Exception as e:
            print("An error occurred: {e}")

def menu(conn,c1):
    while True:
        print("""CLUB MENU
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
