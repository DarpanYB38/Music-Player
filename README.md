# Music System Project 🎵

This is a simple yet functional **Music System Web Application** built using Python, Flask, HTML, and CSS. The application allows users to manage a playlist by adding songs, playing them, and removing them. The focus is on delivering an intuitive user interface along with basic music management functionalities.

---

## Features 🚀

- 🎶 **Add Songs**: Add songs with metadata like title, artist, and duration.
- ▶️ **Play Songs**: Play music directly from the playlist.
- ❌ **Remove Songs**: Remove songs from the playlist.
- 🎨 **Beautiful UI**: Designed with a clean and visually appealing user interface.
- 📂 **Dynamic Playlist**: Displays songs in the playlist dynamically.

---

## Technologies Used 🛠️

- **Backend**: Flask (Python Framework)
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Music Playback**: HTML `<audio>` element

---

## How to Run Locally 🖥️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/music-system.git
   cd music-system
   
2. Set up a Virtual Environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Initialize the Database: Run the following script to create and initialize the SQLite database:
   ```bash
   python initialize_db.py

5. Run the Application:
   ```bash
   python app.py

6. Access the App: Open your browser and go to http://127.0.0.1:5000

## File Structure
7. files
    ```bash
    music-system/
    │
    ├── app.py                   # Main Flask app
    ├── templates/
    │   ├── index.html           # Playlist page
    │   ├── add_song.html        # Add song form
    │   ├── error.html           # Error handling page
    ├── static/
    │   ├── styles.css           # CSS for UI
    │   ├── songs/               # Directory to store uploaded songs
    ├── requirements.txt         # Python dependencies
    ├── initialize_db.py         # Script to set up the database
    └── README.md                # Project documentation
   
## Future Imporvements
- Add user authentication for personalized playlists.
- Integrate a search bar for easy song filtering.
- Allow drag-and-drop uploads for songs.
- Implement sorting and categorization of songs by artist, genre, etc.

## Contributing 🤝
Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or create a pull request.

## License 📜
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact 💬
Name: Darpan YB
Email: darpanbrahma@gmai.com
GitHub: DarpanYB38

Feel free to reach out for any questions or suggestions!
Enjoy the music! 🎧
