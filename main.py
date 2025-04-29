from Server.server import server
import uvicorn
app = server.app


@app.get('/teste', tags=['Teste'])
def teste_rout():
    return {'result': 'ok, server funcionando'}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_level="info", host="0.0.0.0")