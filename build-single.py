"""Genera una version de un solo archivo (imagenes incrustadas) para previsualizar y compartir."""
import base64, os, re, sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(SRC), "edwardhh-preview.html")

html = open(SRC, encoding="utf-8").read()

def inline(m):
    path = os.path.join(os.path.dirname(SRC), m.group(1))
    if not os.path.exists(path):
        return m.group(0)
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp", "svg": "svg+xml"}.get(ext, ext)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return 'src="data:image/%s;base64,%s"' % (mime, b64)

html = re.sub(r'src="((?:assets)/[^"]+)"', inline, html)

# En la vista previa, el titulo estatico es solo el nombre: asi aparece en la galeria.
# El sitio real conserva su titulo completo para buscadores, y el router lo repone al cargar.
html = html.replace("<title>Edward H. H. — Futurista, consultor y comunicador</title>",
                    "<title>Edward H. H.</title>", 1)

open(OUT, "w", encoding="utf-8").write(html)
print(OUT, os.path.getsize(OUT), "bytes")
