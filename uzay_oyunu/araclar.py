import time
from functools import wraps


def hamle_sayaci():
    """Her çağrıldığında bir artan sayaç döndürür."""
    sayac = 0

    def artir():
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def sure_olc(fonksiyon):
    """Bir fonksiyonun çalışma süresini ölçen sarmalayıcı (decorator)."""

    @wraps(fonksiyon)
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] {bitis - baslangic:.6f} saniyede çalıştı.")
        return sonuc

    return wrapper


@sure_olc
def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına (azalan) ve isme (alfabetik) göre sıralar."""
    baglantilar = galaksi["baglantilar"]

    sirali = sorted(
        galaksi["gezegenler"],
        key=lambda gezegen: (-len(baglantilar.get(gezegen, [])), gezegen)
    )
    return sirali