import React, { useEffect, useRef } from 'react';
import { Globe2 } from 'lucide-react';

const SAMPLE_THREATS = [
  { lat: 40.7128, lng: -74.0060, type: 'phishing' },
  { lat: 51.5074, lng: -0.1278, type: 'malware' },
  { lat: 35.6762, lng: 139.6503, type: 'scam' },
  { lat: 1.3521, lng: 103.8198, type: 'phishing' },
];

export default function ThreatMap() {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center gap-2 mb-4">
        <Globe2 className="w-5 h-5 text-green-600" />
        <h2 className="text-xl font-semibold">Global Threat Map</h2>
      </div>

      <div className="relative h-[400px] bg-gray-100 rounded-lg overflow-hidden">
        <img
          src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80"
          alt="World Map"
          className="absolute inset-0 w-full h-full object-cover opacity-50"
        />
        
        {SAMPLE_THREATS.map((threat, index) => (
          <div
            key={index}
            className="absolute w-3 h-3 rounded-full animate-ping"
            style={{
              backgroundColor: threat.type === 'phishing' ? '#ef4444' : 
                             threat.type === 'malware' ? '#8b5cf6' : '#f59e0b',
              left: `${((threat.lng + 180) / 360) * 100}%`,
              top: `${((90 - threat.lat) / 180) * 100}%`,
            }}
          />
        ))}
      </div>

      <div className="mt-4 flex gap-4 text-sm">
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-red-500" />
          <span>Phishing</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-purple-500" />
          <span>Malware</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-amber-500" />
          <span>Scam</span>
        </div>
      </div>
    </div>
  );
}