import os
import subprocess
import whisper
from pytube import YouTube

def download_audio(url: str, output_path: str = "audio.mp3"):
    subprocess.run([
        "yt-dlp", "-x", "--audio-format", "mp3",
        "-o", output_path,
        url
    ], check=True)
    return output_path

def transcribe_audio(audio_path: str, model_size="small"):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result

def save_transcripts(result, base_filename):
    os.makedirs("transcripts", exist_ok=True)

    # .txt
    with open(f"transcripts/{base_filename}.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])

    # .srt
    srt = ""
    for i, seg in enumerate(result["segments"]):
        start = seg['start']
        end = seg['end']
        srt += f"{i+1}\n{format_time(start)} --> {format_time(end)}\n{seg['text'].strip()}\n\n"
    with open(f"transcripts/{base_filename}.srt", "w", encoding="utf-8") as f:
        f.write(srt)

    # .vtt
    vtt = "WEBVTT\n\n"
    for seg in result["segments"]:
        vtt += f"{format_vtt(seg['start'])} --> {format_vtt(seg['end'])}\n{seg['text'].strip()}\n\n"
    with open(f"transcripts/{base_filename}.vtt", "w", encoding="utf-8") as f:
        f.write(vtt)

def format_time(seconds):
    return f"{int(seconds // 3600):02}:{int((seconds % 3600) // 60):02}:{int(seconds % 60):02},000"

def format_vtt(seconds):
    return f"{int(seconds // 3600):02}:{int((seconds % 3600) // 60):02}:{seconds % 60:.3f}".replace('.', ',')

