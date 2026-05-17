# item.py - Oyun içi eşyaların tanımlandığı modül
class Item:
    def __init__(self, name, item_type, effect_value, uses=1):
        self.name = name
        self.item_type = item_type   # "heal" | "attack_boost" | "shield" | "stun"
        self.effect_value = effect_value
        self.uses = uses

    def use(self, character, enemy=None):
        if self.uses <= 0:
            print(f"  {self.name} tükendi!")
            return False

        if self.item_type == "heal":
            before = character.current_hp
            character.current_hp = min(character.current_hp + self.effect_value, character.max_hp)
            healed = character.current_hp - before
            print(f"  {self.name} kullanıldı! +{healed} HP kazandın.")

        elif self.item_type == "attack_boost":
            character.temp_damage_boost += self.effect_value
            print(f"  {self.name} kullanıldı! Sonraki saldırı +{self.effect_value} hasar alır.")

        elif self.item_type == "shield":
            character.temp_shield += self.effect_value
            print(f"  {self.name} kullanıldı! {self.effect_value} hasara karşı kalkan aktif.")

        elif self.item_type == "stun":
            # TODO: Felç (stun) etkisi türünde, parametre olarak gelen düşmanın 'stunned' durumunu aktif hale getir.

            pass

        return True
    

    def __str__(self):
        type_labels = {
            "heal": "İyileşme",
            "attack_boost": "Saldırı Güçlendirme",
            "shield": "Kalkan",
            "stun": "Felç"
        }
        label = type_labels.get(self.item_type, self.item_type)
        return f"{self.name}  [{label}]  (x{self.uses})"
