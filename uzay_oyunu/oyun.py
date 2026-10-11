def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun envanterindeki eşyaları formatlı bir metin olarak döndürür."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hızlı motor")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandırılmış bir menü metni olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)