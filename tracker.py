import json
import os
from datetime import date

HISTORY_FILE = 'output/history.json'

def save_entry(name, weight, nutrition, bmi_data):
    """Save daily entry to history."""
    os.makedirs('output', exist_ok=True)
    history = load_history()
    entry = {
        'date': str(date.today()),
        'name': name,
        'weight': weight,
        'calories': nutrition['calories'],
        'protein': nutrition['protein'],
        'carbs': nutrition['carbs'],
        'fats': nutrition['fats'],
        'bmi': bmi_data['bmi'],
        'category': bmi_data['category']
    }
    history.append(entry)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)
    print(f"Entry saved for {name}! ✅")
    return entry

def load_history():
    """Load history from file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def get_streak(name):
    """Count consecutive days tracked."""
    history = load_history()
    user = [e for e in history
            if e['name'] == name]
    return len(user)

def get_achievements(streak):
    """Get achievement badges."""
    achievements = []
    if streak >= 1:
        achievements.append(
            '🏅 First Step — Started journey!')
    if streak >= 7:
        achievements.append(
            '🔥 7 Day Warrior — One week strong!')
    if streak >= 14:
        achievements.append(
            '💪 Two Week Champion!')
    if streak >= 30:
        achievements.append(
            '👑 30 Day Legend — Unstoppable!')
    return achievements