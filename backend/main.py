# from models.userModel import User
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from routes import auth, plot,allot,groups
from config import Settings

app=FastAPI()
settings = Settings()
origins=[
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.USE_NGROK:
    # pyngrok should only ever be installed or initialized in a dev environment when this flag is set
    from pyngrok import ngrok

    # Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
    # when starting the server
    port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 8000

    # Open a ngrok tunnel to the dev server
    public_url = ngrok.connect(port).public_url
    logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

    # Update any base URLs or webhooks to use the public ngrok URL
    settings.BASE_URL = public_url
    init_webhooks(public_url)

app.include_router(auth.authRoute)
app.include_router(plot.plotRoute)
app.include_router(allot.weightRoute)
app.include_router(groups.groupRoute)
