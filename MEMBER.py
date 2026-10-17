from prettytable import PrettyTable
def inst(conn, c1):
    try:
        c1.execute("SELECT * FROM club")
        rows = c1.fetchall()
        print("AVAILABLE CLUBS:")
        table = PrettyTable(["Club ID", "Club Name", "Description", "Teacher Incharge", "Member Count"])
        for row in rows:
            table.add_row(row)
            table.max_width = 20 
        print(table)
        print("REGISTER FOR A NEW CLUB")
        member_id = input("Enter your Member ID: ")
        new_club = input("Enter Club ID to Add: ")
        c1.execute("SELECT club_id FROM member WHERE member_id = %s", (member_id,))
        existing = c1.fetchone()[0]
        if new_club in existing:
            print("\nYou are already registered for this club!")
            return
        updated = existing + "," + new_club
        c1.execute("UPDATE member SET club_id = %s WHERE member_id = %s", (updated, member_id))
        conn.commit()
        print("Successfully registered for club:", new_club)

    except Exception as e:
        print(f"Error:", e)

def update(conn, c1):
    c = 'y'
    while c.lower() == 'y':
        try:
            mid = input("Enter Member ID to update: ")
            c1.execute("SELECT * FROM member WHERE member_id = %s", (mid,))
            if not c1.fetchall():
                print("No member found with that ID.")
            else:
                print('''Update Member:
1. Grade
2. Post
3. Exit''')

                while True:
                    ch = int(input("Enter choice: "))
                    if ch == 1:
                        new_grade = int(input("Enter new grade: "))
                        c1.execute("UPDATE member SET grade = %s WHERE member_id = %s", (new_grade, mid))
                    elif ch == 2:
                        new_post = input("Enter new post: ")
                        c1.execute("UPDATE member SET post = %s WHERE member_id = %s", (new_post, mid))
                    elif ch == 3:
                        break
                    else:
                        print("Invalid choice.")
                    conn.commit()
                    print("MEMBER updated successfully.")
                    c = input("Continue updating another club? (y/n): ")
                    if c.lower()=="n":
                        break
        except Exception as e:
            print(f"Error: {e}")
def display(conn,c1):
    c1.execute("SELECT * FROM member")
    rows = c1.fetchall()
    if rows:
        table = PrettyTable(["Member ID", "Member Name", "Grade", "Club ID", "Post", "Date of Joining"])
        for row in rows:
            table.add_row(row)
            table.max_width = 20 
        print(table)
    else:
        print("No clubs found.\n")
def search (conn,c1):
    name = input("Enter member id to search: ")
    query = "SELECT * FROM member WHERE member_id = %s"
    c1.execute(query, (name,))
    result = c1.fetchall()
    if result:
        table = PrettyTable(["Member ID", "Member Name", "Grade", "Club ID", "Post", "Date of Joining"])
        for row in result:
            table.add_row(row)
            table.max_width = 20 
        print(table)
    else:
        print("No record found.\n")
def delete(conn, c1):
    c = 'y'
    while c.lower() == 'y':
        try:
            print('Deleting member details')
            member_id = input("Enter the Member ID to remove: ")
            c1.execute("DELETE FROM register_f_club WHERE member_id = %s", (member_id,))
            c1.execute("DELETE FROM register_event WHERE member_id = %s", (member_id,))
            q = "DELETE FROM member WHERE member_id = %s"
            c1.execute(q, (member_id,))
            if c1.rowcount == 0:
                print("No member found with ID", member_id)
            else:
                conn.commit()
                print('Member record deleted successfully!')
            c = input('Continue deleting? (y/n): ')
        except Exception as e:
            print(f"An error occurred: {e}")

    
def menu(conn,c1):
    while True:
        print("""MEMBER MENU
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
        
