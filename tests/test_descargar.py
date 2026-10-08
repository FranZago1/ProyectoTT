"""Descarga desde TikTok: reconocimiento de URLs (sin red)."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from carrusel.descargar import PATRON_TIKTOK  # noqa: E402


def test_urls_tiktok():
    for url, usuario, id_ in [
        ("https://www.tiktok.com/@quantgent/photo/7616778102257110294?_r=1", "quantgent", "7616778102257110294"),
        ("https://www.tiktok.com/@a.b_c/video/123", "a.b_c", "123"),
    ]:
        m = re.search(PATRON_TIKTOK, url)
        assert m and m.group(1) == usuario and m.group(2) == id_
    assert re.search(PATRON_TIKTOK, "https://www.instagram.com/p/abc/") is None
