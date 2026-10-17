import mysql.connector as sql
import CLUB as aa
import MEMBER as ab
import EVENT as ac
import TEACHER as ad
import PORTAL as ua
from prettytable import PrettyTable
import pyfiglet

conn = sql.connect(
    host='localhost',
    user='root',
    password='your_password_here')
if conn.is_connected():
    print("Successfully connected!")
c1 = conn.cursor()
c1.execute("create database if not exists school_club_management")
c1.execute("use school_club_management")
#club
c1.execute("""
create table if not exists club (
    club_id VARCHAR(20) PRIMARY KEY,
    club_name VARCHAR(50),
    description VARCHAR(500),
    tch_incharge VARCHAR(90),
    mem_count int)""")

#member 
c1.execute("""
create table if not exists member (
    member_id VARCHAR(20) PRIMARY KEY,
    member_name VARCHAR(50),
    grade int,
    club_id VARCHAR(200),
    post VARCHAR(20),
    DOJ date)""")

#event
c1.execute("""
create table if not exists event (
    event_name VARCHAR(50),
    event_id int PRIMARY KEY,
    club_id VARCHAR(20),
    event_date date,
    venu varchar(50),
    description VARCHAR(500))""")

#teacher
c1.execute("""
create table if not exists teacher (
    tch_id VARCHAR(20) PRIMARY KEY,
    tch_name VARCHAR(50),
    club_id VARCHAR(20),
    email varchar(50))
    """)
#REG_E
c1.execute("""
CREATE TABLE IF NOT EXISTS register_event (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id VARCHAR(20),
    event_id INT,
    qualification VARCHAR(100),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id)
)
""")

#REG_C
c1.execute("""
CREATE TABLE IF NOT EXISTS register_f_club (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    club_id VARCHAR(20),
    member_id VARCHAR(20),
    qualification VARCHAR(50),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (club_id) REFERENCES club(club_id)
)
""")
result = pyfiglet.figlet_format("SCHOOL CLUB MANAGEMENT SYSTEM", font = "digital" )
print(result)
while True:
    z=input("ARE YOU A USER OR ADMIN(U/A):")
    if z.upper()=="U":
        if ua.login(conn, c1):
            result = pyfiglet.figlet_format("PORTAL", font = "digital" )
            print(result)
            ua.menu(conn, c1)
    elif z.upper() =="A":
        result = pyfiglet.figlet_format("TABLE MENU", font = "digital" )
        print(result)
        print("""
1.CLUB
2.MEMBER
3.EVENT
4.TEACHER""")
        ch=int(input("enter which table:"))
        if ch==1:
            result = pyfiglet.figlet_format("CLUB", font = "digital" )
            print(result)
            aa.menu(conn,c1)
        elif ch==2:
            result = pyfiglet.figlet_format("MEMBER", font = "digital" )
            print(result)
            ab.menu(conn,c1)
        elif ch==3:
            result = pyfiglet.figlet_format("EVENT", font = "digital" )
            print(result)
            ac.menu(conn,c1)
        elif ch==4:
            result = pyfiglet.figlet_format("TEACHER", font = "digital" )
            print(result)
            ad.menu(conn,c1)
        else:
            break
            
        
