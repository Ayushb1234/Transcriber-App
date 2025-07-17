import streamlit as st
import os
from transcriber import download_audio, transcribe_audio, save_transcripts

st.set_page_config(page_title="YouTube Whisper Transcriber", layout="centered")

st.title("🎙️ YouTube Video Transcriber using OpenAI Whisper")

# Input Section
url = st.text_input("📺 Enter YouTube Video URL")

model_size = st.selectbox("Select Whisper Model Size", ["tiny", "base", "small", "medium", "large"])

if st.button("🎯 Transcribe"):
    if not url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        try:
            st.info("Downloading audio...")
            audio_file = "audio.mp3"
            download_audio(url, audio_file)

            st.success("✅ Audio downloaded!")
            st.info(f"Transcribing using '{model_size}' model...")
            result = transcribe_audio(audio_file, model_size)

            base_name = os.path.splitext(audio_file)[0]
            save_transcripts(result, base_name)

            st.success("🎉 Transcription Complete!")
            st.download_button("⬇ Download Transcript (.txt)", data=open(f"transcripts/{base_name}.txt", "rb").read(), file_name="transcript.txt")
            st.download_button("⬇ Download Subtitles (.srt)", data=open(f"transcripts/{base_name}.srt", "rb").read(), file_name="subtitles.srt")
            st.download_button("⬇ Download Web Captions (.vtt)", data=open(f"transcripts/{base_name}.vtt", "rb").read(), file_name="captions.vtt")

            st.subheader("📄 Preview Transcript:")
            st.write(result["text"])

        except Exception as e:
            st.error(f"❌ Error: {e}")
