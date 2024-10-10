import os
import logging
import tempfile
import speech_recognition as sr
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from utils import extract_audio
from groq import Groq
import json

import json
import logging
from groq import Groq
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk
from dotenv import load_dotenv
nltk.download('punkt_tab')

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Groq client
# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variable
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)



def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Try Google Speech Recognition first
            transcript = recognizer.recognize_google(audio_data)
            logging.info("Audio transcription completed using Google Speech Recognition.")
        except sr.RequestError as e:
            logging.warning(f"Could not request results from Google Speech Recognition service; {e}")
            try:
                # Fall back to PocketSphinx
                transcript = recognizer.recognize_sphinx(audio_data)
                logging.info("Audio transcription completed using PocketSphinx.")
            except sr.UnknownValueError:
                logging.error("PocketSphinx could not understand audio")
                transcript = ""
            except sr.RequestError as e:
                logging.error(f"PocketSphinx error; {e}")
                transcript = ""
        except sr.UnknownValueError:
            logging.error("Speech recognition could not understand audio")
            transcript = ""
        
        return transcript

def analyze_transcript(transcript, job_description):
    # Prepare the prompt for Groq
    prompt = f"""
    Analyze the following interview transcription for the given job description:

    Interview Transcription:
    {transcript}

    Job Description:
    {job_description}

    Provide the following in JSON format:
    1. A summary of the candidate's key points (max 150 words) with Keyword as Summary
    2. Evaluate the correctness of their responses (score out of 100) with keyword as Correctness
    3. Assess their communication skills (score out of 100) with keyword as Communication
    4. List 3 strengths demonstrated in the interview with keyword as Strengths
    5. Suggest 2 areas for improvement with keyword as Improvement
    6. Overall recommendation (Highly Recommended, Recommended, or Not Recommended) with keyword as Overall
    7. Keywords matched between the transcript and job description with keyword as Matched Words

    
    """

    # Get analysis from Groq
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            max_tokens=1000,
        )

        # Parse the JSON response
        try:
            analysis = json.loads(chat_completion.choices[0].message.content)
        except json.JSONDecodeError:
            logging.error("Failed to parse Groq response as JSON")
            logging.error(f"Raw response: {chat_completion.choices[0].message.content}")
            analysis = {}

        # Add additional analysis
        analysis['transcript'] = transcript
        analysis['word_count'] = len(word_tokenize(transcript))
        analysis['sentence_count'] = len(sent_tokenize(transcript))
        analysis['frequent_words'] = get_frequent_words(transcript)

        return analysis

    except Exception as e:
        logging.error(f"Error during transcript analysis: {e}")
        return {}

def analyze_interview(video_file, job_description):
    try:
        # Create a temporary file for the video
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
            video_file.save(temp_video.name)
            logging.info(f"Video saved to: {temp_video.name}")

        # Create a temporary file for the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            audio_file_path = temp_audio.name

        # Extract audio from the video
        extract_audio(temp_video.name, audio_file_path)

        # Log audio file details
        audio_size = os.path.getsize(audio_file_path)
        logging.info(f"Audio file size: {audio_size} bytes")

        # Transcribe the audio
        transcript = transcribe_audio(audio_file_path)
        logging.info(f"Transcription result (first 100 chars): {transcript[:100]}")

        # Analyze the transcript
        analysis_result = analyze_transcript(transcript, job_description)
        logging.info(f"Analysis result: {analysis_result}")

        # Cleanup temporary files
        os.unlink(temp_video.name)
        os.unlink(audio_file_path)

        return analysis_result

    except Exception as e:
        logging.error(f"Error during interview analysis: {e}")
        return {
            "summary": "An error occurred during the interview analysis process.",
            "correctness_score": 0,
            "communication_score": 0,
            "strengths": [],
            "areas_for_improvement": [],
            "recommendation": "Unable to provide recommendation due to analysis error.",
            "keywords_matched": []
        }

def get_frequent_words(text, top_n=10):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    freq_dist = FreqDist(words)
    return freq_dist.most_common(top_n)

# If you need to run any initialization code
def init():

    nltk.download('punkt')
    nltk.download('stopwords')

# Run initialization if this script is run directly
if __name__ == "__main__":
    init()