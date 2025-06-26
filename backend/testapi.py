import httpx

uid = "800066701"
url = f"https://enka.network/api/hsr/uid/{uid}/"
headers = {
    "User-Agent": "Safari/537.36"
}

try:
    response = httpx.get(url, headers=headers, follow_redirects=True, timeout=10.0)

    if response.status_code == 200:
        data = response.json()
        detail = data.get("detailInfo", {})

        print("暱稱:", detail.get("nickname", "未知"))
        print("等級:", detail.get("level", "未知"))
        print("角色數量:", len(detail.get("avatarDetailList", [])))

        print("角色列表:")
        for avatar in detail.get("avatarDetailList", []):
            print(f" - Avatar ID: {avatar.get('avatarId')} 等級: {avatar.get('level')}")

    else:
        print("錯誤狀態碼:", response.status_code)
        print("錯誤內容:", response.text)

except Exception as e:
    print("請求失敗:", str(e))
