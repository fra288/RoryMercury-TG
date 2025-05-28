import json
import os
from datetime import datetime

db_path = "data/economia.json"

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(db_path):
    with open(db_path, "w") as f:
        json.dump({}, f)

def load_economy():
    with open(db_path, "r") as f:
        return json.load(f)

def save_economy(data):
    with open(db_path, "w") as f:
        json.dump(data, f, indent=4)

def init_user(user_id):
    data = load_economy()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {
            "oro": 500,
            "banco": 0,
            "xp": 0,
            "nivel": 1,
            "trabajo": None,
            "inventario": [],
            "pareja": None,
            "ultima_claim": "",
            "ultima_daily": ""
        }
        save_economy(data)
    return data[uid]

def dar_oro(user_id, cantidad):
    data = load_economy()
    uid = str(user_id)
    if uid in data:
        data[uid]["oro"] += cantidad
        save_economy(data)

def dar_xp(user_id, cantidad):
    data = load_economy()
    uid = str(user_id)
    if uid in data:
        data[uid]["xp"] += cantidad
        save_economy(data)

def subir_nivel_si_corresponde(user_id):
    data = load_economy()
    uid = str(user_id)
    if uid in data:
        xp = data[uid]["xp"]
        nivel = data[uid]["nivel"]
        if xp >= nivel * 100:
            data[uid]["nivel"] += 1
            data[uid]["xp"] = 0
            save_economy(data)
            return True
    return False