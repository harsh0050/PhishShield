import os

from google import genai
from google.genai import types
import aiohttp
import asyncio

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
system_prompt = f"""
You are a cybersecurity AI designed to detect phishing and impersonation by analyzing the text content of two websites.
You will be given the text from:
Site A: A known legitimate website (the brand being potentially impersonated)
Site B: A suspected fraudulent or phishing website
Your task is to compare their textual content and determine if Site B is copying Site A with the intent to deceive users.
your main focus should be on the brand name, try to see if the brand name has been tweaked a bit to look like the legit site on the first site but it has slight variation
if the content of the websites prove that those websites are for completely different purposes, then that should favour in the website being not phishing
your final answer should only be the matching score between 0 to 100
only output the integer score, no text at all.
"""


def get_base_prompt(legit_site: str, sus_site: str) -> str:
    return f"""Compare the following two websites to determine if Site B is copying or mimicking Site A in a way that could indicate a phishing attempt.
    Site A (Legitimate Website): ${legit_site}
    Site B (Suspected Website): ${sus_site}
    """


def get_match_score(legit_site_content: str, sus_site_content: str) -> int:
    """
    Only this one works due to free-quota limitations
    """
    response = client.models.generate_content(
        model="models/gemini-2.0-flash-lite",
        config=types.GenerateContentConfig(
            # max_output_tokens=4096,
            temperature=0.6,
            system_instruction=system_prompt),
        contents=get_base_prompt(legit_site_content, sus_site_content)
    )
    try:
        return int(response.text)
    except ValueError as e:
        return -1


async def generate_content(model: str, api_key: str, base_prompt: str, system_prompt: str) -> str:
    """Send request to gemini using http asynchronously."""
    async with aiohttp.ClientSession(
            base_url=f"https://generativelanguage.googleapis.com/v1beta/{model}:generateContent/"
    ) as session:
        headers = {
            "x-goog-api-key": api_key,
            "Content-Type": "application/json"
        }
        data = {
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"parts": [{"text": base_prompt}]}]
        }
        async with session.post("", headers=headers, json=data) as response:
            json = await response.json()
            try:
                ans = json["candidates"][0]['content']['parts'][0]['text']
                return ans
            except Exception as e:
                print(json)


async def get_async_match_score(legit_site_content: str, sus_site_content: str, sus_site_url: str) -> dict[str, int]:
    """Doesn't work due to quota limit."""
    response = await generate_content(
        model="models/gemini-2.0-flash-lite",
        api_key=api_key,
        base_prompt=get_base_prompt(legit_site=legit_site_content, sus_site=sus_site_content),
        system_prompt=system_prompt
    )
    try:
        score = int(response)
    except ValueError as e:
        score = -1
    return {"score": score}


async def get_all_match_scores(legit_sites_content: list[str], sus_site_content: str, sus_site_url: str):
    tasks = [get_async_match_score(legit_content, sus_site_content, sus_site_url) for legit_content in
             legit_sites_content]
    results = await asyncio.gather(*tasks)
    for res in results:
        print(res)
