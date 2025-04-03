from fastapi import APIRouter

router = APIRouter()

@router.post("/mcp")
async def mcp():
    return {"hello": "world"}