-- convert hbtn_0c_0 database to UTF8
-- utf8mb4, collate utf8mb4_unicode_ci
-- convert database
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;
-- select db
USE hbtn_0c_0;
-- convert table first_table
ALTER TABLE first_table CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- convert column name
ALTER TABLE first_table
CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
