from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from relaymcp import routes

app = FastAPI(
    title="RelayMCP",
    description="An OpenAPI-native, session-aware gateway that bridges REST APIs into the Model Context Protocol with full support for JSON-RPC, streaming, and dynamic backend configuration.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)