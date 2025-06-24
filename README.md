# keploy3


project/
├── app/
│   ├── main.py
│   ├── logic.py         
│   └── ...
├── tests/
│   ├── unit/
│   │   └── test_logic.py
│   └── ...

# Custom API Server - Test Coverage Project

## 📌 API Description
A custom API server that supports basic CRUD operations for users, books, or any entity.

## 🛠 Tech Stack
- Python 3.10
- Flask / FastAPI / Django
- pytest & pytest-cov
- requests / httpx (for API testing)

## 🧪 How to Run Tests
```bash
pip install -r requirements.txt
pytest --cov=app tests/
