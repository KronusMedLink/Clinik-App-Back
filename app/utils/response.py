from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def success_response(data, status_code=200):
    return JSONResponse(content=jsonable_encoder(data), status_code=status_code)

def error_response(message, status_code=400):
    return JSONResponse(content={"error": message}, status_code=status_code)
