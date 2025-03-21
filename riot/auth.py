import os
from dotenv import load_dotenv

load_dotenv()

def get_tokens():
    access_token = os.getenv("ACCESS_TOKEN")
    entitlements_token = os.getenv("ENTITLEMENTS_TOKEN")
    puuid = os.getenv("PUID")
    region = os.getenv("REGION")
    
    if not access_token or not entitlements_token or not puuid:
        raise ValueError("One or more tokens are missing from .env")

    return access_token, entitlements_token, puuid, region
