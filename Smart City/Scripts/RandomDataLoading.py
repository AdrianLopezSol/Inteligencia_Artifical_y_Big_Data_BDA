import requests
import random
from datetime import datetime, timedelta

ORION_URL = "http://localhost:1026/v2/entities"
HEADERS = {
    "Content-Type": "text/plain",
    "Fiware-Service": "openiot",
    "Fiware-ServicePath": "/"
}

entidades = [
    {
        "id": "SensorAgua:001",
        "type": "SensorCalidadAgua",
        "attrs": {
            "ph": 7.2,
            "chlorine": 0.5,
            "temperatura": 18.4,
            "turbidez": 2.1
        }
    },
    {
        "id": "SensorCO2:001",
        "type": "SensorCO2",
        "attrs": {
            "co2": 415.7
        }
    },
    {
        "id": "SensorTemperatura:001",
        "type": "SensorTemperatura",
        "attrs": {
            "temperatura": 23.5
        }
    }
]

NUM_UPDATES = 400

for entidad in entidades:
    for attr, base_value in entidad["attrs"].items():
        for i in range(NUM_UPDATES):
            if isinstance(base_value, float):
                value = round(base_value + random.uniform(-0.5, 0.5), 2)
            else:
                value = base_value
            
            url = f"{ORION_URL}/{entidad['id']}/attrs/{attr}/value"
            response = requests.put(url, headers=HEADERS, data=str(value))
            
            if response.status_code in [204, 200]:
                print(f"{entidad['id']} - {attr} actualizado: {value}")
            else:
                print(f"Error al actualizar {entidad['id']} - {attr}: {response.status_code} {response.text}")
