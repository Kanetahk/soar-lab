from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from tasks import processar_alerta

app = FastAPI()

class SplunkWebhook(BaseModel):
    search_name: str
    result: dict[str, Any]

@app.post("/webhook")
async def receber_alerta(alerta: SplunkWebhook):
    processar_alerta.delay(alerta.search_name, alerta.result)
    return {"status": "received"}