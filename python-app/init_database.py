from dotenv import load_dotenv

load_dotenv()
from app.db import db
from app.services import webhelper

legit_sites = [
    "https://accounts.google.com",
    "https://www.facebook.com/login/",
    "https://www.instagram.com/accounts/login/",
    "https://github.com/login",
    "https://login.microsoftonline.com",
    "https://login.yahoo.com",
    "https://www.linkedin.com/login",
    "https://appleid.apple.com",
    "https://www.paypal.com/signin",
    "https://www.netflix.com/login",
    "https://www.amazon.com/ap/signin",
    "https://www.dropbox.com/login",
    "https://zoom.us/signin",
    "https://slack.com/signin",
    "https://accounts.snapchat.com/accounts/login",
    "https://mail.proton.me/login",
    "https://login.aol.com",
    "https://www.office.com/login",
    "https://trello.com/login",
    "https://auth.wetransfer.com/login",
    "https://account.docusign.com",
    "https://mydhl.express.dhl",
    "https://www.bankofamerica.com/online-banking/sign-in/",
    "https://secure01a.chase.com/web/auth/#/logon/logon/chaseOnline"
]

for legit_site_url in legit_sites:
    if db.is_recorded(legit_site_url):
        print("site data already recorded. skipping it.")
        continue
    data = webhelper.get_text_from_url(legit_site_url)
    if 'text' in data:
        print("inserting...")
        db.insert_legit_site_data(site_url=legit_site_url, content=data['text'])
