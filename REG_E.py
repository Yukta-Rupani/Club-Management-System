from prettytable import PrettyTable

def inst(conn, c1):
    try:
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
        print("\nEnter event registration details:")
        member_id = input("Enter Member ID: ")
        event_id = input("Enter Event ID: ").strip()
        if "," in event_id or " " in event_id:
            print("Error: You can register for only ONE event at a time.")
            return
        qualification = input("Enter Qualification (top 2): ")
        query = "INSERT INTO register_event (member_id, event_id, qualification) VALUES (%s, %s, %s)"
        values = (member_id, event_id, qualification)
        c1.execute(query, values)
        conn.commit()
        print("Event registration successful!")
    except Exception as e:
        print("Error:", e)
        conn.rollback()

