from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi import FastAPI
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

print(settings.database_username)

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") 
def dowolna_nazwa():
    return {"message":"hello siemanko"}




    


        