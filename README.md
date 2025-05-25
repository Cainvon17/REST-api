# REST-api
Ice Cream Shop API - A lightweight REST API built with Flask and Python for managing an ice cream shop's flavors and pricing. It supports full CRUD operations using in-memory data structures
## Features Implemented

- `GET /icecreams` — View all available ice creams
- `POST /icecreams` — Add a new ice cream flavor
- `PUT /icecreams/<id>` — Update an existing ice cream
- `DELETE /icecreams/<id>` — Remove an ice cream
- `GET /` — Welcome message

----
## Setup Instructions (Terminal)
### 1. Change to your project directory
``bash
cd icecream-api(my project folder name)

### 2.Create and activate a virtual environment :
#### Create venv
python -m venv venv

#### Activate (choose based on OS)
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

### 3.Install dependencies:
pip install -r requirements.txt

### 4.Run the application:
python main.py
Then open your browser and go to: http://127.0.0.1:5000/icecreams

### 5.Testing the API with curl
--> In bash or command prompt terminal
#### Get all ice creams
curl http://127.0.0.1:5000/icecreams

#### Add new ice cream
Example:
curl -X POST http://127.0.0.1:5000/icecreams -H "Content-Type: application/json" -d "{\"flavor\":\"Butterscotch\",\"price\":65}"

#### Update an ice cream
Example:
curl -X PUT http://127.0.0.1:5000/icecreams/2 -H "Content-Type: application/json" -d "{\"flavor\":\"Mint Choco\",\"price\":70}"

#### Delete an ice cream
Example:
curl -X DELETE http://127.0.0.1:5000/icecreams/3
