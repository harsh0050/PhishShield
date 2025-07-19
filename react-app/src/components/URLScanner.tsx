import React, { useState } from 'react';
import { Globe, Shield } from 'lucide-react';

export default function URLScanner() {
  const [url, setUrl] = useState('');
  const [isScanning, setIsScanning] = useState(false);
  const [scanResult, setScanResult] = useState<{
    status: string;
    lastSeen?: string;
    registration?: string;
  } | null>(null);

  const handleScan = async () => {
    setIsScanning(true);
    // Simulate scanning
    // await new Promise(resolve => setTimeout(resolve, 2000));
    


    // Simulate scanning
    let url = document.getElementById("urlScan")?.value;
    // console.log("emailTxt = " + emailTxt);
    // try {
    // console.log(url);
    let reqUrl = 'http://192.168.33.10:5000/check_url?url='+url;
    const response = await fetch( reqUrl , {  // Replace with your server's URL
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },  // Sending the email entered by the user
    });

    if (!response.ok) {
      throw new Error('Failed to analyze email. Please try again.');
    }

    const data = await response.json();
    console.log(data.phishing_status);
    setScanResult({
      status: data.phishing_status == "phishing" ? "Phishing" : "Safe",
      lastSeen: '2024-03-15',
      registration: '2023-12-01',
    });
    setIsScanning(false);
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center gap-2 mb-4">
        <Globe className="w-5 h-5 text-purple-600" />
        <h2 className="text-xl font-semibold">URL Scanner</h2>
      </div>

      <div className="space-y-4">
        <div className="flex gap-2">
          <input
            type="url"
            className="flex-1 p-3 border rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            placeholder="Enter URL to scan..."
            id="urlScan"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button
            className={`px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors ${
              isScanning ? 'opacity-75 cursor-not-allowed' : ''
            }`}
            onClick={handleScan}
            disabled={isScanning || !url}
          >
            {isScanning ? 'Scanning...' : 'Scan'}
          </button>
        </div>

        {scanResult && (
          <div className="border rounded-lg p-4">
            <div className="flex items-center gap-2 mb-3">
              <Shield className={`w-5 h-5 ${
                scanResult.status == "Phishing" ? 'text-red-500' : 'text-green-500'
              }`} />
              <span className="font-medium">Threat status: {scanResult.status}</span>
            </div>
            
          </div>
        )}
      </div>
    </div>
  );
}