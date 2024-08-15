from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.url

app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(routers.url.router)