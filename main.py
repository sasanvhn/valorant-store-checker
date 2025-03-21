from dotenv import load_dotenv
import os
import requests

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ENTITLEMENTS_TOKEN = os.getenv("ENTITLEMENTS_TOKEN")
PUID = os.getenv("PUID")
REGION = os.getenv("REGION")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Riot-Entitlements-JWT": ENTITLEMENTS_TOKEN,
    "X-Riot-ClientVersion": "release-10.05-shipping-11-3345198",
    "X-Riot-ClientPlatform": "ewogICJwbGF0Zm9ybU5hbWUiOiAiV2luZG93cyIsCiAgInBsYXRmb3JtVmVyc2lvbiI6ICIxMC4wLjE1MDYzLjAiLAogICJhcmNoaXRlY3R1cmUiOiAieDY0Igp9",
    "User-Agent": "ShooterGame/10 Windows/10.0.19042.1.256.64bit",
    "Content-Type": "application/json"
}

url = f"https://pd.{REGION}.a.pvp.net/store/v2/storefront/{PUID}"
print("📦 Requesting store with the following:")
print("URL:", url)
print("HEADERS:", headers)

res = requests.get(url, headers=headers)
try:
    data = res.json()
    if "SkinsPanelLayout" in data:
        skins = data["SkinsPanelLayout"]["SingleItemOffers"]
        print("✅ Skins:", skins)
    else:
        print("❌ Failed to retrieve store items.")
        print(data)
except Exception as e:
    print("❌ Error parsing response:", e)
    print(res.text)