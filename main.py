from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import faiss
from typing import List
import together
from .fake_data import generate_profiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize TogetherAI
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env
together.api_key = os.getenv("TOGETHER_API_KEY")

class SearchRequest(BaseModel):
    text: str

class Profile(BaseModel):
    id: str
    name: str
    title: str
    skills: List[str]
    experience: str
    summary: str
    similarity: float = 0.0

# Initialize in-memory data
profiles = generate_profiles(100)  # Generate 100 fake profiles
profile_texts = [f"{p['title']} with skills in {', '.join(p['skills'])}. {p['summary']}" for p in profiles]

# Get embeddings and build FAISS index
embeddings_response = together.Embeddings.create(
    model="togethercomputer/m2-bert-80M-8k-retrieval",
    input=profile_texts
)
embeddings = [result['embedding'] for result in embeddings_response['data']]

dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype('float32'))

@app.post("/search")
async def search(request: SearchRequest):
    query_response = together.Embeddings.create(
        model="togethercomputer/m2-bert-80M-8k-retrieval",
        input=request.text
    )
    query_embedding = np.array(query_response['data'][0]['embedding']).astype('float32').reshape(1, -1)
    
    _, indices = index.search(query_embedding, 5)
    
    results = []
    for i in indices[0]:
        if i < len(profiles):
            profile = profiles[i]
            results.append(Profile(
                id=profile['id'],
                name=profile['name'],
                title=profile['title'],
                skills=profile['skills'],
                experience=profile['experience'],
                summary=profile['summary'],
                similarity=float(1 - (query_embedding[0] @ embeddings[i]) / 2)  # Convert to similarity score
            ))
    
    return {"results": results}

# temporary
@app.get("/test_key")
async def test_key():
    return {"key_set": bool(os.getenv("TOGETHER_API_KEY"))}