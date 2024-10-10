import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './FileUpload';
import AnalysisResults from './AnalysisResults';

const InterviewAnalysis = () => {
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
    formData.append('video', file);
    formData.append('job_description', jobDescription);

    try {
      const response = await axios.post('http://localhost:5000/analyze_interview', formData);
      setAnalysis(response.data);
    } catch (error) {
      console.error('Error analyzing interview:', error);
      setError('An error occurred while analyzing the interview. Please try again.');
    }

    setLoading(false);
  };

  return (
    <div className="bg-gray-50 p-8 shadow-md rounded-md">
      <h2 className="text-3xl font-bold text-gray-800 mb-6">Interview Analysis</h2>
      <form onSubmit={handleSubmit} className="space-y-6">
        <FileUpload 
          accept="video/*" 
          onChange={setFile} 
          label="Upload Interview Video" 
        />
        <div>
          <label className="block text-gray-700 mb-2">Job Description:</label>
          <textarea
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows="4"
            required
          />
        </div>
        <button 
          type="submit" 
          className="w-full bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition duration-300"
          disabled={loading || !file}
        >
          {loading ? 'Analyzing...' : 'Analyze Interview'}
        </button>
      </form>
      {error && <p className="text-red-500 mt-4">{error}</p>}
      {analysis && <AnalysisResults results={analysis} type="interview" />}
    </div>
  );
};

export default InterviewAnalysis;
