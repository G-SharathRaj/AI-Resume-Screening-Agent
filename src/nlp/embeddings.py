from sentence_transformers import SentenceTransformer

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """
    Generate embedding for input text.
    """
    return model.encode(text, convert_to_numpy=True)