from fastapi import FastAPI
from API.CRequest import app_request
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.include_router(
    router=app_request,
    prefix="/client",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def welcome():
    return {"message":"Welcome"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host='127.0.0.1',
        port=12345,
        reload=True,
        workers=14
    )