import requests

def fetch_store(access_token, entitlements_token, puuid, region):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Riot-Entitlements-JWT": entitlements_token,
        "X-Riot-ClientVersion": "release-10.05-shipping-11-3345198",
        "X-Riot-ClientPlatform": "ewogICJwbGF0Zm9ybU5hbWUiOiAiV2luZG93cyIsCiAgInBsYXRmb3JtVmVyc2lvbiI6ICIxMC4wLjE1MDYzLjAiLAogICJhcmNoaXRlY3R1cmUiOiAieDY0Igp9",
        "User-Agent": "ShooterGame/10 Windows/10.0.19042.1.256.64bit",
        "Content-Type": "application/json"
    }

    url = f"https://pd.{region}.a.pvp.net/store/v2/storefront/{puuid}"
    print("📦 Requesting store with the following:")
    print("URL:", url)
    print("HEADERS:", headers)

    res = requests.get(url, headers=headers)
    try:
        data = res.json()
        if "SkinsPanelLayout" in data:
            return data["SkinsPanelLayout"]["SingleItemOffers"]
        else:
            print("Failed to retrieve store items.")
            print(data)
            return []
    except Exception as e:
        print("Error parsing response:", e)
        print(res.text)
        return []
