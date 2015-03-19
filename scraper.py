import sqlite3
import os
import csv

def main():
    db = sqlite3.connect(os.path.expanduser("~/.config/Clementine/clementine.db"))

    cursor = db.cursor()

    rows = [(row[0], row[1], row[2], row[13]) for row in cursor.execute("SELECT * FROM songs")]

    writer = csv.writer(open('clem.csv', 'w'))
    writer.writerow(('Title', 'Album', 'Artist', 'Bitrate'))
    writer.writerows(rows)

    db.close()

if __name__ == '__main__':
    main()
