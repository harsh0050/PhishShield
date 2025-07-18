import os
from pymongo import MongoClient

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
mongo_uri = f"mongodb://{user}:{password}@{host}:{port}/"
db_client = MongoClient(mongo_uri)
db = db_client["phishshield"]
collection_name = "website_contents"


def insert_legit_site_data(site_url: str, content: str):
    db[collection_name].insert_one({
        '_id': site_url,
        'site_url': site_url,
        'content': content
    })


def is_recorded(url: str) -> bool:
    return db[collection_name].count_documents({
        '_id': url
    }) == 1


def get_legit_sites_data() -> list[dict[str, str]]:
    cursor = db[collection_name].find()
    ls = list()
    for doc in cursor:
        data = {
            "site_url": doc["site_url"],
            "content": doc["content"]
        }
        ls.append(data)
    return ls
