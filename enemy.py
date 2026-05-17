# enemy.py - Düşman karakterlerini temsil eden modül
import random
from .character import Character

class Enemy(Character):
    def __init__(self, name, hp, damage, level=1, xp_reward=20):
        super().__init__(name, hp, damage)
        self.name = name
        self.level = level
        self.max_hp = hp
        self.current_hp = hp
        self.damage = damage
        self.xp_reward = xp_reward
        self.stunned = False

    def attack(self):
        if self.stunned:
            print(f"   {self.name} felç! Bu tur saldıramadı.")
            self.stunned = False
            return 0
            
        # DÜZELTME 1 (KEŞİF RAPORU #4): Engel olan 'return 0' satırı kaldırıldı!
        # Böylece alt satırdaki hasar hesaplaması artık başarıyla çalışacak.
        bonus_damage = random.randint(-1, 3)
        return max(0, self.damage + bonus_damage)
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
        return damage

    def is_alive(self):
        return self.current_hp > 0

    def get_xp_reward(self):
        return self.xp_reward

    def show_stats(self):
        print(f"   [{self.name}] HP: {self.current_hp}/{self.max_hp} | Level: {self.level}")