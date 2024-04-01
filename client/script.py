import requests

BASE_URL = "http://localhost:5000/api/restaurants"

# Requisição para obter todos os restaurantes
response = requests.get(BASE_URL)
print("GET all restaurants:")
print(response.json())
print()

# Requisição para obter um restaurante pelo ID
response = requests.get(BASE_URL + "/1")
print("GET restaurant by ID:")
print(response.json())
print()

# Requisição para obter todos os restaurantes com filtro
params = {"addressRegion": "SP"}
response = requests.get(BASE_URL, params=params)
print("GET all restaurants with filter:")
print(response.json())
print()

# Requisição para inserir um novo restaurante
new_restaurant = {
    "name": "Outback Steakhouse",
    "address": {
        "postalCode": "01415-000",
        "streetAddress": "Av. Pres. Juscelino Kubitschek, 2041",
        "addressLocality": "São Paulo",
        "addressRegion": "SP",
        "addressCountry": "BR"
    },
    "url": "https://www.outback.com.br/",
    "menu": "https://www.outback.com.br/menu",
    "telephone": "+55 11 3078-7748",
    "priceRange": "15-45"
}
response = requests.post(BASE_URL, json=new_restaurant)
print("POST new restaurant:")
print(response.json())
print()

# Requisição para atualizar um restaurante pelo ID
updated_restaurant = {"name": "Outback Steakhouse Brasil"}
response = requests.put(BASE_URL + "/1", json=updated_restaurant)
print("PUT update restaurant:")
print(response.json())
print()

# Requisição para excluir um restaurante pelo ID
response = requests.delete(BASE_URL + "/1")
print("DELETE restaurant by ID:")
print(response.json())
print()
