# battle.py - Savaş mekaniklerini yöneten modül
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn_count = 0
        self.battle_log = []

    def start_battle(self):
        print(f"\n  {'='*43}")
        print(f"  SAVAŞ: {self.player.name}  vs  {self.enemy.name}")
        print(f"  {'='*43}\n")

        while self.player.is_alive() and self.enemy.is_alive():
            self.turn_count += 1
            self.show_turn_status()

            while True:
                result = self.player_turn()
                if result != "back_to_menu":
                    break

            if result == "fled":
                return "fled"

            if self.enemy.is_alive():
                if result == "failed_flee":
                    self.enemy_turn(damage_multiplier=1.5)
                # DÜZELTME 1: Oyuncu saldırdıysa, savunduysa VEYA item kullandıysa sıra düşmana geçer
                elif result in ["continue", "item_used"]: 
                    self.enemy_turn()

        return self.end_battle()

    def player_turn(self):
        print(f"\n  --- Senin Turun (Tur {self.turn_count}) ---")
        print("  1. Saldır")
        print("  2. Savun")
        print("  3. Envanter")
        print("  4. Kaç")

        while True:
            choice = input("  Seçim yap (1-4): ").strip()
            if choice in ["1", "2", "3", "4"]:
                break
            print("  Geçersiz seçim!")

        if choice == "1":
            damage = self.player.attack()
            actual = self.enemy.take_damage(damage)
            msg = f"  {self.player.name} saldırdı! {self.enemy.name} {actual} hasar aldı."
            print(msg)
            self.battle_log.append(msg)
            return "continue"

        elif choice == "2":
            self.player.defend()
            self.battle_log.append(f"  {self.player.name} savunma yaptı.")
            return "continue"

        elif choice == "3":
            inv_result = self.use_inventory()
            if inv_result == "no_items" or inv_result == "back":
                if inv_result == "no_items":
                    print("  Envanterde kullanılabilir item yok!")
                return "back_to_menu" 
            
            # DÜZELTME 1 (KEŞİF RAPORU #4): İtem başarıyla kullanıldıysa sırayı 'item_used' olarak bitir
            if inv_result == "used":
                return "item_used"

        elif choice == "4":
            if random.random() < 0.5:
                print("  Başarıyla kaçtın!")
                self.battle_log.append(f"  {self.player.name} kaçtı!")
                return "fled"
            else:
                print("  Kaçamadın! Düşman öfkelendi ve daha güçlü saldıracak!")
                self.battle_log.append(f"  {self.player.name} kaçamadı.")
                return "failed_flee"

        return "continue"

    def use_inventory(self):
        self.player.inventory.show()
        if not self.player.inventory.has_items():
            return "no_items"

        while True:
            choice = input("  Kullanmak istediğin item numarası (0=geri): ").strip()
            if choice == "0":
                return "back"
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(self.player.inventory.items):
                    item = self.player.inventory.items[idx]
                    if item.uses > 0:
                        item.use(self.player, self.enemy)
                        self.player.inventory.remove_empty()
                        return "used"
            print("  Geçersiz seçim!")

    def enemy_turn(self, damage_multiplier=1):  
        damage = self.enemy.attack()
        
        # DÜZELTME 2 (KEŞİF RAPORU #3): Düşman felç veya etkisizken sessizce dönmek yerine bilgi yazdırıyoruz
        if damage == 0:
            msg = f"  {self.enemy.name} bu tur saldıramadı veya hasar veremedi!"
            print(msg)
            self.battle_log.append(msg)
            return

        damage = int(damage * damage_multiplier)
        actual = self.player.take_damage(damage)
        if damage_multiplier > 1:
            msg = f"  {self.enemy.name} öfkeyle saldırdı! {self.player.name} {actual} hasar aldı!"
        else:
            msg = f"  {self.enemy.name} saldırdı! {self.player.name} {actual} hasar aldı."
        print(msg)
        self.battle_log.append(msg)

    def show_turn_status(self):
        print(f"\n  {'─'*43}")
        print(f"  TUR {self.turn_count}")
        self.player.show_stats()
        self.enemy.show_stats()
        print(f"  {'─'*43}")

    def end_battle(self):
        print(f"\n  {'='*43}")
        if self.player.is_alive():
            print(f"  KAZANDIN! {self.enemy.name} yenildi!")
            self.player.gain_xp(self.enemy.get_xp_reward())
            return "win"
        else:
            print(f"  KAYBETTİN! {self.player.name} yenildi...")
            return "lose"
