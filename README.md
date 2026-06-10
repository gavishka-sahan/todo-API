# Todo API, CI/CD Pipeline Project

A Python FastAPI Todo REST API with a full end-to-end CI/CD pipeline using GitHub Actions, Docker, and GitHub Container Registry.

---

## Tech Stack

| Layer | Technology |
|---|---|
| App | Python, FastAPI |
| Testing | pytest, httpx |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Registry | GitHub Container Registry (ghcr.io) |
| Server | OVH VPS (Ubuntu 22.04) |

---

## Pipeline Architecture

```
git push 
    GitHub Actions
        Run tests (pytest)
        Build Docker image
        Push to ghcr.io
        SSH into VPS
            Pull latest image
            Stop old container
            Run new container
```

Every push to `main` automatically tests, builds, and deploys the app.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/todos` | Get all todos |
| GET | `/todos/{id}` | Get a single todo |
| POST | `/todos` | Create a todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

---

## Running Locally

### Prerequisites
- Python 3.11+
- Docker

### Run with Python

```bash
git clone https://github.com/gavishka-sahan/todo-API.git
cd todo-API
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Run with Docker

```bash
docker pull ghcr.io/gavishka-sahan/todo-api:latest
docker run -p 8000:8000 ghcr.io/gavishka-sahan/todo-api:latest
```

Visit `http://localhost:8000/docs` for the interactive API documentation.

---

## Running Tests

```bash
pytest -v
```

---

## Example Usage

```bash
# Health check
curl http://localhost:8000/health

# Create a todo
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'

# Get all todos
curl http://localhost:8000/todos

# Mark as completed
curl -X PUT http://localhost:8000/todos/{id} \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete a todo
curl -X DELETE http://localhost:8000/todos/{id}
```

---

## Project Structure

```
todo-API/
    main.py               # FastAPI application
    test_main.py          # pytest test suite
    Dockerfile            # Container definition
    requirements.txt      # Python dependencies
    .github/
        workflows/
            ci.yml        # GitHub Actions pipeline

```

---

## What Learned

- Building REST APIs with FastAPI and Pydantic
- Writing automated tests with pytest and httpx
- Containerizing applications with Docker
- Setting up CI/CD pipelines with GitHub Actions
- Pushing and pulling images from GitHub Container Registry
- Deploying to a live VPS via automated SSH
