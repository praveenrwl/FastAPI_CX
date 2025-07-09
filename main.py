from fastapi import FastAPI
import json

# End Point
app = FastAPI()

# To load function from json
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

# Route
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def avout():
    return {'message':'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    return {'error':'Patient not found'}