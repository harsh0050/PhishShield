export interface EmailAnalysisResult {
  probability: number;
  threats: string[];
  confidence: number;
}

export interface URLAnalysisResult {
  reputation: number;
  threats: string[];
  lastSeen?: string;
  registrationDate?: string;
}

export interface ThreatFeed {
  id: string;
  timestamp: string;
  type: 'phishing' | 'malware' | 'scam';
  source: string;
  target: string;
  location?: {
    lat: number;
    lng: number;
  };
}