from flask import Blueprint, request, jsonify
from app.services import webhelper
from app.db import db
from app.services import gemini_util
from app.utils import get_tld

url_bp = Blueprint(name="url_bp", import_name=__name__)


@url_bp.route('/check_url', methods=['GET'])
def check_url():
    # Get the URL from query parameters
    # print("received request")
    url_to_check = request.args.get('url')

    if not url_to_check:
        return jsonify({"error": "URL query parameter is required"}), 400
    data = webhelper.get_text_from_url(url=url_to_check)
    if 'error' in data:
        return jsonify({"error": data['error']}), 500

    domain = get_tld(url=url_to_check)
    text_content = data['text']
    legit_sites_data = db.get_legit_sites_data()
    for site_data in legit_sites_data:
        this_tld = get_tld(site_data["site_url"])
        if domain == this_tld:
            print("returning result")
            return jsonify({"url": url_to_check, "phishing_status": "not phishing"}), 200

        score = gemini_util.get_match_score(legit_site_content=site_data['content'], sus_site_content=text_content)
        if score > 70 and domain != get_tld(site_data['site_url']):
            print("returning result")
            return jsonify({"url": url_to_check, "phishing_status": "phishing"}), 200
    print("returning result")
    return jsonify({"url": url_to_check, "phishing_status": "not phishing"}), 200


