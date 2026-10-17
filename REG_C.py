from prettytable import PrettyTable
from datetime import date
today = date.today()
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
        clubs = existing.split(",") if existing else []
        if new_club in clubs:
            print("You are already registered for this club!")
            return
        clubs.append(new_club)
        updated = ",".join(clubs)
        c1.execute("UPDATE member SET club_id = %s WHERE member_id = %s", (updated, member_id))
        conn.commit()
        print("Successfully registered for club:", new_club)
    except Exception as e:
        print("Error:", e)
