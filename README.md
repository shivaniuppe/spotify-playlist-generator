# 🎵 Spotify Playlist Generator

Automatically generate a Spotify playlist based on your **recently played tracks** using Python + Spotify Web API.

Perfect for discovering your current vibe in playlist form. Easy to set up and clone!

---

## 🚀 Features

- ✅ Authenticates your Spotify account securely
- 🎶 Fetches your recently played tracks
- 📂 Creates a new public playlist named *"Mood Booster 🎶"*
- 💾 Adds those tracks into the playlist automatically
- 💻 Fully local — no server or deployment needed

---

## 🧰 Requirements

- Python 3.8+
- A [Spotify account](https://spotify.com/)
- A [Spotify Developer App](https://developer.spotify.com/dashboard/)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/spotify-playlist-generator.git
cd spotify-playlist-generator
```

### 2. Set Up Virtual Environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Spotify Developer App

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create an app → Note the **Client ID** and **Client Secret**
- Add a **Redirect URI**:  
  ```
  http://127.0.0.1:8888/callback
  ```

### 5. Add Environment Variables

Copy the example and fill in your values:

```bash
cp .env.example .env
```

Then edit `.env`:
```env
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

---

## ▶️ Run the App

```bash
python main.py
```

- A browser will open for you to log into Spotify
- The script will create your personalized playlist 🎉

---

## 📁 Project Structure

```
spotify-playlist-generator/
│
├── main.py             # Main script
├── .env.example        # Template for environment variables
├── requirements.txt    # Python dependencies
├── README.md           # You're here!
└── .gitignore          # Excludes sensitive or unnecessary files
```

---

## 🛑 Do Not Push Your `.env` File

Your real credentials should **never** be committed to GitHub. They are safely ignored via `.gitignore`.

---

## 💡 Future Ideas

- Mood-based playlist generation using genre or sentiment
- Schedule daily playlists with `cron`
- Add a simple Streamlit UI
- Share playlist links via Telegram or Email

---

## 👩‍💻 Made by Shivani Uppe

Enjoy your playlist! 🎧  
Feel free to fork, star, or contribute!
