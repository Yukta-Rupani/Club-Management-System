-- School Club Management System: database schema
-- These are the same tables the Python program creates automatically on startup.

CREATE DATABASE IF NOT EXISTS school_club_management;
USE school_club_management;

-- Stores details of all school clubs
CREATE TABLE IF NOT EXISTS club (
    club_id VARCHAR(20) PRIMARY KEY,
    club_name VARCHAR(50),
    description VARCHAR(500),
    tch_incharge VARCHAR(90),
    mem_count INT
);

-- Stores student details and membership information
CREATE TABLE IF NOT EXISTS member (
    member_id VARCHAR(20) PRIMARY KEY,
    member_name VARCHAR(50),
    grade INT,
    club_id VARCHAR(200),
    post VARCHAR(20),
    DOJ DATE
);

-- Stores event information including venue and date
CREATE TABLE IF NOT EXISTS event (
    event_name VARCHAR(50),
    event_id INT PRIMARY KEY,
    club_id VARCHAR(20),
    event_date DATE,
    venu VARCHAR(50),
    description VARCHAR(500)
);

-- Stores teacher coordinator details for each club
CREATE TABLE IF NOT EXISTS teacher (
    tch_id VARCHAR(20) PRIMARY KEY,
    tch_name VARCHAR(50),
    club_id VARCHAR(20),
    email VARCHAR(50)
);

-- Stores event registration records
CREATE TABLE IF NOT EXISTS register_event (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id VARCHAR(20),
    event_id INT,
    qualification VARCHAR(100),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id)
);

-- Stores club registration records
CREATE TABLE IF NOT EXISTS register_f_club (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    club_id VARCHAR(20),
    member_id VARCHAR(20),
    qualification VARCHAR(50),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (club_id) REFERENCES club(club_id)
);

-- Useful queries for checking the data
-- SELECT * FROM club;
-- SELECT * FROM member;
-- SELECT * FROM event;
-- SELECT * FROM teacher;
-- SELECT * FROM register_event;
-- SELECT * FROM register_f_club;
