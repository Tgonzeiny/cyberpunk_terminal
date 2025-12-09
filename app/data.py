import random
import json
from http.client import HTTPException
from pathlib import Path

BASE = Path(__file__).resolve().parent

def load_json(name: str):
    with open(BASE / "data" / name, "r") as f:
        return json.load(f)


def get_augmentations():
    return load_json("augmentations.json")  # → now returns Kiroshi, Sandevistan, Gorilla Arms, etc.


def get_district_status():
    districts = [
        "Heywood Heights", "Santo Domingo Sprawl", "Vista del Rey", "Rancho Coronado",
        "Pacific Bluffs", "Westwind Estate", "Badlands Border Zone", "Little China Undercity",
        "Kabuki Roundabout", "Corpo Plaza Sublevels"
    ]
    district = random.choice(districts)
    return {
        "district": district,
        "power_grid": f"{random.randint(42, 98)}%",
        "crime_index": random.randint(28, 97),
        "air_quality": random.choice(["Toxic", "Hazy", "Acid Rain Warning", "Nominal", "Recyclable"]),
        "controlling_gang": random.choice(
            ["Valentinos", "Mox", "6th Street", "Tyger Claws", "Voodoo Boys", "None – corpo lockdown"])
    }


def scan_citizen(name: str = None):
    citizens = [
        "Razor Vega", "Nyxx Kade", "Cassian Holt", "Selene Voss", "Dante Creed",
        "Kira Nox", "Jett Valkyrie", "Raven Six", "Neon Shiro", "Vanta Crowe",
        "Sable Rex", "Echo Draven"
    ]

    target = name.lower() if name else random.choice([c.lower() for c in citizens])
    if target not in [c.lower() for c in citizens]:
        raise HTTPException(status_code=404, detail="ICE DETECTED – NO RECORD FOUND")

    chosen = random.choice(citizens)
    augs = random.sample(get_augmentations(), k=random.randint(1, 4))

    return {
        "name": chosen,
        "alias": chosen.split()[0],
        "occupation": random.choice(["Solo", "Netrunner", "Techie", "Fixer", "Ripperdoc", "Nomad", "Corpo"]),
        "threat_level": random.randint(15, 95),
        "last_seen": random.choice([
            "Heywood Heights", "Kabuki Roundabout", "Little China Undercity",
            "Pacific Bluffs", "Badlands Border Zone", "Corpo Plaza Sublevels"
        ]),
        "known_chrome": [aug["name"] for aug in augs],
        "status": random.choice([
            "Active – laying low", "On a gig", "Flatlined 3 days ago",
            "Boostergang activity reported", "Arasaka watchlist", "Clean"
        ])
    }


def get_latest_news():
    headlines = [
        "Militech convoy ambushed outside Rancho Coronado",
        "Kiroshi Optics black-market raid in Kabuki – 40 arrests",
        "Unexplained blackwall breach traced to Pacific Bluffs server farm",
        "New Sandevistan variant causing cyberpsycho cases in Heywood",
        "Tyger Claws declare war on Valentinos after Vista del Rey drive-by",
        "Biotechnica announces ‘immortality trials’ for select corpos",
        "Mox put Pacific Bluffs stadium on lockdown after Voodoo Boys incursion"
    ]
    return {"headline": random.choice(headlines), "source": "N54 News • 54 minutes ago"}
