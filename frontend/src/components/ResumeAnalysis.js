import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './FileUpload';
import AnalysisResults from './AnalysisResults';

const ResumeAnalysis = () => {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('resume', file);
    formData.append('job_description', jobDescription);

    try {
      const response = await axios.post('http://localhost:5000/analyze_resume', formData);
      setAnalysis(response.data);
    } catch (error) {
      console.error('Error analyzing resume:', error);
      setError('An error occurred while analyzing the resume. Please try again.');
    }

    setLoading(false);
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Resume Analysis</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <FileUpload 
          accept=".pdf,.docx" 
          onChange={setFile} 
          label="Upload Resume (PDF or DOCX)" 
        />
        <div className="mb-4">
          <label className="block mb-2">Job Description:</label>
          <textarea
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            className="w-full p-2 border rounded"
            rows="4"
            required
          />
        </div>
        <button 
          type="submit" 
          className="bg-blue-500 text-white px-4 py-2 rounded" 
          disabled={loading || !file}
        >
          {loading ? 'Analyzing...' : 'Analyze Resume'}
        </button>
      </form>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      {analysis && <AnalysisResults results={analysis} type="resume" />}
    </div>
  );
};

export default ResumeAnalysis;