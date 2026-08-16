# Sitio web personal de Edward H. H. — www.edwardhh.com

**Omar Eduardo Hernández Hernández** · Chihuahua, México
Futurista, consultor de alta dirección y comunicador.

Este repositorio contiene **únicamente** su sitio personal. No es iogga, no es
EdwCorp, no es la app.

| Proyecto | Repositorio | Dirección |
|---|---|---|
| **Sitio personal de Edward** | `ioggain/edwardhh` ← *estás aquí* | www.edwardhh.com |
| Sitio de iogga | `ioggain/iogga` | www.iogga.com |
| App de iogga (PWA) | `ioggain/iogga-app` | iogga.com |
| EdwCorp | `ioggain/edwcorp` | — |

No copies aquí archivos de esos proyectos ni empujes ramas suyas a este
repositorio.

---

## Cómo está construido

Un solo archivo `index.html` con la estructura, los estilos y el JavaScript
dentro. Sin React, sin Node, sin compilación, sin tipografías externas. Se
publica con GitHub Pages desde la rama `main`.

- **Bilingüe.** Cada texto existe dos veces, marcado por idioma:
  `<span data-l="es">…</span><span data-l="en">…</span>`. El CSS oculta el
  idioma inactivo. **Al editar un texto hay que cambiar las dos versiones.**
- **Rutas por hash.** Cada sección es un `<div class="route" data-route="…">`
  y se navega con `#/conferencias`, `#/kungfu`, etc. Al agregar una ruta nueva
  hay que registrar su título en el objeto `TITLES` del JavaScript.
- **Revelado al hacer scroll.** La clase `rv` anima un elemento al entrar en
  pantalla. Se respeta `prefers-reduced-motion`.
- **Fotos** en `assets/`, en blanco y negro que vuelve a color al pasar el
  cursor. `build-single.py` genera una copia de un solo archivo con las
  imágenes incrustadas, para compartir por correo o WhatsApp.

## Secciones

`#/inicio` · `#/vision` (incluye «La raíz», su fe) · `#/futuro` (+3 ensayos) ·
`#/ideas` · `#/conferencias` (catálogo de 70 temas) · `#/docencia`
(23 asignaturas) · `#/consultoria` · `#/proyectos` · `#/kungfu` ·
`#/biografia` · `#/contacto`

## Tono y contenido

El sitio proyecta visión internacional, no currículum. Editorial y
cinematográfico: negro profundo, serif grande, latón como acento, verde jade
solo en Kung Fu. Nada de lenguaje motivacional ni de consultora genérica.

Su diferenciador declarado es **visión + experiencia + comunicación**, y su
tesis propia es **la teoría de los tres relojes** (la tecnología corre, la
organización camina, la persona respira).

La sección «La raíz» declara su fe cristiana como algo que **une y no separa**.
Al tocarla, mantener ese tono: firme, sin predicar, sin excluir a nadie.

## Datos de contacto

- WhatsApp **+52 614 216 8738** → `wa.me/526142168738`
- Correo `hola@edwardhh.com` *(pendiente de crear en el dominio)*
- LinkedIn `/omareduardohh`

## Antes de dar por terminado un cambio

Revisar que las dos versiones de idioma quedaron iguales de actualizadas, que
no hay imágenes rotas y que no aparece desbordamiento horizontal en móvil.

## Dominio

El sitio se publica hoy en `ioggain.github.io/edwardhh/`. Para conectar
**www.edwardhh.com** hay que crear un archivo `CNAME` en la raíz con ese
dominio (el contenido está guardado en `CNAME.txt`) y apuntar el registro
CNAME de `www` a `ioggain.github.io` en GoDaddy.
