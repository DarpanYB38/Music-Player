from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

app = Flask(__name__)

# Set the directory to save uploaded songs
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('music_playlist.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to create the table if it doesn't exist
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            genre TEXT NOT NULL,
            file_path TEXT NOT NULL,
            playlist_order INTEGER NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Create the table when the app starts
create_table()

@app.route('/')
def index():
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs ORDER BY playlist_order').fetchall()
    conn.close()
    return render_template('index.html', songs=songs)

@app.route('/add_song', methods=['POST'])
def add_song():
    title = request.form['title']
    artist = request.form['artist']
    genre = request.form['genre']
    song_file = request.files['song_file']

    # Save the song file
    song_file_path = os.path.join(app.config['UPLOAD_FOLDER'], song_file.filename)
    song_file.save(song_file_path)

    # Insert song details into the database
    conn = get_db_connection()
    conn.execute('INSERT INTO songs (title, artist, genre, file_path, playlist_order) VALUES (?, ?, ?, ?, ?)',
                 (title, artist, genre, song_file_path, 0))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/play/<int:song_id>')
def play_song(song_id):
    conn = get_db_connection()
    song = conn.execute('SELECT * FROM songs WHERE id = ?', (song_id,)).fetchone()
    conn.close()
    return render_template('play.html', song=song)

@app.route('/delete_song/<int:song_id>', methods=['POST'])
def delete_song(song_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM songs WHERE id = ?', (song_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
