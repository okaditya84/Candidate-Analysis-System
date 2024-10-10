import PyPDF2
import docx
from groq import Groq
from utils import extract_text_from_pdf, extract_text_from_docx
import json

client = Groq(
    api_key="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",
)

def analyze_resume(resume_file, job_description):
    if resume_file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.filename.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_file)
    else:
        return {"error": "Unsupported file format"}

    prompt = f"""
Analyze the following resume for the given job description:

Resume:
{resume_text}

Job Description:
{job_description}

Provide the following in JSON format:
    1. A summary of the candidate's key points (max 150 words) with Keyword as Summary
    2. Evaluate the correctness of their responses (score out of 100) with keyword as Correctness
    3. Assess their communication skills (score out of 100) with keyword as Communication
    4. List 3 strengths demonstrated in the interview with keyword as Strengths
    5. Suggest 2 areas for improvement with keyword as Improvement
    6. Overall recommendation (Highly Recommended, Recommended, or Not Recommended) with keyword as Overall
    7. Keywords matched between the transcript and job description with keyword as Matched Words.
"""

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="mixtral-8x7b-32768",
        max_tokens=1000,
    )
    
    # Debugging: Print the raw output
    print(chat_completion.choices[0].message.content)

    # Try parsing the content
    try:
        return json.loads(chat_completion.choices[0].message.content)
    except json.JSONDecodeError as e:
        return {"error": "Failed to parse response", "details": str(e)}