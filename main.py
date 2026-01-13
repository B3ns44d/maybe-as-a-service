from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import json
import random
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Maybe-as-a-Service",
    description="A delightfully ambiguous decision-making API for the commitment-phobic",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_responses():
    try:
        with open("responses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

responses_data = load_responses()

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint with API information"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Maybe-as-a-Service</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .ascii-art { font-family: monospace; white-space: pre; color: #666; }
            .endpoint { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
            .example { background: #e8f4f8; padding: 10px; margin: 10px 0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="ascii-art">
  __  __             _          
 |  \\/  |           | |         
 | \\  / | __ _ _   _| |__   ___ 
 | |\\/| |/ _` | | | | '_ \\ / _ \\
 | |  | | (_| | |_| | |_) |  __/
 |_|  |_|\\__,_|\\__, |_.__/ \\___|
                __/ |           
               |___/            
    as-a-Service
        </div>
        <h1>Maybe-as-a-Service</h1>
        <p><em>Commitment issues? There's an API for that.</em></p>
        
        <h2>Available Endpoints</h2>
        <div class="endpoint"><strong>GET /maybe</strong> - Get a random maybe response</div>
        <div class="endpoint"><strong>GET /maybe/random</strong> - Alias for /maybe</div>
        <div class="endpoint"><strong>GET /maybe/{id}</strong> - Get a specific response by ID</div>
        <div class="endpoint"><strong>GET /maybe/category/{category}</strong> - Filter by category</div>
        <div class="endpoint"><strong>GET /health</strong> - Health check</div>
        
        <h2>Example Usage</h2>
        <div class="example">
            <code>curl https://maybe-as-a-service.fly.dev/maybe</code><br>
            Returns: <code>{"response": "Maybe yes, maybe no, maybe I'll decide tomorrow.", "id": 7, "category": "philosophical"}</code>
        </div>
        
        <p><a href="/docs">Interactive API Documentation</a></p>
        <p><a href="https://github.com/B3ns44d/maybe-as-a-service">GitHub Repository</a></p>
    </body>
    </html>
    """
    return html_content

@app.get("/maybe")
async def get_maybe():
    """Get a random maybe response"""
    if not responses_data:
        raise HTTPException(status_code=500, detail="No responses available")
    
    response = random.choice(responses_data)
    return response

@app.get("/maybe/random")
async def get_maybe_random():
    """Alias for /maybe - get a random maybe response"""
    return await get_maybe()

@app.get("/maybe/{response_id}")
async def get_maybe_by_id(response_id: int):
    """Get a specific maybe response by ID"""
    response = next((r for r in responses_data if r["id"] == response_id), None)
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    return response

@app.get("/maybe/category/{category}")
async def get_maybe_by_category(category: str):
    """Get a random maybe response from a specific category"""
    category_responses = [r for r in responses_data if r["category"].lower() == category.lower()]
    if not category_responses:
        raise HTTPException(status_code=404, detail=f"No responses found for category: {category}")
    
    return random.choice(category_responses)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "maybe"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
