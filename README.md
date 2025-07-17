# Transcriber-App
Basically this app transcribes videos  when you paste any video links inside it.

A powerful, lightweight **audio/video transcriber app** built using OpenAI's Whisper model. It allows users to upload YouTube links or local audio/video files and receive accurate transcription in multiple languages — all with a simple web interface.

---

## 📌 Features

- 🎙️ Transcribe **audio/video files**
- 🔗 Accept **YouTube URLs** for transcription
- 🌍 Supports **multiple languages**
- 🧠 Powered by **OpenAI Whisper**
- 📄 Downloadable transcripts
- ⚡ Built with **Streamlit**

---

## 🧠 How It Works

1. 🎥 Accepts a **file** or **YouTube URL**
2. 🔄 Converts to `.wav` format (if video)
3. 🧠 Runs Whisper (small/base/medium/large model)
4. 📝 Outputs transcript
5. 💾 Allows download as `.txt`

---

## 🚀 Demo

[Click to Try the Live App](#) *(Add Hugging Face/Render link once deployed)*

---

## 🛠️ Tech Stack

| Tech          | Role                          |
|---------------|-------------------------------|
| Python        | Core programming language      |
| Streamlit     | Web frontend UI                |
| OpenAI Whisper| Transcription engine           |
| ffmpeg        | Audio/video format conversion  |
| pytube        | YouTube URL downloader         |
| Hugging Face / Render | Optional Deployment   |

---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/transcriber-app.git
cd transcriber-app


python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


pip install -r requirements.txt


4. Install ffmpeg
Make sure ffmpeg is installed and added to your system path.


streamlit run app.py


Inside the app:
Upload a local file OR

Paste a YouTube URL

Choose model size (tiny/small/base/etc.)

Wait for transcription...

Copy or download the result



transcriber-app/
├── app.py
├── utils.py
├── requirements.txt
├── audio/              # temp audio files
├── transcripts/        # saved transcript output
├── README.md
└── .gitignore


🙌 Acknowledgements
OpenAI Whisper

Streamlit

PyTube

FFmpeg


👤 Author
Ayush
🌐 Your Portfolio
📫 Contact: yourname@email.com
🔗 LinkedIn | Twitter | GitHub

