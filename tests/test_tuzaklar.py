# (a) Hatalı fonksiyon
def yakit_ekle_hatali(miktar, depo=[]):
    depo.append(miktar)
    return depo

# (a) None kalıbı ile düzeltilmiş hali
def yakit_ekle_duzeltilmis(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle_hatasi():
    """Hatalı fonksiyonun listeyi bellekte tuttuğunu kanıtlar."""
    yakit_ekle_hatali(10)
    depo2 = yakit_ekle_hatali(20)
    # Hata: İkinci çağrıda depo [20] olmalıydı ama [10, 20] oldu
    assert depo2 == [10, 20]

def test_yakit_ekle_duzeltilmis():
    """Düzeltilmiş fonksiyonun her seferinde sıfırdan liste açtığını test eder."""
    depo1 = yakit_ekle_duzeltilmis(10)
    depo2 = yakit_ekle_duzeltilmis(20)
    assert depo1 == [10]
    assert depo2 == [20]