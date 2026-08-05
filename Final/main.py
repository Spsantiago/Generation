import requests
def dish_fetch(num):
    url = f"https://api-colombia.com/api/v1/TypicalDish"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"--- PLATOS TÍPICOS DE COLOMBIA ---")
        for dish in data:
            if dish.get("id") == num:
                return {
                    "id": dish.get("id"),
                    "name": dish.get("name"),
                    "description": dish.get("description"),
                    "city": dish.get("city", {}).get("name")
                }
    else:
       print("Error al conectar con la API:", response.status_code)
      

