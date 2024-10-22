import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/{uid}")
async def root(uid: int):
    await asyncio.sleep(1)
    return {"uid": uid}


if __name__ == '__main__':
    uvicorn.run(
        app='server:app',
        host='0.0.0.0',
        port=3111,
        reload=False,
        workers=8
    )