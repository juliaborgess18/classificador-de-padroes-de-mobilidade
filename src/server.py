from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

app = FastAPI()

origins = ['http://localhost:8000']  #Define a lista de origens permitidas para solicitações CORS.

# Permite que a aplicação aceite solicitações de diferentes origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# DataFrame global para armazenar os dados carregados do arquivo CSV
df_global = None

@app.post("/upload/")
async def carregar_dados_csv(file: UploadFile = File(...)):
    global df_global
    
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser um CSV")

    try:
        df = pd.read_csv(file.file)
        df_global = df  # Armazena o DataFrame globalmente
        return JSONResponse(content={"detail": "Arquivo CSV carregado com sucesso"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/resultado/")
async def resultado_processamento():
    global df_global
    
    if df_global is None:
        raise HTTPException(status_code=404, detail="Nenhum arquivo CSV foi carregado ainda")
    
    # Processamento dos dados
    # Neste exemplo, apenas retornaremos as primeiras linhas como JSON
    return JSONResponse(content=df_global.head().to_dict(orient="records"))
