from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import httpx
import json
import os

router = APIRouter()

ENKA_API_BASE = "https://enka.network/api/hsr/uid"


@router.get("/import/")
def import_data(uid: str = Query(..., description="你的星穹鐵道 UID")):
    url = f"{ENKA_API_BASE}/{uid}/"
    headers = {
        "User-Agent": "Safari/537.36"
    }

    try:
        response = httpx.get(url, headers=headers, follow_redirects=True, timeout=10.0)

        if response.status_code != 200:
            return JSONResponse(
                status_code=response.status_code,
                content={"error": "Enka API 回應錯誤", "status": response.status_code, "detail": response.text}
            )

        data = response.json()
        new_detail = data.get("detailInfo", {})
        new_list = new_detail.get("avatarDetailList", [])

        # 合併邏輯：保留舊資料，更新已有角色，加入新角色
        file_path = f"data/characters/{uid}.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            old_detail = old_data.get("detailInfo", {})
            old_list = old_detail.get("avatarDetailList", [])
        else:
            old_list = []

        # 將舊角色列表轉成 dict（以 avatarId 當 key）
        merged = {a["avatarId"]: a for a in old_list}

        # 更新 / 加入新角色資料
        for avatar in new_list:
            merged[avatar["avatarId"]] = avatar

        # 組成新的儲存結構
        new_data_to_save = {
            "detailInfo": {
                **new_detail,
                "avatarDetailList": list(merged.values())
            },
            "ttl": data.get("ttl"),
            "uid": data.get("uid")
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(new_data_to_save, f, ensure_ascii=False, indent=2)

        return {
            "uid": new_detail.get("uid"),
            "nickname": new_detail.get("nickname"),
            "level": new_detail.get("level"),
            "avatar_count": len(merged),
            "merged_avatar_ids": list(merged.keys())
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "無法連線 Enka API", "detail": str(e)}
        )
