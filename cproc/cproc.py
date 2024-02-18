from fastapi import Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .config import settings
from typing import List
from pydantic import BaseModel
from datetime import datetime
from .exceptions import GraphNotFoundException, CodeExecutionException
from fastapi import APIRouter

import aiohttp
import toml
import asyncio
import random
import time

class ServiceParameters(BaseModel):
    exception_types: List[str]
    numbers: int = 100

def get_service_info():
    with open('config.toml', 'r') as f:
        config = toml.load(f)
    return config['exceptions']['service_host'], config['exceptions']['service_port']

router = APIRouter()

errors = {'GraphNotFoundException': GraphNotFoundException, 'CodeExecutionException': CodeExecutionException}
service_host, service_port = get_service_info()
session = aiohttp.ClientSession()

@router.post("/api/v1/cproc/generate")
async def generate(error: ServiceParameters, response: Response):
    if settings.status:
        response.status_code = status.HTTP_409_CONFLICT
        error = jsonable_encoder({"error": "409 - process already started"})
        return JSONResponse(error)
    
    settings.status = True
    url = f"http://{service_host}:{service_port}"
    for i in range(error.numbers):
        if not(settings.status):
            break
        
        err = random.choice(error.exception_types)

        err_name = err.split('=')[0]
        err_id = err.split('=')[1]

        message = errors[err_name](err_id)
        
        date_time = datetime.fromtimestamp(time.time())
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

        err_struct = jsonable_encoder({"exception": err_name, "message": str(message), "timestamp": date_time})
        await session.post(url, json=err_struct)
        await asyncio.sleep(random.uniform(0.01, 0.5))
    settings.status = False

@router.get("/api/v1/cproc/status")
async def get_status():
    if settings.status:
        ans = jsonable_encoder({"status": "generating"})
    else:
        ans = jsonable_encoder({"status": "idle"})
    return JSONResponse(content=ans)

@router.post("/api/v1/cproc/stop")
async def stop():
    settings.status = False
    ans = jsonable_encoder({"status": "OK!"})
    return JSONResponse(ans)
