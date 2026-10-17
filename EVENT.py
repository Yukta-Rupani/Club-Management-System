from prettytable import PrettyTable
def inst(conn, c1):
    import random as r
    try:
        ans = "y"
        while ans.lower() == "y":
            event_name = input("Enter event name: ")
            event_id = r.randint(1000,10000)
            club_id = input("Enter club ID: ")
            venu = input("Enter venu: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            query = "INSERT INTO event ( event_name,event_id, club_id, venu, event_date,description) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (event_name, event_id, club_id, venu, event_date,description)

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
            eid = input("Enter Event ID to update: ")
            c1.execute("SELECT * FROM event WHERE event_id = %s", (eid,))
            if not c1.fetchall():
                print("No event found with that ID.")
            else:
                print('''Update Event:
1. Venue
2. Event Date
3. Exit''')

                while True:
                    ch = int(input("Enter choice: "))
                    if ch == 1:
                        new_venue = input("Enter new venue: ")
                        c1.execute("UPDATE event SET venu = %s WHERE event_id = %s", (new_venue, eid))
                    elif ch == 2:
                        new_date = input("Enter new event date (YYYY-MM-DD): ")
                        c1.execute("UPDATE event SET event_date = %s WHERE event_id = %s", (new_date, eid))
                    elif ch == 3:
                        break
                    else:
                        print("Invalid choice.")
                    conn.commit()
                    print("EVENT updated successfully.")
                    c = input("Continue updating another club? (y/n): ")
                    if c.lower()=="n":
                        break
        except Exception as e:
            print("Error: {e}")
def display(conn,c1):
    c1.execute("SELECT * FROM event")
    rows = c1.fetchall()
    if rows:
        table = PrettyTable(["Event Name", "Event ID", "Club ID", "Event Date", "Venue", "Description"])
        for row in rows:
            table.add_row(row)
            table.max_width = 20 
        print(table)
    else:
        print("No events found.\n")
def search (conn,c1):
    name = input("Enter event name to search: ")
    query = "SELECT * FROM event WHERE event_name = %s"
    c1.execute(query, (name,))
    result = c1.fetchall()
    if result:
        table = PrettyTable(["Event Name", "Event ID", "Club ID", "Event Date", "Venue", "Description"])
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
            print('Deleting event details')
            event_id = input("Enter the Event ID to remove: ")
            q = "DELETE FROM event WHERE event_id = %s"
            c1.execute(q, (event_id,))
            if c1.rowcount == 0:
                print("No event found with ID", event_id)
            else:
                conn.commit()
                print('Event record deleted successfully!')
            c = input('Continue deleting? (y/n): ')
        except Exception as e:
            print(f"An error occurred: {e}")

def menu(conn,c1):
    while True:
        print("""EVENT MENU
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
