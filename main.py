from tortoise.contrib.fastapi import register_tortoise
from Server.server import server
import uvicorn
from models.models import Usuario
app = server.app


@app.post("/usuarios")
async def criar_usuario(user: str, senha: str):
    usuario = await Usuario.create(user=user, senha=senha)
    return {"id": usuario.id, "user name": usuario.user}

@app.get('/teste', tags=['Teste'])
def teste_rout():
    return {'result': 'ok, server funcionando'}

register_tortoise(
    app,
    db_url="jdbc:postgresql://localhost:5432/postgres",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_level="info", host="0.0.0.0")