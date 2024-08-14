from fastapi import FastAPI
import routers.url

app = FastAPI()
app.include_router(routers.url.router)