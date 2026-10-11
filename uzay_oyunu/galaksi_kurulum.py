import json


def galaksi_kur(gezegenler: list, baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """JSON'dan alınan verilerle galaksiyi kurup bir sözlük döndürür."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok.")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }


if __name__ == "__main__":
    with open("galaksi.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    g = galaksi_kur(**veri)
    print("Konum ve Yakıt:", (g["konum"], g["yakit"]))