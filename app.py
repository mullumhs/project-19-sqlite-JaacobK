import sqlite3



conn = sqlite3.connect('movies.db')

cursor = conn.cursor()



# Create the movies table

cursor.execute('''

CREATE TABLE IF NOT EXISTS movies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    director TEXT,

    year INTEGER,

    rating FLOAT

)

''')

movies = [

    ('The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),
    ('Inception', 'Christopher Nolan', 2010, 8.8),
    ('The Matrix', 'Lana and Lilly Wachowski', 1999, 8.7),
    ('Interstellar', 'Christopher Nolan', 2014, 8.6)
]



# Insert multiple movies

cursor.executemany('''
INSERT INTO movies (title, director, year, rating)
VALUES (?, ?, ?, ?)
''', movies)

cursor.execute('SELECT * FROM movies')
all_movies = cursor.fetchall()
print("All movies:")
for movie in all_movies:
    print(movie)

cursor.execute('SELECT title FROM movies WHERE year > 2000')
recent_movies = cursor.fetchall()
for movie in recent_movies:
    print(movie)

cursor.execute('DROP TABLE movies')

# Commit the changes and close the connection
conn.commit()
conn.close()

