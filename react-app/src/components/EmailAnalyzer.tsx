import React, { useState } from 'react';
import { Upload, AlertCircle, Mail } from 'lucide-react';


export default function EmailAnalyzer() {
  const [emailContent, setEmailContent] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [probability, setProbability] = useState<number | null>(null);

  const handleAnalyze = async (email) => {
    setIsAnalyzing(true);
    setIsAnalyzing(true);
    let emailTxt = document.getElementById("email-textarea")?.innerHTML;
    // console.log("emailTxt = " + emailTxt);
    // try {
    const response = await fetch('http://192.168.33.10:5000/email', {  // Replace with your server's URL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ "email-text": emailTxt }),  // Sending the email entered by the user
    });

    if (!response.ok) {
      throw new Error('Failed to analyze email. Please try again.');
    }

    const data = await response.json();
    // Assuming your API response has a `probability` field
    // Set the probability received from the server

    console.log(data.text);
    setProbability(parseFloat(data.probability));  // Save the full response for further display

    // } catch (err) {
    //   console.log("failed sending request\n" + err)  // If there’s an error, show it to the user
    // } finally {
    setIsAnalyzing(false);  // Stop loading state
    // }
  };

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = async (e) => {
        const response = await fetch('http://127.0.0.1:5000/emailFile', {  // Replace with your server's URL
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: e.target?.result,
        });

        if (!response.ok) {
          throw new Error('Failed to analyze email. Please try again.');
        }

        const data = await response.json();
        console.log(data.text);
        setProbability(parseFloat(data.probability));
        setIsAnalyzing(false);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center gap-2 mb-4">
        <Mail className="w-5 h-5 text-blue-600" />
        <h2 className="text-xl font-semibold">Email Analyzer</h2>
      </div>

      <div className="space-y-4">
        <div>
          <textarea
            id="email-textarea"
            className="w-full h-40 p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Paste email content here..."
            value={emailContent}
            onChange={(e) => setEmailContent(e.target.value)}
          />
        </div>

        <div className="flex items-center gap-4">
          <label className="flex items-center gap-2 px-4 py-2 bg-gray-100 rounded-lg cursor-pointer hover:bg-gray-200 transition-colors">
            <Upload className="w-4 h-4" />
            <span>Upload .eml</span>
            <input
              type="file"
              accept=".eml"
              className="hidden"
              onChange={handleFileUpload}
            />
          </label>

          <button
            className={`px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors ${isAnalyzing ? 'opacity-75 cursor-not-allowed' : ''
              }`}
            onClick={handleAnalyze}
            disabled={isAnalyzing || !emailContent}
          >
            {isAnalyzing ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>

        {probability !== null && (
          <div className={`p-4 rounded-lg flex items-center gap-3 ${probability > 0.7 ? 'bg-red-100' : probability > 0.4 ? 'bg-yellow-100' : 'bg-green-100'
            }`}>
            <AlertCircle className={`w-5 h-5 ${probability > 0.7 ? 'text-red-600' : probability > 0.4 ? 'text-yellow-600' : 'text-green-600'
              }`} />
            <div>
              <div className="font-medium">Phishing Probability: {(probability * 100).toFixed(1)}%</div>
              <div className="text-sm text-gray-600">
                {probability > 0.7 ? 'High Risk' : probability > 0.4 ? 'Medium Risk' : 'Low Risk'}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}