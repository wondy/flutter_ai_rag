import chromadb

class ChromaDB:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("confluence_data")

    def update_data(self, new_data):
        # Process and add new data to ChromaDB
        for item in new_data:
            self.collection.add(
                documents=[item['content']],
                metadatas=[{"title": item['title'], "id": item['id']}],
                ids=[item['id']]
            )

    def search(self, query_embedding):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )
        return results
