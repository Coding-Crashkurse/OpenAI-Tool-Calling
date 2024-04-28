from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/weather")
async def get_weather(city: str):
    # This endpoint provides weather information based on the city.
    if city.lower() == "sunnyville":
        return {"city": city, "weather": "Sunny, 22°C"}
    elif city.lower() == "rainytown":
        return {"city": city, "weather": "Rainy, 15°C"}
    else:
        raise HTTPException(404, detail=f"Weather data not available for city: {city}")

@app.get("/outdoor-seating")
async def outdoor_seating(city: str):
    # This endpoint checks if outdoor seating is available in the given city.
    if city.lower() == "sunnyville":
        return {"city": city, "outdoor_seating": "Available"}
    elif city.lower() == "rainytown":
        return {"city": city, "outdoor_seating": "Unavailable"}
    else:
        raise HTTPException(404, detail=f"Outdoor seating information not available for city: {city}")
