# 🍦 Ice Cream Shop API

A lightweight REST API built with Flask and Python for managing an ice cream shop's flavors and pricing.  
It supports full CRUD operations using in-memory data structures.

---

## 🚀 Features Implemented

- `GET /icecreams` — View all available ice creams
- `POST /icecreams` — Add a new ice cream flavor
- `PUT /icecreams/<id>` — Update an existing ice cream
- `DELETE /icecreams/<id>` — Remove an ice cream
- `GET /` — Welcome message

---

## 🛠️ Setup Instructions (Terminal)

### 1. Change to your project directory

```bash
cd icecream-api
# Create venv
python -m venv venv

# Activate (choose based on OS)
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

python main.py

Open your browser and visit:
http://127.0.0.1:5000/icecreams
