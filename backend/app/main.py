from fastapi import FastAPI
from app.api import enka, characters, stages, simulate

app = FastAPI(title="星鐵隊伍模擬器 API")

app.include_router(enka.router, prefix="/enka")
app.include_router(characters.router, prefix="/characters")
app.include_router(stages.router, prefix="/stages")
app.include_router(simulate.router, prefix="/simulate")

@app.get("/")
async def root():
    return {"message": "Hello from HSR Team Tool API"}
