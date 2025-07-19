# Basic Idea and Workflow 
Phishing Email Detection & URL threat Analysis System

This project uses a fine tuned NLP model for phishing email identification and integrates the VirusTotal REST API for real-time threat analysis. Combining NLP and cybersecurity tools, it offers an intelligent and automated approach to detecting malicious emails.
Project Overview

1. Phishing Email Detection
2. It constitutes of a finetuned NLP Model with GOOGLE BERT as base model. It analyzes email content and classifies it as phishing or legitimate based on contextual patterns.
3. End-to-End Security Workflow - This is an intuitive, interactive platform that identifies phishing emails and gives users in-depth threat reports.
Technology Stack

How does the Phishing URL Detection work:
The system loads the given URL using a webdriver in the server, It takes the screenshot of the site and extracts the text from the site. It then compares that site content with other common target sites' (The legitimate site of which the phishing site is a copy of) content. If the content of the suspect site matches the content of any of the target sites above a certain level, then the suspect site is declared to be Phishing site.

- Frontend: React.js, HTML, CSS, JavaScript - It ensures the UI is responsive and intuitive.
- Backend: Python -Interact with APIs and execute phishing detection models.
- Machine Learning: Google BERT - It was fine-tuned for phishing detection using real-world datasets.

How It Works

1. User Input - User uploads an email (.eml file) or pastes its content and clicks on analyze.
2. BERT Model Analysis - The system processes the content of the email and predicts whether it is a phishing email.

- AI-Driven Phishing Detection - Highly advanced NLP techniques for accurate categorization.
- Real-Time Threat Analysis - Instant malware detection through VirusTotal integration.
- User-Friendly Interface - Built with React.js for smooth interaction.
- Improved Email Security - Phishing detection and risk assessment.
This project enhances email security by integrating the latest AI and real-time threat intelligence to help its users find potential cyber threats before they can happen.


**To run the project, check out [this](https://github.com/harsh0050/Phishshield-VM) repository.**
