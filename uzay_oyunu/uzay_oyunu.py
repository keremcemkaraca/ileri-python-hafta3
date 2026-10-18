import itertools
from typing import Iterator, Tuple, Iterable, Dict, List, Callable
from functools import lru_cache


def fibonacci() -> Iterator[int]:
    """Sonsuz fibonacci dizisi uretir."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Yakiti tuketim kadar azaltip kalani uretir."""
    guncel_yakit = yakit - tuketim
    while guncel_yakit >= 0:
        yield guncel_yakit
        guncel_yakit -= tuketim


def travel():
    """Oyun basinda yakit gostergesi olusturur ve deger ceker."""
    gosterge = yakit_gostergesi(100, 5)
    try:
        while True:
            kalan = next(gosterge)
    except StopIteration:
        print("Yakıtın bitti, uzayda sürükleniyorsun...")


def satirlari_oku(yol: str) -> Iterator[str]:
    """Dosyadan bos olmayan ve yorumsuz satirlari okur."""
    with open(yol, 'r', encoding='utf-8') as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if temiz and not temiz.startswith('#'):
                yield temiz


def ayristir(satirlar: Iterable[str]) -> Iterator[Tuple[str, str, int]]:
    """Satirlardan kaynak, hedef ve yakit bilgisi cikarir."""
    for satir in satirlar:
        parcalar = satir.replace('->', ' ').replace('>', ' ').split()
        if len(parcalar) == 3:
            yield (parcalar[0], parcalar[1], int(parcalar[2]))


def uzun_yolculuklar(kayitlar: Iterable[Tuple[str, str, int]], esik: int) -> Iterator[Tuple[str, str, int]]:
    """Yakiti esikten buyuk olan rotalari suzer."""
    return (k for k in kayitlar if k[2] > esik)


def rota_sayaci(baglantilar: Dict[str, List[str]]) -> Callable[[str, int], int]:
    """Verilen gezegenden baslayip n adimlik rotalari sayar."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1

        toplam = 0
        for komsu in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(komsu, adim - 1)

        return toplam

    return rota_sayisi