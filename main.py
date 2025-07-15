import request
import pymem
import time
import os
import json
import sys



ONFIG_DIR = os.path.join(os.environ['LOCALAPPDATA'], 'temp', 'PyIt')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')
DEFAULT_SETTINGS = {
    "esp_rendering": 1,
    "esp_mode": 1,
    "line_rendering": 1,
    "hp_bar_rendering": 1,
    "head_hitbox_rendering": 1,
    "bons": 1,
    "nickname": 1,
    "radius": 50,
    "keyboard": "C",
    "aim_active": 0,
    "aim_mode": 1,
    "aim_mode_distance": 1,
    "trigger_bot_active": 0,
    "keyboards": "X", 
    "weapon": 1,
    "bomb_esp": 1
}
BombPlantedTime = 0
BombDefusedTime = 0


def load_settings():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(CONFIG_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def get_offsets_and_client_dll():
    offsets = requests.get('https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json').json()
    client_dll = requests.get('https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json').json()
    return offsets, client_dll

def get_window_size(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        rect = win32gui.GetClientRect(hwnd)
        return rect[2], rect[3]
    return None, None
