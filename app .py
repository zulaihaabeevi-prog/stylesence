from fastapi import FastAPI,  Form
from fastapi.responses import JSONResponse
from backend.models import generate_advice
app = FastAPI()

@app.post("/recommend")
async def recommend_style(user_preferences: str = Form(...), file: UploadFile = None):
    advice = generate_advice(user_preferences)
    recommendations = {
        "outfits": ["Casual Denim Jacket + White Tee", "Formal Blazer + Slim Pants"],
        "trends": ["Oversized blazers", "Neutral tones"],
        "advice": advice
    }
    return JSONResponse(content=recommendations)
    if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
