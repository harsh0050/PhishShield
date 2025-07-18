from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
load_dotenv()
from app.routes import email, url

app = Flask(__name__)
CORS(app, origins=["*"])

email_blueprint = email.email_bp
url_blueprint = url.url_bp

app.register_blueprint(email_blueprint)
app.register_blueprint(url_blueprint)


app.run(host="0.0.0.0", port=5000)


