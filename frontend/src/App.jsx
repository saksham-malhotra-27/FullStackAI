import React, { useEffect, useRef, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import axios from 'axios';

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [generatedContent, setGeneratedContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [fileId, setFileId] = useState(null);
  const [file, setFile] = useState(null);
  const refer = useRef(null);

  async function handleFileUpload() {
    if (!file) return;
    // can add react-toastify here 

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/upload', formData);
      setFileId(response.data[0].id);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  }

  async function run() {
    try {
      setGeneratedContent('');
      setLoading(true);

      const response = await axios.post('/ask', {
        id: fileId,
        question: prompt,
      });
      
      if(response.data[0].success==true){
       setGeneratedContent(String(response.data[0].answer.text));  // Adjust the key based on your response structure
      }
      else{
        console.error('Error occurred while generating content:');
      }
      
    } catch (error) {
      console.error('Error occurred while generating content:', error);
      setGeneratedContent('Error occurred while generating content.');
    } finally {
      setLoading(false);
    }
  }

  const handleInputChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleGenerateClick = () => {
    if (prompt.trim() !== '') {
      run();
    }
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  return (
    <div className="min-h-screen text-white bg-black flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-lg">
        {!fileId ? (
          <div className="flex flex-col items-center gap-4">
            <h2 className="text-white text-4xl font-semibold">Upload File:</h2>
            <div className='flex flex-col gap-2'>
              <input className="text-center" type="file" onChange={handleFileChange} />
              <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={handleFileUpload}>Upload</button>
            </div>
          </div>
        ) : (
          <>
            <label>
              <h2 className="text-white">Enter Prompt:</h2>
              <textarea
                className="bg-black text-whitesmoke rounded p-2 w-full min-h-[10vh]"
                value={prompt}
                onChange={handleInputChange}
              />
            </label>
            <button className="bg-blue-500 text-white px-4 py-2 mt-2 rounded" onClick={handleGenerateClick}>Generate Content</button>
          </>
        )}
      </div>

      {fileId && (
        <div className="w-full max-w-lg mt-4">
          <strong className="text-white">Generated Content:</strong>
          {loading && <p>Wait</p>}
          <div  className="bg-gray-800 text-white p-4 rounded">
            {generatedContent}
          </div>
        </div>
      )}
    </div>
  );
}
