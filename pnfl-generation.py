
from datetime import datetime

def pnfl_yarat():
    print("=== PNFL Ommaviy Generator / Hisoblagich ===\n")
    
    # 1. Tug'ilgan sanani so'rash
    sana_str = input("Tug'ilgan sanangizni kiriting (YYYY-MM-DD, 2000-01-24): ").strip()
    try:
        sana = datetime.strptime(sana_str, "%Y-%m-%d")
    except ValueError:
        print("Xato: Sana formati Noto'g'ri! Iltimos, YYYY-MM-DD ko'rinishida kiriting.")
        return

    # 2. Jinsni so'rash
    jins = input("Jinsingizni kiriting (E - erkak / A - ayol): ").strip().upper()
    if jins not in ['E', 'A']:
        print("Xato: Jins noto'g'ri kiritildi! Faqat 'E' yoki 'A' deb yozing.")
        return

    # 3. Tuman / Hudud kodini so'rash (3 xonali)
    hudud_kodi = input("Hudud/Tuman kodini kiriting (3 xonali, masalan:518): ").strip()
    if not (hudud_kodi.isdigit() and len(hudud_kodi) == 3):
        print("Xato: Hudud kodi roppa-rosa 3 ta raqamdan iborat bo'lishi kerak!")
        return

    # 4. Nechigacha tartib raqami kerakligini so'rash
    limit_str = input("Nechta tartib raqamigacha generatsiya qilaylik? (masalan: 100): ").strip()
    if not (limit_str.isdigit() and 1 <= int(limit_str) <= 999):
        print("Xato: Son 1 va 999 orasida bo'lishi kerak!")
        return
    limit = int(limit_str)

    # --- A) 1-raqam: Jins va Asr indeksi ---
    yil = sana.year
    if 1800 <= yil <= 1899:
        birinchi_raqam = '1' if jins == 'E' else '2'
    elif 1900 <= yil <= 1999:
        birinchi_raqam = '3' if jins == 'E' else '4'
    elif 2000 <= yil <= 2099:
        birinchi_raqam = '5' if jins == 'E' else '6'
    else:
        print("Xato: Kiritilgan yil qamrov doirasida emas!")
        return

    # --- B) 2-7 raqamlar: DDMMYY formatida ---
    sana_kodi = sana.strftime("%d%m%y")

    print(f"\n--- 1 dan {limit} gacha bo'lgan PNFL ro'yxati ---")
    vaznlar = [7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7]

    # Tsikl orqali 1 dan kiritilgan songacha barchasini chiqarish
    for i in range(1, limit + 1):
        tartib_kodi = f"{i:03d}"
        
        # Dastlabki 13 ta raqamni birlashtirish
        dastlabki_13 = f"{birinchi_raqam}{sana_kodi}{hudud_kodi}{tartib_kodi}"
        
        # Nazorat raqamini hisoblash (Modul 10, vaznlar: 7, 3, 1)
        yigindi = sum(int(raqam) * vazn for raqam, vazn in zip(dastlabki_13, vaznlar))
        nazorat_raqami = yigindi % 10
        
        toliq_pnfl = f"{dastlabki_13}{nazorat_raqami}"
        print(f"Tartib {tartib_kodi}: {toliq_pnfl}")

if __name__ == "__main__":
    pnfl_yarat()
