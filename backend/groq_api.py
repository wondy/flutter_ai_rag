import groq

class GroqAPI:
    def __init__(self):
        self.client = groq.Client(api_key="your-groq-api-key")

    def get_embedding(self, text):
        response = self.client.embeddings.create(
            model="mixtral-8x7b-32768",
            input=text
        )
        return response.data[0].embedding

    def generate_response(self, query, context):
        response = self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
            ]
        )
        return response.choices[0].message.content
