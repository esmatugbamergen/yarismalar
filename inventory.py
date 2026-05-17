# inventory.py - Oyuncunun envanterini yöneten modül
from .item import Item

class Inventory:
    def __init__(self, max_slots=3):
        self.max_slots = max_slots
        self.items = []

    def add_item(self, item):
        # Aynı isimli item varsa uses'ını artır
        for existing in self.items:
            if existing.name == item.name:
                existing.uses += item.uses
                return True
        if len(self.items) < self.max_slots:
            self.items.append(item)
            return True
        return False

    # Seviye atladıkça envanter slotunu açmak için fonksiyon
    def expand_slot(self):
        # TODO: Seviye atlama ödülü olarak envanterin maksimum kapasitesini (max_slots) 1 birim artır.
        pass  

    def show(self):
        print(f"\n  Envanter  ({len(self.items)}/{self.max_slots} slot):")
        if not self.items:
            print("  [Boş]")
            return
        for i, item in enumerate(self.items):
            print(f"    {i + 1}. {item}")

    # Kullanılan item'ları envanterden kaldırmak için fonksiyon
    def remove_empty(self):
        self.items = [item for item in self.items if item.uses > 0]

    # Envanterde kullanılabilir item olup olmadığını kontrol eden fonksiyon
    def has_items(self):
        return True  
