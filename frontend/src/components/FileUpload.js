import React from 'react';

const FileUpload = ({ accept, onChange, label }) => {
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    onChange(file);
  };

  return (
    <div>
      <label className="block text-gray-700 mb-2">{label}:</label>
      <input 
        type="file" 
        accept={accept} 
        onChange={handleFileChange} 
        className="w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        required 
      />
    </div>
  );
};

export default FileUpload;
