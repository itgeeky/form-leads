import json
from fastapi import FastAPI, HTTPException
from requests import post

app = FastAPI()

@app.post("/port_lead", tags=["LEADS"])
def post_lead(data:str):
    datos = json.loads(data)
    headers = {'Content-Type': 'application/json'}
    response = post ('https://form-leads-84252-default-rtdb.firebaseio.com/leads.json',data= json.dumps(datos), headers=headers)
    if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error al enviar datos")
    return 'ok'
