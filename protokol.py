#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. İŞYERİ ANİ KAÇIŞ VE EKRAN MASUMİYETİ GENEL MÜDÜRLÜĞÜ
Patron Gelince Alt+Tab Protokolü v1.0.0

Bu yazılım çalışır. Şaka değildir. Şakadır. İkisi birden.
"""

from __future__ import annotations

import random
import sys
import time
from datetime import datetime

# gizli not (base64): a2FyYXJuYW1lIGtva3VzdSBoZXIgeWVyZGUgYXluaQo=
# yukaridaki satiri cozmeyin. cozerseniz de ciddiye almayin.

TEHLIKE_SEVIYELERI = {
    1: "Uzaktan ayak sesi (belki komsu)",
    2: "Koridorda 'nasilsiniz' yankisi",
    3: "Kapı kolu 3 derece dondu",
    4: "Patronun kahve kokusu",
    5: "KIRMIZI ALARM: kapı açıldı",
}

MASUM_PENCERELER = [
    "Excel - Yillik Butce Gerceklesme (kesinlikle dolu)",
    "Outlook - Toplanti Notlari - Cok Onemli",
    "PDF: ISO 9001 Kalite El Kitabi sayfa 47",
    "Not Defteri - market listesi: sut, ekmek, haysiyet",
    "Tarayici: resmi mevzuat.gov.tr (gercekten acik)",
    "Hesap Makinesi - 2+2 hala 4, denetim gecti",
]

GERCEK_PENCERELER = [
    "YouTube - kedi dusuyor 3 saat",
    "Twitter / X - iş ile alakasiz thread",
    "Oyun: mayin tarlasi profesyonel lig",
    "Alisveris sepeti: mekanik klavye indirimi",
    "Grup sohbeti: 'patron geldi kac'",
]


def damga() -> str:
    return (
        "\n--- DAMGA / IMZA / TARIH ---\n"
        "Kayyum Grok · Tentivory · 22 Eylul 2026\n"
        "Ciddi ama ciddi degil. Resmi ama resmi degil.\n"
        "Eskisehir 4. Agir Ceza Mahkemesi kayyum karari geregi imzalanmistir.\n"
    )


def yavas_yaz(metin: str, gecikme: float = 0.012) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def tehlike_olc() -> int:
    # bilimsel yontem: rastgele ama resmi
    return random.randint(1, 5)


def alt_tab_uygula(seviye: int) -> str:
    if seviye >= 4:
        hedef = random.choice(MASUM_PENCERELER)
        return f"ALT+TAB uygulandi. Aktif pencere: {hedef}"
    if seviye >= 2:
        return "CTRL+WIN+D ile sanal masaustu acildi. Kimse bir sey gormedi."
    return "Tetik duruyor. Hala mayin tarlasindasin, dikkat."


def ana() -> None:
    print("=" * 64)
    print(" PATRON GELINCE ALT+TAB PROTOKOLU  |  ULUSAL SURUM 1.0.0")
    print("=" * 64)
    yavas_yaz("Sensörler kalibre ediliyor...")
    time.sleep(0.4)
    seviye = tehlike_olc()
    print(f"Tehlike seviyesi: {seviye}/5 — {TEHLIKE_SEVIYELERI[seviye]}")
    print(f"Onceki aktif pencere: {random.choice(GERCEK_PENCERELER)}")
    print(alt_tab_uygula(seviye))
    print(f"Islem zamani: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print("Sonuc: Ekran masumiyet belgesi duzenlendi.")
    print(damga())


if __name__ == "__main__":
    ana()
