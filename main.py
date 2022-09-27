import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests import post

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://itgeeky.github.io/portfolio-eng/",
    "https://itgeeky.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/port_lead", tags=["LEADS"])
def post_lead(data:str):
    datos = json.loads(data)
    headers = {'Content-Type': 'application/json'}
    response = post ('https://form-leads-84252-default-rtdb.firebaseio.com/leads.json',data= json.dumps(datos), headers=headers)
    if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error al enviar datos")
    return 'ok'
