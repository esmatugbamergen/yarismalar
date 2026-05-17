# yarismalar
TYZT çatısı altında düzenlenen tüm yarışmaların repoları

### 🛠️ Çözülen Hatalar Raporu

| Dosya Adı | Bulunan Hata (Sorun) | Yapılan Düzeltme (Çözüm) | İlgili Keşif Raporu |
| :--- | :--- | :--- | :--- |
| **enemy.py** | `attack` fonksiyonunun ortasındaki erken `return 0` satırı altındaki kodların çalışmasını engelliyordu (Unreachable Code). Düşman hasar veremiyordu. | Erken `return 0` satırı kaldırıldı, düşmanın gerçek hasar hesaplama ve kritik vuruş mekaniği aktif edildi. | **KEŞİF RAPORU #3 / #7** |
| **character.py** | Seviye atlama (`level_up`) ödülleri `LEVEL_REWARDS` sözlüğünden doğrudan istenirken olmayan seviyeler için `KeyError` verip oyunu çökertiyordu. | Doğrudan erişim yerine `.get()` metodu kullanılarak güvenlik sağlandı. Ayrıca envanter listesi bellek çakışmasını önlemek için `__init__` içine taşındı. | **KEŞİF RAPORU #2 / #10** |
| **battle.py** | `enemy_turn` fonksiyonunun başında eksik iki nokta (`:`) vardı ve envanterden item kullanıldığında döngü kilitlenip sıra düşmana geçmiyordu. | Söz dizimi hatası (`:`) düzeltildi. İtem kullanımı başarıyla tamamlandığında sıranın düşmana geçmesi sağlandı ve felç durumları için ekrana bilgi eklendi. | **KEŞİF RAPORU #3 / #4** |
