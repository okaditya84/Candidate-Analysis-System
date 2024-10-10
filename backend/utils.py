import PyPDF2
import docx
import subprocess
import tempfile

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

import subprocess

import os

import logging

# Extract audio function using FFmpeg
def extract_audio(input_video_path, output_audio_path):
    try:
        ffmpeg_command = [
            'ffmpeg',
            '-i', input_video_path,
            '-vn',  # Disable video
            '-acodec', 'pcm_s16le',  # Audio codec
            '-ar', '16000',  # Set sample rate to 16kHz
            '-ac', '1',  # Set to mono
            '-y',  # Overwrite output file if it exists
            output_audio_path
        ]
        
        subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        logging.info(f"Audio extracted successfully: {output_audio_path}")
        return output_audio_path
    except subprocess.CalledProcessError as e:
        logging.error(f"FFmpeg command failed: {e}")
        logging.error(f"FFmpeg stderr: {e.stderr}")
        raise
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        raise