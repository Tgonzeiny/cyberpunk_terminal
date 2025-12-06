import random
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

def load_json(name: str):
    with open(BASE / "data" / name, "r") as f:
        return json.load(f)

def get_augmentations():
    return load_json("augmentations.json")

def get_district_status():
    districts = ["Neon Bazaar", "Sector 7", "Old Stack", "Chrome Alley"]
    return {
        "district": random.choice(districts),
        "power_grid": f"{random.randint(60, 95)}%",
        "crime_index": random.randint(10, 98),
        "air_quality": random.choice(["Clean", "Hazy", "Toxic"]),
    }

def scan_citizen(name):
    return {
        "name": name,
        "occupation": random.choice(["Netrunner", "Courier", "Tech Salvager", "Private Security"]),
        "risk_score": random.randint(1, 100),
        "last_seen": random.choice(["Sector 7", "Neon Bazaar", "Drone District"]),
        "augmentations": random.sample(
            ["Optic HUD", "Ghostlink", "Chrome Bones", "Neural Uplink", "Nano Muscles"],
            k=random.randint(1, 3),
        ),
    }

def get_latest_news():
    headlines = [
        "Cyberdrugs Sweep Through Neon Bazaar",
        "AI Council Bans Unauthorized Neural Links",
        "Power Grid Surge Shuts Down Chrome Alley",
        "Corporate War Intensifies in Sector 12",
    ]
    return {"headline": random.choice(headlines)}
