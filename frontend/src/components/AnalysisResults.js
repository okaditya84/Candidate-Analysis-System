import React from 'react';

const AnalysisResults = ({ results, type }) => {
  const getScoreColor = (score) => {
    if (score >= 80) return 'text-green-600';
    if (score >= 60) return 'text-yellow-500';
    return 'text-red-500';
  };

  return (
    <div className="bg-white shadow-lg p-6 rounded-lg border border-gray-200">
      <h3 className="text-2xl font-semibold text-gray-800 mb-4">Analysis Results</h3>
      <div className="mb-4">
        <strong className="block text-lg text-gray-700 mb-2">Summary:</strong>
        <p className="text-gray-600">{results.Summary || 'No summary available.'}</p>
      </div>

      {type === 'resume' && (
        <div className="mb-4">
          <strong className="block text-lg text-gray-700 mb-2">Correctness Score:</strong>
          <span className={`text-xl font-semibold ${getScoreColor(results.Correctness || 0)}`}>
            {results.Correctness || 0}/100
          </span>
        </div>
      )}

      {type === 'interview' && (
        <div className="mb-4">
          <strong className="block text-lg text-gray-700 mb-2">Communication Score:</strong>
          <span className={`text-xl font-semibold ${getScoreColor(results.Communication || 0)}`}>
            {results.Communication || 0}/100
          </span>
        </div>
      )}

      <div className="mb-4">
        <strong className="block text-lg text-gray-700 mb-2">Strengths:</strong>
        <ul className="list-disc pl-5 space-y-2 text-gray-600">
          {(results.Strengths || []).map((strength, index) => (
            <li key={index}>{strength}</li>
          ))}
        </ul>
      </div>

      <div className="mb-4">
        <strong className="block text-lg text-gray-700 mb-2">Areas for Improvement:</strong>
        <ul className="list-disc pl-5 space-y-2 text-gray-600">
          {(results.Improvement || []).map((improvement, index) => (
            <li key={index}>{improvement}</li>
          ))}
        </ul>
      </div>

      <div>
        <strong className="block text-lg text-gray-700 mb-2">Recommendation:</strong>
        <p className="text-gray-600">{results.Overall || 'No recommendation available.'}</p>
      </div>
    </div>
  );
};

export default AnalysisResults;
