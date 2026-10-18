from functools import reduce, partial

galaksi = {
    "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
    "baglantilar": {
        "dünya": ["sirius", "centauri"],
        "centauri": ["orion"],
        "sirius": ["orion", "kara_delik"],
        "orion": ["sirius", "centauri", "dünya"],
        "kara_delik": []
    }
}

yontem1_buyuk_harf = list(map(str.upper, galaksi["gezegenler"]))
yontem2_buyuk_harf = [g.upper() for g in galaksi["gezegenler"]]

yontem1_ikili_bag = list(filter(lambda g: len(galaksi["baglantilar"].get(g, [])) >= 2, galaksi["gezegenler"]))
yontem2_ikili_bag = [g for g in galaksi["gezegenler"] if len(galaksi["baglantilar"].get(g, [])) >= 2]

yontem1_toplam_bag = reduce(lambda acc, g: acc + len(galaksi["baglantilar"].get(g, [])), galaksi["gezegenler"], 0)
yontem2_toplam_bag = sum(len(k) for k in galaksi["baglantilar"].values())
def yolculuk(kaynak: str, hedef: str, hiz: int = 1):
    """Yolculuk islevi"""
    return f"{kaynak} -> {hedef} hiz: {hiz}"

hizli_yolculuk = partial(yolculuk, hiz=3)