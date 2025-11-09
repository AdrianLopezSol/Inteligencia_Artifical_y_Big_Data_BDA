# Tarea 1: Construcción infraestructura FIWARE

Este readme describe la creación de la infraesctructura para todo el sistema de **Fiware**.

## FIWARE Setup con Orion, QuantumLeap y CrateDB

Este proyecto despliega un stack básico de FIWARE con los siguientes componentes:

- **MongoDB**: Base de datos utilizada por Orion Context Broker para almacenar el estado actual de las entidades.
- **Orion Context Broker**: Gestiona el estado de las entidades NGSI y permite actualizaciones y consultas.
- **CrateDB**: Base de datos de series temporales para almacenar históricos de atributos de entidades.
- **QuantumLeap**: Servicio que suscribe a Orion y guarda los cambios en CrateDB para análisis históricos.

### docker-compose.yml

```yaml
version: "3.7"
services:
  mongo:
    image: mongo:8.0
    networks:
      - fiware-net

  orion:
    image: telefonicaiot/fiware-orion
    ports:
       - "1026:1026"
    depends_on:
       - mongo
    command: -dbURI mongodb://mongo
    networks:
      - fiware-net

  cratedb:
    image: crate:5.2.2
    container_name: fiware_cratedb
    ports:
      - "4200:4200"   # HTTP
      - "5432:5432"   # Protocolo Postgres (opcional)
    volumes:
      - crate_data:/var/lib/crate
    networks:
      - fiware-net

  quantumleap:
    image: fiware/quantum-leap:1.0.0
    container_name: fiware_quantumleap
    depends_on:
      - cratedb
      - orion
    ports:
      - "8668:8668"
    environment:
      - CRATE_HOST=cratedb
      - CRATE_PORT=4200
      - TZ=Europe/Madrid
    networks:
      - fiware-net

volumes:
  mongo_data:
  crate_data:

networks:
  fiware-net:
    driver: bridge
```

### Crear las entidades en Orion Context Broker

A continuación se muestra cómo crear la entidad `SensorAgua:001` con todos sus atributos y metadata usando la API NGSIv2:

```bash
curl -iX POST 'http://localhost:1026/v2/entities' \
  -H 'Content-Type: application/json' \
  -H 'Fiware-Service: openiot' \
  -H 'Fiware-ServicePath: /' \
  -d '{
    "id": "SensorAgua:001",
    "type": "SensorCalidadAgua",
    "ph": {
      "value": 7.2,
      "type": "Float",
      "metadata": { "unidad": { "value": "pH" } }
    },
    "chlorine": {
      "value": 0.5,
      "type": "Float",
      "metadata": { "unidad": { "value": "mg/L" } }
    },
    "temperatura": {
      "value": 18.4,
      "type": "Float",
      "metadata": { "unidad": { "value": "°C" } }
    },
    "turbidez": {
      "value": 2.1,
      "type": "Float",
      "metadata": { "unidad": { "value": "NTU" } }
    },
    "location": {
      "type": "geo:json",
      "value": { "type": "Point", "coordinates": [-3.7038, 40.4168] }
    },
    "fechaHora": {
      "value": "2025-10-19T10:45:00Z",
      "type": "DateTime"
    }
  }'
```

Posteriormente `SensorCO2:001` con todos sus atributos y metadata usando la API NGSIv2:

```bash
curl -iX POST 'http://localhost:1026/v2/entities' \
  -H 'Content-Type: application/json' \
  -H 'Fiware-Service: openiot' \
  -H 'Fiware-ServicePath: /' \
  -d '{
    "id": "SensorCO2:001",
    "type": "SensorCO2",
    "co2": {
      "value": 415.7,
      "type": "Float",
      "metadata": { "unidad": { "value": "ppm" } }
    },
    "location": {
      "type": "geo:json",
      "value": { "type": "Point", "coordinates": [-3.7038, 40.4168] }
    },
    "fechaHora": {
      "value": "2025-10-19T10:45:00Z",
      "type": "DateTime"
    }
  }'
```

Finalmente `SensorTemperatura:001` con todos sus atributos y metadata usando la API NGSIv2:

```bash
curl -iX POST 'http://localhost:1026/v2/entities' \
  -H 'Content-Type: application/json' \
  -H 'Fiware-Service: openiot' \
  -H 'Fiware-ServicePath: /' \
  -d '{
    "id": "SensorTemperatura:001",
    "type": "SensorTemperatura",
    "temperatura": {
      "value": 23.5,
      "type": "Float",
      "metadata": { "unidad": { "value": "°C" } }
    },
    "location": {
      "type": "geo:json",
      "value": { "type": "Point", "coordinates": [-3.7038, 40.4168] }
    },
    "fechaHora": {
      "value": "2025-10-19T10:45:00Z",
      "type": "DateTime"
    }
  }'
```

### Creación de una suscripción en Orion Context Broker

Este es el comando ejecutado hacia Orion Context Broker para que envíe todas las actualizaciones de nuestros sensores a QuantumLeap:

```bash
curl -iX POST 'http://localhost:1026/v2/subscriptions' \
  -H 'Content-Type: application/json' \
  -H 'Fiware-Service: openiot' \
  -H 'Fiware-ServicePath: /' \
  -d '{
    "description": "Send all updates from SensorAgua, SensorCO2, and SensorTemperatura to QuantumLeap",
    "subject": {
      "entities": [
        { "idPattern": "SensorAgua:.*", "type": "SensorCalidadAgua" },
        { "idPattern": "SensorCO2:.*", "type": "SensorCO2" },
        { "idPattern": "SensorTemperatura:.*", "type": "SensorTemperatura" }
      ],
      "condition": {
        "attrs": [
          "ph",
          "chlorine",
          "temperatura",
          "turbidez",
          "co2",
          "fechaHora",
          "location"
        ]
      }
    },
    "notification": {
      "http": { "url": "http://quantumleap:8668/v2/notify" },
      "attrs": [
        "ph",
        "chlorine",
        "temperatura",
        "turbidez",
        "co2",
        "fechaHora",
        "location"
      ],
      "metadata": ["dateCreated", "dateModified"]
    },
    "throttling": 0
  }'
```

### Carga masiva de datos

Ahora vamos a realizar la **carga de datos masivos** utilizando un script de Python que envía actualizaciones a Orion Context Broker.  
El objetivo es enviar **400 actualizaciones por atributo** para cada una de nuestras tres entidades.

Cada vez que el script envíe una actualización:

1. Orion actualizará el documento en MongoDB con el nuevo estado.
2. Gracias a la **suscripción a QuantumLeap**, se enviará automáticamente una copia a QuantumLeap, que la insertará en CrateDB como un nuevo registro de serie de tiempo.

```python
import requests
import random

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
            
            if response.status_code in [200, 204]:
                print(f"{entidad['id']} - {attr} actualizado: {value}")
            else:
                print(f"Error al actualizar {entidad['id']} - {attr}: {response.status_code} {response.text}")
```

### Visualización de los registros en CrateDB

A continuación se muestran imágenes de los registros históricos de los sensores en CrateDB y la vista general del stack FIWARE puesto a que creemos que se visualiza mejor y se muestran todos los datos en comparación con MongoDB:

#### Vista de las entidades

![Vista de las entidades](/Recursos/img/Vista-entidades.png)

#### Vista de las tablas en CrateDB

![Vista de las tablas](/Recursos/img/Vista-tablas.png)

#### Vista general del stack FIWARE

![Vista general del stack](/Recursos/img/Vista-general-stack.png)
