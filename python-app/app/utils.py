from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
import io
from tldextract import extract
from typing_extensions import Buffer


def extract_text_from_html(html_content: str):
    """Extract and clean text from HTML, replacing new lines with a space."""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator=" ", strip=True)  # Replace newlines with a space


def extract_email_file_content(email_content: Buffer) -> str:
    msg = BytesParser(policy=policy.default).parse(io.BytesIO(email_content))

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

    extracted_text = text_body.strip() if text_body else extract_text_from_html(
        html_body) if html_body else "No content"
    return extracted_text


def get_tld(url: str) -> str:
    extracted = extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    return domain
