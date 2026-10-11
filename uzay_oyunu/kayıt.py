def gorev_kaydi(baslik: str, *adimlar, oncelik: str = "normal", **ekler) -> None:
    """Görev detaylarını ve adımlarını ekrana yazdırır."""
    print(f"[{oncelik.upper()}] {baslik}")

    for i, adim in enumerate(adimlar, 1):
        print(f"{i}. {adim}")

    for anahtar, deger in ekler.items():
        print(f"{anahtar}: {deger}")


if __name__ == "__main__":
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler_sozlugu = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adimlar_listesi, oncelik="yüksek", **ekler_sozlugu)