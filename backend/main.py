from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from confluence_api import ConfluenceAPI
from chroma_db import ChromaDB
from groq_api import GroqAPI

app = FastAPI()

confluence_api = ConfluenceAPI()
chroma_db = ChromaDB()
groq_api = GroqAPI()

class Query(BaseModel):
    text: str

@app.post("/query")
async def process_query(query: Query):
    try:
        # Convert query to embedding
        embedding = openai_api.get_embedding(query.text)
        
        # Perform semantic search
        search_results = chroma_db.search(embedding)
        
        # Extract the actual content from the search results
        relevant_docs = [result['document'] for result in search_results['documents'][0]]
        
        # Generate AI response
        context = "\n".join(relevant_docs)
        response = openai_api.generate_response(query.text, context)
        
        return {"response": response}
    except Exception as e:
        print(f"Error processing query: {str(e)}")  # Log the error
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/update_confluence_data")
async def update_confluence_data():
    try:
        # Fetch new data from Confluence
        new_data = confluence_api.fetch_new_data()
        
        # Update ChromaDB
        chroma_db.update_data(new_data)
        
        return {"message": "Data updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
