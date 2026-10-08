"""Descarga de carruseles desde un link (TikTok, modo foto) a entrada/<slug>/.

TikTok no incluye el detalle de la publicación en el HTML de las URLs /photo/, pero sí en la misma
publicación pedida como /video/: el JSON embebido (__UNIVERSAL_DATA_FOR_REHYDRATION__) trae
imagePost.images[].imageURL.urlList con las imágenes originales (p. ej. 1080x1920).
Plan B: yt-dlp (si alguna versión futura soporta /photo/).
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path

from .comun import RAIZ, log

PATRON_TIKTOK = r"tiktok\.com/@([^/?#]+)/(?:photo|video)/(\d+)"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")


def _get(url: str, referer: str | None = None) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **({"Referer": referer} if referer else {})})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read(), r.geturl()


def resolver(url: str) -> tuple[str, str, str]:
    """Link corto o largo -> (url_canónica, usuario, id)."""
    _, final = _get(url)
    m = re.search(PATRON_TIKTOK, final)
    if not m:
        raise ValueError(f"No reconozco una publicación de TikTok en {final}")
    return final, m.group(1), m.group(2)


def _item_tiktok(usuario: str, id_: str) -> dict:
    """itemStruct de la publicación (probando /video/ y /photo/)."""
    for tipo in ("video", "photo"):
        html, _ = _get(f"https://www.tiktok.com/@{usuario}/{tipo}/{id_}")
        m = re.search(rb'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
        if not m:
            continue
        datos = json.loads(m.group(1))["__DEFAULT_SCOPE__"]
        item = datos.get("webapp.video-detail", {}).get("itemInfo", {}).get("itemStruct")
        if item:
            return item
    raise RuntimeError("TikTok no devolvió el detalle de la publicación (puede ser privada, borrada o "
                       "con restricción por región).")


def _plan_b_ytdlp(url: str, destino: Path) -> list[Path]:
    exe = shutil.which("yt-dlp") or str(RAIZ / ".venv" / "bin" / "yt-dlp")
    if not Path(exe).exists():
        return []
    subprocess.run([exe, "-q", "--no-warnings", "-o", str(destino / "%(autonumber)02d.%(ext)s"), url],
                   check=False)
    return sorted(p for p in destino.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"))


def descargar(url: str, slug: str | None = None) -> str:
    final, usuario, id_ = resolver(url)
    slug = slug or f"tiktok-{usuario}-{id_[-6:]}"
    destino = RAIZ / "entrada" / slug
    destino.mkdir(parents=True, exist_ok=True)
    for viejo in destino.iterdir():
        viejo.unlink()
    log(f"[descargar] {final}")
    archivos: list[Path] = []
    meta: dict = {"plataforma": "tiktok", "url": url, "url_canonica": final, "usuario": usuario, "id": id_}
    try:
        item = _item_tiktok(usuario, id_)
        imagenes = (item.get("imagePost") or {}).get("images") or []
        if not imagenes:
            raise RuntimeError("la publicación no es un carrusel de fotos (es un video)")
        meta.update(descripcion=item.get("desc", ""), autor=(item.get("author") or {}).get("nickname", usuario),
                    creada=item.get("createTime"))
        for i, im in enumerate(imagenes, start=1):
            for u in im["imageURL"]["urlList"]:
                try:
                    datos, _ = _get(u, referer="https://www.tiktok.com/")
                except Exception:
                    continue
                ext = ".png" if datos[:4] == b"\x89PNG" else (".webp" if datos[8:12] == b"WEBP" else ".jpg")
                ruta = destino / f"{i:02d}{ext}"
                ruta.write_bytes(datos)
                archivos.append(ruta)
                break
            else:
                raise RuntimeError(f"no se pudo bajar la imagen {i}")
        meta["metodo"] = "JSON embebido de la página (/video/)"
    except Exception as e:
        log(f"  método principal falló ({e}); pruebo yt-dlp")
        archivos = _plan_b_ytdlp(final, destino)
        meta["metodo"] = "yt-dlp"
        if not archivos:
            shutil.rmtree(destino, ignore_errors=True)
            raise SystemExit(f"No se pudieron obtener las imágenes de {url}: {e}")
    meta["imagenes"] = [p.name for p in archivos]
    (destino / "fuente.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"  {len(archivos)} imágenes en entrada/{slug}/ ({meta['metodo']})")
    return slug
