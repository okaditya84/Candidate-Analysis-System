# Candidate Evaluation System

## Overview
The **Candidate Evaluation System** allows users to evaluate both resumes and interview videos against a provided job description. It returns a detailed analysis of the candidate's strengths, areas for improvement, and scores based on various criteria such as correctness and communication.

## Key Features

### 1. **Resume Analysis**
- **Upload Resume**: Supports PDF and DOCX file formats.
- **Job Description**: Users input a job description to guide the analysis process.
- **Correctness Score**: Evaluates how well the resume aligns with the job description.
- **Strengths & Areas for Improvement**: Summarizes the candidate's strong points and where they can improve.
- **Recommendation**: Provides an overall recommendation based on the analysis.

### 2. **Interview Analysis**
- **Upload Interview Video**: Users can upload video files for analysis.
- **Job Description**: Tailors the analysis based on the provided job description.
- **Communication Score**: Assesses the candidate's communication skills.
- **Strengths & Areas for Improvement**: Highlights the candidate's strengths and where they need to improve.
- **Recommendation**: Offers a final recommendation based on the interview performance.

### 3. **Interactive and Responsive UI**
- Built with **React** and styled with **Tailwind CSS**, the UI is intuitive and responsive.
- The application includes two main sections: **Resume Analysis** and **Interview Analysis**, which can be easily switched using navigation buttons.

### 4. **Comprehensive Analysis Results**
- For each analysis (resume or interview), the results include:
  - **Summary**: Key points from the analysis.
  - **Scores**: Correctness score for resumes and communication score for interviews.
  - **Strengths and Areas for Improvement**: Detailed feedback on candidate performance.
  - **Recommendation**: A summary recommendation for the candidate's suitability.

## Installation and Setup

### 1. **Backend Setup**
- The backend is built using Python and Flask. It performs the analysis of the resumes and interview videos.
  
#### Prerequisites:
- Python 3.x
- Flask
- Other dependencies listed in `requirements.txt`

#### Steps:
1. Navigate to the `backend/` directory:
    ```bash
    cd backend
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Start the Flask server:
    ```bash
    python app.py
    ```
    The server will run on `http://localhost:5000`.

### 2. **Frontend Setup**
- The frontend is built with **React** and uses **Tailwind CSS** for styling.

#### Prerequisites:
- Node.js and npm

#### Steps:
1. Navigate to the `frontend/` directory:
    ```bash
    cd frontend
    ```
2. Install the required dependencies:
    ```bash
    npm install
    ```
3. Start the React development server:
    ```bash
    npm start
    ```
    The development server will run on `http://localhost:3000`.

### 3. **Connecting Frontend to Backend**
- The frontend is configured to communicate with the Flask backend. Ensure both servers (Flask and React) are running simultaneously for full functionality.

## File Structure

```bash
CANDIDATE ANALYSIS SYSTEM/
│
├── backend/
│   ├── __pycache__/             # Python cache files
│   ├── .env                     # Environment configuration
│   ├── app.py                   # Main Flask server
│   ├── candidate_analysis.db     # Database (if required)
│   ├── database.py              # Database management code
│   ├── interview_analysis.py     # Interview analysis logic
│   ├── resume_analysis.py        # Resume analysis logic
│   ├── utils.py                 # Utility functions
│   ├── requirements.txt         # Backend dependencies
│
├── frontend/
│   ├── node_modules/            # Node.js dependencies
│   ├── public/
│   │   ├── favicon.ico           # Favicon for the app
│   │   ├── index.html            # HTML template
│   │   ├── manifest.json         # Web app manifest
│   └── src/
│       ├── components/
│       │   ├── AnalysisResults.js # Display analysis results
│       │   ├── FileUpload.js      # File upload component
│       │   ├── InterviewAnalysis.js # Interview analysis UI
│       │   ├── ResumeAnalysis.js   # Resume analysis UI
│       ├── App.js                 # Main App component
│       ├── index.js               # React entry point
│       ├── index.css              # Global CSS styles
│       └── tailwind.config.js      # Tailwind CSS configuration

