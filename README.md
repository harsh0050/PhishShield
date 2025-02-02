# Basic Idea and Workflow 
Phishing Email Detection & URL threat Analysis System

This project uses a fine tuned NLP model for phishing email identification and integrates the VirusTotal REST API for real-time threat analysis. Combining NLP and cybersecurity tools, it offers an intelligent and automated approach to detecting malicious emails.
Project Overview

1. Phishing Email Detection
2. It constitutes of a finetuned NLP Model with GOOGLE BERT as base model. It analyzes email content and classifies it as phishing or legitimate based on contextual patterns.
3. VirusTotal API for Threat-Intelligence - This validates URL from VirusTotal's global threat database for malware, phishing domains, etc.
4. End-to-End Security Workf>ow - Th>s is an intuitive, interactive platform that identifies phishing emails and gives users in-depth threat reports.
Technology Stack

- Frontend: React.js, HTML, CSS, JavaScript - It ensures the UI is responsive and intuitive.
- Backend: Python -Interact with APIs and execute phishing detection models.
- Machine Learning: Google BERT - It was fine-tuned for phishing detection using real-world datasets.
- Security API: VirusTotal REST API - Provides real-time threat intelligence for both URLs and files.

How It Works

1. User Input - User uploads an email (.eml file) or pastes its content and clicks on analyze.
2. BERT Model Analysis - The system processes the content of the email and predicts whether it is a phishing email.
3. URL Scanning - Scan URLs with VirusTotal's API.

- AI-Driven Phishing Detection - Highly advanced NLP techniques for accurate categorization.
- Real-Time Threat Analysis - Instant malware detection through VirusTotal integration.
- User-Friendly Interface - Built with React.js for smooth interaction.
- Improved Email Security - Phishing detection and risk assessment.
This project enhances email security by integrating the latest AI and real-time threat intelligence to help its users find potential cyber threats before they can happen.




# Instruction for setup
<h3>Software Requirements:</h3>

- Python 3
- Node JS
- npm

<h3>Setup & Running the Backend</h3>

Install dependencies:
```
pip install -r requirements.txt
```
Run the API server:
```
python restapi.py
```

<h3>Setup & Running the Frontend</h3>

Navigate to the react-app directory:
```
cd react-app
```
Install dependencies:
```
npm install
```
Start the React development server:
```
npm run dev
```
