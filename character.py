import random

from .item import Item
from .inventory import Inventory
from .data import LEVEL_REWARDS


class Character:
    # DÜZELTME 1 (KEŞİF RAPORU #1): Dışarıdan (Enemy'den) gelecek hp ve damage'ı karşılamak için parametreler eklendi!
    def __init__(self, name, hp=100, damage=10):
        self.name = name
        self.level = 1
        self.max_hp = hp          # Artık Enemy'den gelen dinamik canı alabiliyor
        self.current_hp = hp      # Hafıza kaybı tamamen çözüldü
        self.xp = 0
        self.xp_needed = 100
        self.damage = damage      # Artık Enemy'den gelen dinamik hasarı alabiliyor
        self.is_defending = False
        self.temp_damage_boost = 0
        self.temp_shield = 0
        self.inventory = Inventory(max_slots=3)
        self.inventory.add_item(Item("İksir", "heal", 30, uses=2))

    def attack(self):
        # DÜZELTME 2 (KEŞİF RAPORU #4): Sabit 0 yerine istenen hasar formülü hesaplanıp return edildi
        rastgele_bonus = random.randint(0, 5)
        toplam_hasar = self.damage + rastgele_bonus + self.temp_damage_boost
        
        # Geçici hasar boost'u kullanıldığı için sıfırlanıyor
        self.temp_damage_boost = 0
        return toplam_hasar

    def defend(self):
        print(f"  {self.name} savunma pozisyonu aldı! Bu tur %50 az hasar alacak.")
        self.is_defending = True # Savunma durumu aktif edildi

    def take_damage(self, damage):
        if self.temp_shield > 0:
            blocked = min(self.temp_shield, damage)
            damage -= blocked
            self.temp_shield = 0
            print(f"  Kalkan {blocked} hasarı bloke etti!")
        if self.is_defending:
            damage = damage // 2
            self.is_defending = False
        self.current_hp -= damage
        return damage

    # XP kazanma
    def gain_xp(self, amount):
        self.xp += amount
        print(f"  {self.name} {amount} XP kazandı!")
        if self.level < 5 and self.xp >= self.xp_needed:
            self.level_up()

    # Seviye atlama mekanikleri: HP, hasar artışı + envanter ödülü
    def level_up(self):
        XP_THRESHOLDS = {2: 150, 3: 225, 4: 340, 5: 500}
        
        # DÜZELTME 3 (KEŞİF RAPORU #6): XP birikimi sıfırlanıyor (gereken miktar düşülüyor)
        self.xp -= self.xp_needed
        if self.xp < 0:
            self.xp = 0
            
        self.level += 1
        
        # DÜZELTME 3: Maksimum can seviye başına 20 puan artırılıyor
        self.max_hp += 20
        
        self.xp_needed = XP_THRESHOLDS.get(self.level, 500)
        self.current_hp = self.max_hp
        self.damage += 2
        print(f"\n  *** SEVİYE ATLADI! {self.name} artık Level {self.level}! ***")
        print(f"  Max HP: {self.max_hp} | Hasar: {self.damage}")

        self.inventory.expand_slot()
        reward = LEVEL_REWARDS.get(self.level)
        if reward:
            item = Item(reward["name"], reward["type"], reward["value"], uses=reward["uses"])
            added = self.inventory.add_item(item)
            if added:
                print(f"  Yeni item kazandın: {item.name}!")
            else:
                print(f"  Envanter doldu, {item.name} alınamadı.")

    # Karakterin canlı olup olmadığını kontrol eder   
    def is_alive(self):
        return self.current_hp > 0

    # Karakterin istatistiklerini yazdırır
    def show_stats(self):
        print(f"  [{self.name}] HP: {self.current_hp}/{self.max_hp} | "
              f"Level: {self.level} | XP: {self.xp}/{self.xp_needed}")