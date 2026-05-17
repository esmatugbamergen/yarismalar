# TODO: Sınıf etkileşimleri için gerekli olan içe aktarma (import) işlemlerini tamamla
import random
from game.data import CHAPTERS
from game.enemy import Enemy
from game.character import Character
from game.battle import Battle

class Game:
    def __init__(self):
        self.player = None

    def setup(self):
        print("=" * 45)
        print("      TERMINAL RPG BATTLE")
        print("=" * 45)
        name = input("\nKarakterinin adını gir: ").strip()
        if not name:
            name = "Kahraman"
        self.player = Character(name)
        print(f"\n  {self.player.name} maceraya başlıyor!")

    def play_chapter(self, chapter_num):
        chapter = CHAPTERS[chapter_num]

        print(f"\n  {'#'*43}")
        print(f"  BÖLÜM {chapter_num}: {chapter['name'].upper()}")
        print(f"  {'#'*43}")
        print(f"\n  {chapter['intro']}\n")
        input("  [Devam etmek için Enter'a bas...]\n")

        enemies_data = chapter["enemies"].copy()  # henüz oluşturulmamış düşmanlar
        fled_enemies = []                        # kaçılan Enemy objeleri (HP korunur)  

        while enemies_data or fled_enemies:

            if enemies_data:
                enemy_data = random.choice(enemies_data)
                enemies_data.remove(enemy_data)
                enemy = Enemy(
                    name=enemy_data["name"],
                    hp=enemy_data["hp"],
                    damage=enemy_data["damage"],
                    xp_reward=enemy_data["xp"],
                    level=enemy_data["level"],
                )
                print(f"\n  Bir {enemy.name} karşına çıktı!")
            else:
                enemy = fled_enemies.pop(0)
                print(f"\n  {enemy.name} seni takip etti ve geri döndü!")
                print(f"  ({enemy.name} HP: {enemy.current_hp}/{enemy.max_hp})")

            battle = Battle(self.player, enemy)
            result = battle.start_battle()

            if result == "lose":
                return "lose"

            if result == "fled":
                # DÜZELTME 1 (KEŞİF RAPORU #3): enemy.current_hp = enemy.max_hp satırı silindi.
                # Canı sıfırlanmadan, azalan mevcut canıyla (current_hp) listeye ekleniyor.
                fled_enemies.append(enemy)
                print(f"  Kaçtın! Ama {enemy.name} peşini bırakmayacak...")
                continue

            if not self.player.is_alive():
                return "lose"

        print(f"\n  Bölüm {chapter_num} tamamlandı! İyi iş!")
        return "win"


    def start(self):
        self.setup()

        for chapter_num in range(1, 6):
            result = self.play_chapter(chapter_num)

            if result == "lose":
                print("\n" + "=" * 45)
                print("  OYUN BİTTİ. Bir sonraki sefere belki...")
                print("=" * 45)
                return

            if chapter_num < 5:
                required_level = chapter_num + 1
                if self.player.level < required_level:
                    print(f"\n  Bir sonraki bölüme geçmek için Level {required_level} olman gerekiyor!")
                    print(f"  Şu anki levelin: {self.player.level}. Yeterince XP kazanmadın!")
                    print("\n" + "=" * 45)
                    print("  OYUN BİTTİ. Daha güçlü ol ve tekrar dene!")
                    print("=" * 45)
                    return
                print(f"\n  Bir sonraki bölüme geçiliyor...")
                input("  [Devam etmek için Enter'a bas...]\n")

        print("\n" + "=" * 45)
        print("  TÜM BÖLÜMLER TAMAMLANDI! EFSANE KAHRAMAN!")
        print("=" * 45)
        self.player.show_stats()
