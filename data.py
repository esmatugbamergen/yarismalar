
# LEVEL ÖDÜL TABLOSU

LEVEL_REWARDS = {
    2: {"name": "Güçlü İksir",    "type": "heal",         "value": 50, "uses": 1},
    3: {"name": "Saldırı Tozu",   "type": "attack_boost", "value": 8,  "uses": 1},
    4: {"name": "Demir Kalkan",   "type": "shield",       "value": 20, "uses": 1},
    5: {"name": "Uyuşturma Ruhu", "type": "stun",         "value": 0,  "uses": 1},
}


# BÖLÜM VERİLERİ

CHAPTERS = {
    1: {
        "name": "Karanlık Orman",
        "intro": "Sisli bir ormanın içinde ilerliyorsun...",
        "enemies": [
            {"name": "Goblin", "hp": 30, "damage": 5,  "xp": 50,  "level": 1},
            {"name": "Kurt",   "hp": 35, "damage": 6,  "xp": 60,  "level": 1},
        ],
        "battles": 2,
    },
    2: {
        "name": "Karanlık Mağara",
        "intro": "Taş duvarlar arasında yankılanan sesler duyuyorsun...",
        "enemies": [
            {"name": "Ork",    "hp": 50, "damage": 9,  "xp": 80,  "level": 2},
            {"name": "Yarasa", "hp": 45, "damage": 8,  "xp": 70,  "level": 2},
        ],
        "battles": 2,
    },
    3: {
        "name": "Zehirli Bataklık",
        "intro": "Çamurlu sularda her adım tehlike...",
        "enemies": [
            {"name": "Troll",           "hp": 70, "damage": 13, "xp": 115, "level": 3},
            {"name": "Zehirli Örümcek", "hp": 65, "damage": 12, "xp": 110, "level": 3},
        ],
        "battles": 2,
    },
    4: {
        "name": "Lanetli Kale",
        "intro": "Taş surların ardından uğursuz bir ışık süzülüyor...",
        "enemies": [
            {"name": "Şövalye", "hp": 90,  "damage": 17, "xp": 165, "level": 4},
            {"name": "Vampir",  "hp": 95,  "damage": 18, "xp": 175, "level": 4},
        ],
        "battles": 2,
    },
    5: {
        "name": "Karanlık Kule",
        "intro": "Kulenin tepesinde kader seni bekliyor...",
        "enemies": [
            {"name": "Ejderha",   "hp": 100, "damage": 23, "xp": 200, "level": 5},
            {"name": "Kara Lord", "hp": 110, "damage": 28, "xp": 300, "level": 5},
        ],
        "battles": 2,
    },
}
