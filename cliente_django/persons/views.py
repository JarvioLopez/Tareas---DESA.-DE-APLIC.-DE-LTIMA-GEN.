import requests
from django.shortcuts import render

API_URL = "http://127.0.0.1:8000/persons"


def person_list(request):
    persons = []
    error = None
    try:
        response = requests.get(
            API_URL,
            params={"skip": 0, "limit": 5},
            timeout=5,
        )
        response.raise_for_status()
        persons = response.json()
        if not isinstance(persons, list):
            raise ValueError("Se esperaba una lista JSON")
    except requests.exceptions.RequestException:
        error = "No se pudo conectar con la API FastAPI. Verifica que esté ejecutándose en el puerto 8000."
    except ValueError:
        error = "La API devolvió un formato inesperado."
    return render(
        request,
        "persons/person_list.html",
        {"persons": persons, "error": error},
    )
