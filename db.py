import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS posts;
        """
    )
    conn.execute(
        """
        CREATE TABLE posts (
          id INTEGER PRIMARY KEY NOT NULL,
          user_id INTEGER,
          title STRING,
          body TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    posts_seed_data = [
        (1, "The Chicago Cubs: More Than Just a Team", "In the heart of Chicago, Wrigley Field stands not just as a stadium, but as a testament to enduring passion and loyalty. The Chicago Cubs, with their storied history, are more than just a baseball team; they are a symbol of perseverance. From the legendary 'Curse of the Billy Goat' to the euphoric 2016 World Series victory, the Cubs' journey mirrors Chicago's spirit: resilient and unwavering. Each game is a convergence of generations, where stories, traditions, and hopes are shared. The Cubs aren't just Chicago's pride; they're a beacon of hope, teaching us that no matter how long the wait, triumph is always within reach."),
        (2, "Al Capone: The Infamous Legend of Chicago", "Al Capone, a name synonymous with Chicago's history, encapsulates an era of both allure and infamy. In the roaring twenties, Capone rose to notoriety, his influence permeating the streets of Chicago. He was more than a notorious gangster; he was a paradoxical figure, feared and revered, a criminal mastermind and a folk hero. The tales of speakeasies, bootlegging, and the St. Valentine's Day Massacre paint a picture of a city gripped by both charm and chaos. Exploring Capone's legacy offers a glimpse into a turbulent period in Chicago's history, where lawlessness and charisma intertwined in the shadowy corners of the Windy City."),
        (3, "The Architectural Marvels of Chicago", "Chicago is not just a city; it's an architectural wonderland. Rising from the ashes of the Great Chicago Fire, the city became a canvas for visionary architects. The skyline, dotted with masterpieces like the Willis Tower and the neo-Gothic Tribune Tower, tells a story of innovation and resilience. Each building is a chapter in Chicago's narrative, showcasing styles ranging from Art Deco to Chicago School. The city's architecture is a dialogue between the past and the present, a blend of historical preservation and cutting-edge design. Strolling through Chicago is like walking through a living museum, each structure whispering tales of the city's relentless ambition and artistic spirit."),
    ]
    conn.executemany(
        """
        INSERT INTO posts (user_id, title, body)
        VALUES (?,?,?)
        """,
        posts_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()


def posts_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM posts
        """
    ).fetchall()
    return [dict(row) for row in rows]

def posts_create(user_id, title, body):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO posts (user_id, title, body)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (user_id, title, body),
    ).fetchone()
    conn.commit()
    return dict(row)

def posts_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM posts
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

def posts_update_by_id(id, user_id, title, body):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE posts SET user_id = ?, title = ?, body = ?
        WHERE id = ?
        RETURNING *
        """,
        (user_id, title, body, id),
    ).fetchone()
    conn.commit()
    return dict(row)
# how do i make it take in params or if blank stays the same (user_id)