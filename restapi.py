from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS  # Import CORS
import requests

from email import policy
from email.parser import BytesParser
import io
from bs4 import BeautifulSoup

app = Flask(__name__)

CORS(app, origins=["http://localhost:5173"])

pipe = pipeline("text-classification", model="Shubh0904/autotrain-ot52s-j6gen", truncation=True)


@app.route('/email', methods=['POST'])
def email_endpoint():
    data = request.get_json()
    email_text = data.get('email-text') if data else None
    if not email_text:
        return jsonify({'error': 'Missing email-text in body'}), 400

    texts = [email_text]

    results = pipe(texts)
    result = results[0]
    print(result['label'].lower() == "safe email")
    if (result['label'].lower() == "safe email"):
        probabiltity = 1 - result['score']
    else:
        probabiltity = result['score']
    return jsonify({"probability": probabiltity, "text": result['label']})


def extract_text_from_html(html_content):
    """Extract and clean text from HTML, replacing new lines with a space."""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator=" ", strip=True)  # Replace newlines with a space


@app.route('/emailFile', methods=['POST'])
def extract_email_body():
    try:
        # Read raw .eml content from request body
        eml_content = request.data

        if not eml_content:
            return jsonify({'error': 'Empty request body'}), 400

        # Parse the email content
        msg = BytesParser(policy=policy.default).parse(io.BytesIO(eml_content))

        # Extract plain text or HTML if no plain text is found
        text_body = None
        html_body = None

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                charset = part.get_content_charset() or "utf-8"  # Default to utf-8 if None

                if content_type == "text/plain":
                    text_body = part.get_payload(decode=True).decode(charset, errors="ignore")
                elif content_type == "text/html":
                    html_body = part.get_payload(decode=True).decode(charset, errors="ignore")

        else:  # Single-part email
            charset = msg.get_content_charset() or "utf-8"
            content_type = msg.get_content_type()
            payload = msg.get_payload(decode=True).decode(charset, errors="ignore")

            if content_type == "text/plain":
                text_body = payload
            elif content_type == "text/html":
                html_body = payload

        # Use plain text if available, otherwise extract text from HTML
        extracted_text = text_body.strip() if text_body else extract_text_from_html(
            html_body) if html_body else "No content"

        texts = [extracted_text]

        results = pipe(texts)
        result = results[0]
        print(result['label'].lower() == "safe email")
        if (result['label'].lower() == "safe email"):
            probabiltity = 1 - result['score']
        else:
            probabiltity = result['score']
        return jsonify({"probability": probabiltity, "text": result['label']})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Function to check for "phishing" in the analysis results
def check_phishing(response_data):
    # Loop through the analysis results and check if any result is "phishing"
    for engine, result in response_data.get("data", {}).get("attributes", {}).get("last_analysis_results", {}).items():
        if result.get("result") == "phishing":
            return "phishing"
    return "not phishing"


@app.route('/check_url', methods=['GET'])
def check_urll():
    # Get the URL from query parameters
    url_to_check = request.args.get('url')

    if not url_to_check:
        return jsonify({"error": "URL query parameter is required"}), 400

    # First API request to VirusTotal
    vt_url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'x-apikey': '637663e3cf0801dd3624c459ee27d22bd236f0540e90a49de80a544a4e570699'
    }
    data = {
        'url': url_to_check
    }

    # Send POST request
    response = requests.post(vt_url, headers=headers, data=data)

    if response.status_code == 200:
        # Extract the ID from the response
        response_data = response.json()
        analysis_id = response_data["data"]["id"]
        base64_id = analysis_id.split("-")[1]  # The base64 part of the ID

        # Second API request to get the detailed analysis
        get_url = f"https://www.virustotal.com/api/v3/urls/{base64_id}"
        get_response = requests.get(get_url, headers=headers)

        if get_response.status_code == 200:
            # Check if the result is phishing
            phishing_status = check_phishing(get_response.json())
            return jsonify({"url": url_to_check, "phishing_status": phishing_status}), 200
        else:
            return jsonify({"error": "Failed to retrieve analysis details", "details": get_response.text}), 500
    else:
        return jsonify({"error": "Failed to analyze URL", "details": response.text}), 500


def check_phishing(response_data):
    # Loop through the analysis results and check if any result is "phishing"
    for engine, result in response_data.get("data", {}).get("attributes", {}).get("last_analysis_results", {}).items():
        if result.get("result") == "phishing":
            return "phishing"
    return "not phishing"


@app.route('/check_url', methods=['GET'])
def check_url():
    # Get the URL from query parameters
    url_to_check = request.args.get('url')

    if not url_to_check:
        return jsonify({"error": "URL query parameter is required"}), 400

    # First API request to VirusTotal
    vt_url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'x-apikey': '637663e3cf0801dd3624c459ee27d22bd236f0540e90a49de80a544a4e570699'
    }
    data = {
        'url': url_to_check
    }

    # Send POST request
    response = requests.post(vt_url, headers=headers, data=data)

    if response.status_code == 200:
        # Extract the ID from the response
        response_data = response.json()
        analysis_id = response_data["data"]["id"]
        base64_id = analysis_id.split("-")[1]  # The base64 part of the ID

        # Second API request to get the detailed analysis
        get_url = f"https://www.virustotal.com/api/v3/urls/{base64_id}"
        get_response = requests.get(get_url, headers=headers)

        if get_response.status_code == 200:
            # Check if the result is phishing
            phishing_status = check_phishing(get_response.json())
            return jsonify({"url": url_to_check, "phishing_status": phishing_status}), 200
        else:
            return jsonify({"error": "Failed to retrieve analysis details", "details": get_response.text}), 500
    else:
        return jsonify({"error": "Failed to analyze URL", "details": response.text}), 500


if __name__ == '__main__':
    app.run(debug=True)
