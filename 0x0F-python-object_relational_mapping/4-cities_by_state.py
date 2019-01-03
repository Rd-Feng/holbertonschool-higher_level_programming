#!/usr/bin/python3
""" list all cities """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("""
        SELECT c.id, c.name, s.name
        FROM cities AS c LEFT JOIN states AS s
        ON c.state_id = s.id
        ORDER BY c.id;
        """)
    for row in cur.fetchall():
        print(row)
