from riot.auth import get_tokens
from riot.store import fetch_store

try:
    access_token, entitlements_token, puuid, region = get_tokens()
    skins = fetch_store(access_token, entitlements_token, puuid, region)

    if skins:
        print("\n🎮 Your Store Skins Today:\n")
        for idx, skin_id in enumerate(skins, start=1):
            print(f"{idx}. Skin UUID: {skin_id}")
    else:
        print("No skins to display.")

except Exception as e:
    print("Error:", e)
