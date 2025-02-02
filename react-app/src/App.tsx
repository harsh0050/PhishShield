import React from 'react';
import { Shield } from 'lucide-react';
import EmailAnalyzer from './components/EmailAnalyzer';
import URLScanner from './components/URLScanner';
import ThreatMap from './components/ThreatMap';

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center gap-2">
            <Shield className="w-8 h-8 text-blue-600" />
            <h1 className="text-2xl font-bold text-gray-900">PhishShield AI</h1>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <EmailAnalyzer />
          <URLScanner />
        </div>

        {/* <div className="mt-8">
          <ThreatMap />
        </div> */}
      </main>
    </div>
  );
}

export default App;