import React, { useState } from 'react';
import ResumeAnalysis from './components/ResumeAnalysis';
import InterviewAnalysis from './components/InterviewAnalysis';

function App() {
  const [activeTab, setActiveTab] = useState('resume');

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">Candidate Analysis System</h1>
      <div className="flex justify-center space-x-4 mb-6">
        <button
          className={`px-6 py-2 font-semibold rounded-lg transition-colors ${
            activeTab === 'resume' ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-800'
          }`}
          onClick={() => setActiveTab('resume')}
        >
          Resume Analysis
        </button>
        <button
          className={`px-6 py-2 font-semibold rounded-lg transition-colors ${
            activeTab === 'interview' ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-800'
          }`}
          onClick={() => setActiveTab('interview')}
        >
          Interview Analysis
        </button>
      </div>
      <div className="max-w-3xl mx-auto">
        {activeTab === 'resume' ? <ResumeAnalysis /> : <InterviewAnalysis />}
      </div>
    </div>
  );
}

export default App;
