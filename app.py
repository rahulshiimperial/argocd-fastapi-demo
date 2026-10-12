from fastapi import FastAPI

app = FastAPI(title="Argo CD Demo")

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI on Kubernetes!",
        "deployed_by": "Argo CD"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}