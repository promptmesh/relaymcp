def main() -> None:
    import uvicorn
    uvicorn.run("relaymcp.main:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()