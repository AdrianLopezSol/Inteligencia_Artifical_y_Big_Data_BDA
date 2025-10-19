# Tarea 1: Definición de Entidades

Este readme describe las entidades definidas para el **Orion Context Broker (FIWARE)** correspondientes a diferentes tipos de sensores ambientales de la práctica.


Cada entidad sigue el formato **NGSI-v2**, con atributos que incluyen su valor, tipo de dato y metadatos (como las unidades de medida).

---

## Sensor de Temperatura

Representa un sensor que mide la temperatura ambiental.

```json
{
  "id": "SensorTemperatura:001",
  "type": "SensorTemperatura",
  "temperatura": {
    "value": 23.5,
    "type": "Float",
    "metadata": {
      "unidad": { "value": "°C" }
    }
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [-3.7038, 40.4168]
    }
  },
  "fechaHora": {
    "value": "2025-10-19T10:45:00Z",
    "type": "DateTime"
  }
}

```
## Sensor de CO2

Representa un sensor que mide cantidad de Co2 en el agua.

```json


{
  "id": "SensorCO2:001",
  "type": "SensorCO2",
  "co2": {
    "value": 415.7,
    "type": "Float",
    "metadata": {
      "unidad": { "value": "ppm" }
    }
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [-3.7038, 40.4168]
    }
  },
  "fechaHora": {
    "value": "2025-10-19T10:45:00Z",
    "type": "DateTime"
  }
}

```

##  Sensor de Calidad del Agua

Representa un sensor que mide la calidad del agua, con valores como ph, temperatura, turbidez y la cantidad de cloro.

```json


{
  "id": "SensorAgua:001",
  "type": "SensorCalidadAgua",
  "ph": {
    "value": 7.2,
    "type": "Float",
    "metadata": {
      "unidad": { "value": "pH" }
    }
  },
  "chlorine": {
    "value": 0.5,
    "type": "Float",
    "metadata": {
      "unidad": { "value": "mg/L" }
    }
  },
  "temperatura": {
    "value": 18.4,
    "type": "Float",
    "metadata": {
      "unidad": { "value": "°C" }
    }
  },
  "turbidez": {
    "value": 2.1,
    "type": "Float",
    "metadata": {
      "unidad": { "value": "NTU" }
    }
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [-3.7038, 40.4168]
    }
  },
  "fechaHora": {
    "value": "2025-10-19T10:45:00Z",
    "type": "DateTime"
  }
}
