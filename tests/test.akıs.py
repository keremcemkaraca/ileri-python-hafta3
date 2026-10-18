import pytest
import itertools
from uzay_oyunu.akis import fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar, rota_sayaci


def test_fibonacci():
    g = fibonacci()
    assert [next(g), next(g), next(g)] == [0, 1, 1]

    l1 = list(itertools.islice(g, 12))
    l2 = list(itertools.islice(g, 12))
    assert l1 != l2

    g2 = fibonacci()
    assert list(itertools.takewhile(lambda x: x < 100, g2)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_yakit():
    g = yakit_gostergesi(100, 30)
    assert list(g) == [70, 40, 10, 0]

    g2 = yakit_gostergesi(10, 5)
    next(g2)
    next(g2)
    with pytest.raises(StopIteration):
        next(g2)


def test_boru_hatti(tmp_path):
    icerik = "dünya -> sirius 12\n#bakım molası\norion > sirius 8"
    dosya = tmp_path / "seyir.txt"
    dosya.write_text(icerik, encoding="utf-8")

    sonuc = list(uzun_yolculuklar(ayristir(satirlari_oku(str(dosya))), 10))
    assert sonuc == [("dünya", "sirius", 12)]


def test_rota():
    galaksi = {
        "baglantilar": {
            "dünya": ["sirius", "centauri"],
            "centauri": ["orion"],
            "sirius": ["orion", "kara_delik"],
            "orion": ["sirius", "centauri", "dünya"],
            "kara_delik": []
        }
    }
    say = rota_sayaci(galaksi["baglantilar"])
    assert say("dünya", 3) == 9