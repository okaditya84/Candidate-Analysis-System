from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_analysis import analyze_resume
from interview_analysis import analyze_interview
from database import init_db, get_db
import json


app = Flask(__name__)
CORS(app)

init_db()

@app.route('/getroute',methods=['GET'])
def hello_world():
    return "Hello World"

@app.route('/analyze_resume', methods=['POST'])
def handle_resume_analysis():
    resume_file = request.files['resume']
    job_description = request.form['job_description']
    result = analyze_resume(resume_file, job_description)
    
    # Store result in database
    db = get_db()
    db.execute('INSERT INTO analyses (type, result) VALUES (?, ?)',
                ('resume', json.dumps(result)))
    db.commit()
    
    return jsonify(result)

@app.route('/analyze_interview', methods=['POST'])
def handle_interview_analysis():
    try:
        
        video_file = request.files['video']
        job_description = request.form['job_description']
        
        # Call the analysis function
        result = analyze_interview(video_file, job_description)
        
        
        # Store result in database
        db = get_db()
        db.execute('INSERT INTO analyses (type, result) VALUES (?, ?)',
                   ('interview', json.dumps(result)))
        db.commit()
        
        
        return jsonify(result), 200

    except Exception as e:
        app.logger.error(f"Error during interview analysis: {e}")
        return jsonify({
            "error": "An unexpected error occurred during the analysis.",
            "summary": "Analysis could not be completed due to an error.",
            "correctness_score": 0,
            "communication_score": 0,
            "strengths": [],
            "areas_for_improvement": [],
            "recommendation": "Unable to provide recommendation due to analysis error.",
            "keywords_matched": []
        }), 500

if __name__ == '__main__':
    app.run(debug=True)