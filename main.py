from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.url

app = FastAPI()
app.include_router(routers.url.router)