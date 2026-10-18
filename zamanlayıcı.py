import time
from typing import Iterator

def zamanlayici(aralik: float) -> Iterator[float]:
    """Mesgul bekleme ile zaman olcer."""
    bas = time.time()
    while True:
        su_an = time.time()
        if su_an - bas >= aralik:
            yield su_an
            bas = su_an