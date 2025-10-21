from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import requests
import re

# --- MODEL SETUP ---
model = OllamaLLM(model="gemma:2b")

# --- PROMPT: Analisi meteo ---
template = """Sei un assistente per l'analisi di richieste meteo in linguaggio naturale.
Data una frase in italiano, estrai chiaramente:
- Città (se specificata)
- Intervallo date o periodo (se specificato)

Rispondi nel formato:
Città: <nome città o 'non specificata'>
Intervallo date: <date o 'non specificato'>

Input: {text}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


# --- FUNZIONI DI SUPPORTO ---
def geocode(città):
    """Ottiene le coordinate (lat, lon) da Nominatim (OpenStreetMap)."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": città, "format": "json", "limit": 1}
    headers = {"User-Agent": "MeteoAssistant/1.0"}
    
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code == 200 and resp.json():
        data = resp.json()[0]
        lat = float(data["lat"])
        lon = float(data["lon"])
        return (lat, lon)
    else:
        return None


def get_weather(lat, lon):
    """Ottiene meteo in tempo reale da Open-Meteo."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        cw = data.get("current_weather", {})
        return f"Temperatura attuale: {cw.get('temperature')}°C, vento: {cw.get('windspeed')} km/h"
    else:
        return "Errore nel recupero dati meteo."


# --- LOOP PRINCIPALE ---
print("💡 Digita 'exit' per uscire completamente.")
print("Chiedimi il meteo per una città specifica. O le previsioni meteo della settimana.\n")

modo_meteo = False
ultima_città = None
ultima_data = None

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Uscita dal programma.")
        break

    # controllo se è un cambio di argomento
    if any(p in user_input.lower() for p in ["cambia argomento", "esci meteo", "nuovo argomento"]):
        modo_meteo = False
        ultima_città = None
        ultima_data = None
        print("Uscito dal contesto meteo. Torniamo alla conversazione generale.\n")
        continue

    # se non siamo in modalità meteo, controlla se la richiesta riguarda il meteo
    if not modo_meteo and any(word in user_input.lower() for word in ["meteo", "piove", "tempo", "previsioni"]):
        modo_meteo = True
        print("Entrato nel contesto meteo.\n")

    if modo_meteo:
        msg = chain.invoke({"text": user_input})
        print("Analisi estratta:")
        print(msg)

        # estrazione semplice da testo modello
        città_match = re.search(r"Città:\s*(.+)", msg)
        data_match = re.search(r"Intervallo date:\s*(.+)", msg)

        città = città_match.group(1).strip().lower() if città_match else None
        intervallo = data_match.group(1).strip() if data_match else None

        if città and città != "non specificata":
            ultima_città = città
        if intervallo and intervallo != "non specificato":
            ultima_data = intervallo

        if not ultima_città:
            print("Nessuna città specificata. Specifica una città per continuare.\n")
            continue

        coords = geocode(ultima_città)
        if not coords:
            print("Non riesco a trovare le coordinate per la città indicata.\n")
            continue

        weather_info = get_weather(*coords)
        print(f"Meteo per {ultima_città.capitalize()} ({ultima_data or 'oggi'}): {weather_info}\n")

    else:
        print("Modalità chat generale (nessuna logica meteo qui per ora).")
        print("Posso rispondere su altri argomenti come programmazione o IA.\n")
