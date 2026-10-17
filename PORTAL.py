import REG_E as ub
import REG_C as uc
from prettytable import PrettyTable
from datetime import date
a=False
today = date.today()
p=""
def login(conn, c1):
    while True:
        print("WELCOME TO CLUB PORTAL")
        print("1. Sign In")
        print("2. Create Account")
        print("3. Exit")
        global p
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            u = input("Enter username: ")
            p = input("Enter password: ")

            c1.execute("SELECT * FROM member WHERE member_name = %s AND member_id = %s", (u, p))
            record = c1.fetchone()

            if record:
                print("\nWelcome! Login successful.\n")
                return True
            else:
                print("\nInvalid username or password. Please try again.\n")
        elif choice == '2':
            print("\n CREATE NEW ACCOUNT ")
            member_id = input("Enter a new Member ID: ")
            member_name = input("Enter your username: ")
            grade = input("Enter your grade: ")
            club_id = input("Enter your club ID: ")
            post = input("Enter your post (e.g., Member, President): ")
            doj = today

            try:
                c1.execute(
                    "INSERT INTO member (member_id, member_name, grade, club_id, post, DOJ) VALUES (%s, %s, %s, %s, %s, %s)",
                    (member_id, member_name, grade, club_id, post, doj)
                )
                conn.commit()
                print("\nAccount created successfully! You can now sign in.\n")
            except Exception as e:
                print(f"\nError creating account: {e}\n")
        elif choice == '3':
            print("Exiting login portal")
            return False
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")

def search(conn, c1, u):
    c1.execute("SELECT * FROM member WHERE member_id = %s", (u,))
    result = c1.fetchall()

    if result:
        table = PrettyTable(["Member ID", "Member Name", "Grade", "Club ID", "Post", "Date of Joining"])
        for row in result:
            table.add_row(row)
        print("\n=== YOUR MEMBER INFORMATION ===")
        print(table)
    else:
        print("No information found for your account.\n")

def menu(conn, c1):
    while True:
            print("""PORTAL  MENU
1.VIEW ALL CLUBS YOU HAVE REGISTERED IN
2.REGISTER FOR A CLUB
3.REGISTER FOR AN EVENT
4.VIEW ALL CLUBS
5.VIEW ALL EVENTS
6.EXIT""")
            ach = int(input("Enter which function: "))
            if ach == 1:
                search(conn,c1,p)
            elif ach == 2:
                uc.inst(conn, c1)
            elif ach == 3:
                ub.inst(conn, c1)
            elif ach == 4:
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
            elif ach == 5:
                c1.execute("SELECT * FROM event")
                result = c1.fetchall()
                if result:
                    print("List of Ongoing Events:")
                    table = PrettyTable(["Event Name", "Event ID", "Club ID", "Event Date", "Venue", "Description"])
                    for row in result:
                        table.add_row(row)
                        table.max_width = 20 
                    print(table)
                else:
                    print("No events found.")
                    return
            elif ach == 6:
                print("Exiting portal menu...")
                break
            else:
                print("Invalid choice. Please try again.")

