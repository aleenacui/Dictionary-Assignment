car_info = {"brand": "Toyota", "model": "Corolla", "year": 2022, "color": "White", "engine": "1.8L", "transmission": "Automatic", "mileage": 35000, "fuel_type": "Petrol"}

print(car_info["brand"])
print(car_info["model"])
print(car_info["year"])
print(car_info["color"])

car_info["owner"] = "Ali"
print(f"The dictionary is now: {car_info['owner']}")

car_info["color"] = "Black"
print(f"The dictionary is now: {car_info['color']}")

del car_info["mileage"]
print(f"The dictionary after deleting mileage: {car_info}")

print(car_info.get("engine"))
print("transmission" in car_info)
print(len(car_info))
