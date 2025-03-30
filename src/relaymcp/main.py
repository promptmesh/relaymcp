from fastapi import FastAPI

app = FastAPI(
    title="RelayMCP",
    description="An OpenAPI-native, session-aware gateway that bridges REST APIs into the Model Context Protocol with full support for JSON-RPC, streaming, and dynamic backend configuration.",
)