import chromadb
from chromadb.config import Settings


CHROMA_SETTINGS = Settings(anonymized_telemetry=False)
CHROMA_CLIENT = chromadb.Client(CHROMA_SETTINGS)
COLLECTION_NAME = "book_versions"
COLLECTION = CHROMA_CLIENT.get_or_create_collection(name=COLLECTION_NAME)

def store_version(version_id, content):
    """
    Stores a new version of the content with a unique version_id.
    If the ID already exists, it is updated.
    """
    try:
        
        COLLECTION.delete(ids=[version_id])
    except:
        pass
    COLLECTION.add(documents=[content], ids=[version_id])

def retrieve_version(version_id):
    """
    Retrieve the content for a given version ID.
    """
    result = COLLECTION.get(ids=[version_id])
    if 'documents' in result and result['documents']:
        return result['documents'][0]
    return None

def load_all_versions():
    """
    Load all stored versions as a dictionary: {version_id: content}.
    """
    results = COLLECTION.get(include=["documents", "ids"])
    history = {id_: doc for id_, doc in zip(results['ids'], results['documents'])}
    return history
