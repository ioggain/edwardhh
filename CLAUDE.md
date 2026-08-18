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

Seis apartados, en este orden y con este peso deliberado:

| Ruta | Qué contiene | Peso |
|---|---|---|
| `#/inicio` | Portada, tesis, tríada del diferenciador, credenciales | — |
| `#/servicios` | Conferencias (catálogo de 70 temas), consultoría y docencia | 30 % |
| `#/ideas` | Tesis de la traducción, 3 ensayos de prospectiva, cuaderno de ideas | 30 % |
| `#/trayectoria` | Carrera, formación, certificaciones y principios de trabajo | 20 % |
| `#/proyectos` | iogga, EdwCorp, OMAH Kung Fu | 10 % |
| `#/raiz` | Fe, kung fu, música, plantas | 10 % |
| `#/contacto` | WhatsApp, correo, LinkedIn y formulario | — |

Los ensayos viven en rutas propias (`#/futuro/tres-relojes`,
`#/futuro/decada-atencion`, `#/futuro/regreso-del-oficio`) y regresan a
`#/ideas`.

**No volver a multiplicar los apartados.** Él pidió expresamente menos
secciones: su filosofía es que lo verdaderamente intuitivo no necesita manual.
Antes de crear una ruta nueva, buscar dónde encaja en las seis existentes.

## Tono y contenido

El sitio proyecta visión internacional, no currículum. Editorial y
cinematográfico: negro profundo, serif grande, latón como acento, verde jade
solo en Kung Fu. Nada de lenguaje motivacional ni de consultora genérica.

Su diferenciador declarado es **visión + experiencia + comunicación**, y su
tesis propia es **la teoría de los tres relojes** (la tecnología corre, la
organización camina, la persona respira).

### Regla de voz: humildad (obligatoria)

Él pidió expresamente que **no se note presunción en ningún texto**. La regla
es pasar del *yo hago* al *el oficio consiste en*:

- Los titulares van en **infinitivo**, no en primera persona:
  «Ejecutar, no sólo opinar», no «He ejecutado».
- Las capacidades se enuncian de forma **impersonal**: «se diseña», «ahí se
  aprende», «el oficio consiste en», «de ahí salen los seminarios».
- Nada de compararse con otros ni de descalificarlos: se dice «el oficio no
  consiste en repetir informes de consultoras», no «yo no repito informes».
- Los logros se enuncian como **hechos verificables**, no como méritos:
  fechas, instituciones, grados, cargos. El dato habla solo.
- **Excepción:** en los ensayos de `#/futuro/*` y en la sección «La raíz» la
  primera persona sí es natural, porque ahí escribe y confiesa, no se vende.

Antes de dar por buena una frase nueva, leerla en voz alta: si suena a que
está presumiendo, se reescribe.

La sección «La raíz» declara su fe cristiana como algo que **une y no separa**.
Al tocarla, mantener ese tono: firme, sin predicar, sin excluir a nadie.

Distinción que él pide sostener siempre: **religión** con minúscula es lo que
construyó el hombre (estructuras, marcas, denominaciones, sucursales);
**Religión** con mayúscula es la del amor, definida en Santiago 1:27. Pertenece
a una comunidad cristiana sin nombre, sin bandera y sin sucursales, en Chihuahua
y en México, en comunión con una iglesia en Chile y con hermanos en Argentina,
Miami y otros países. No mencionar denominaciones ni figuras públicas.

**Kung Fu:** el linaje que aparece en `#/kungfu` es real y verificable
(Ed Parker y James Wing Woo → James Ibrao → Ever Chaparro Mendoza →
Dr. José Guadalupe Becerril López → Edward). No inventar grados ni fechas.
Instagram del proyecto: https://www.instagram.com/omahkungfu/

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
