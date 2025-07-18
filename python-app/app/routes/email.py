from flask import Blueprint, request, jsonify
from transformers import pipeline

from app.services import email_analyser
from app.utils import extract_email_file_content

# pipe = pipeline("text-classification", model="Shubh0904/autotrain-ot52s-j6gen", truncation=True)

email_bp = Blueprint(name="email_bp", import_name=__name__)


@email_bp.route('/email', methods=['POST'])
def email_endpoint():
    data = request.get_json()
    email_text = data.get('email-text') if data else None
    if not email_text:
        return jsonify({'error': 'Missing email-text in body'}), 400
    return email_analyser.analyse_raw_email(email_text)


@email_bp.route('/emailFile', methods=['POST'])
def extract_email_body():
    try:
        # Read raw .eml content from request body
        eml_content = request.data
        if not eml_content:
            return jsonify({'error': 'Empty request body'}), 400

        extracted_text = extract_email_file_content(eml_content)
        return jsonify(email_analyser.analyse_raw_email(extracted_text)), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# def hi():
