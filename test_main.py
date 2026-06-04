from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_create_and_get_todo():
    r = client.post("/todos", json={"title": "Buy milk"})
    assert r.status_code == 201
    todo_id = r.json()["id"]

    r2 = client.get(f"/todos/{todo_id}")
    assert r2.json()["title"] == "Buy milk"

def test_update_todo():
    r = client.post("/todos", json={"title": "Do laundry"})
    todo_id = r.json()["id"]
    r2 = client.put(f"/todos/{todo_id}", json={"completed": True})
    assert r2.json()["completed"] == True

def test_delete_todo():
    r = client.post("/todos", json={"title": "Delete me"})
    todo_id = r.json()["id"]
    client.delete(f"/todos/{todo_id}")
    r2 = client.get(f"/todos/{todo_id}")
    assert r2.status_code == 404