import requests
import os
import json

API_BASE = "https://hsr-api.vercel.app/api"
CHAR_LIST_URL = f"{API_BASE}/characters"
OUTPUT_DIR = os.path.join("data", "characters")

def fetch_character_list():
    res = requests.get(CHAR_LIST_URL)
    res.raise_for_status()
    return res.json()["data"]

def fetch_character_detail(character_id):
    url = f"{API_BASE}/characters/{character_id}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()["data"]

def update_all_characters():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    char_list = fetch_character_list()
    print(f"共發現 {len(char_list)} 位角色，開始下載...")

    for char in char_list:
        char_id = char["id"]
        char_name = char["name"].replace(" ", "_")
        try:
            detail = fetch_character_detail(char_id)
            with open(os.path.join(OUTPUT_DIR, f"{char_name}.json"), "w", encoding="utf-8") as f:
                json.dump(detail, f, ensure_ascii=False, indent=2)
            print(f"✅ {char_name} 更新完成")
        except Exception as e:
            print(f"❌ {char_name} 更新失敗：{e}")

if __name__ == "__main__":
    update_all_characters()
