from fastapi import FastAPI
from main_and_final_chunking import fixed_size_chunking  # Import the function

app = FastAPI()  # Create an instance of the FastAPI app

@app.get("/fixed_size_chunking/")
async def process_fixed_size_chunking(text: str, chunk_size: int):
    result = fixed_size_chunking(text, chunk_size)  # Call the fixed_size_chunking function
    return {"result": result}  # Return the result in a JSON format
