# edwardhh.com — sitio personal de Edward H. H.

Sitio estático, bilingüe (ES/EN), sin dependencias, sin build obligatorio y sin
servicios de terceros. Se abre haciendo doble clic en `index.html`.

**Proyecto independiente.** No comparte código, dominio ni despliegue con iogga,
iogga-app ni EdwCorp.

---

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | El sitio completo: estructura, estilos y JavaScript en un solo archivo. |
| `assets/` | Las fotografías. |
| `build-single.py` | Genera `edwardhh-preview.html`: una copia con las fotos incrustadas, en un solo archivo, para enviar por correo o WhatsApp. |
| `edwardhh-preview.html` | Resultado del script anterior. Se puede compartir tal cual. |

Para regenerar la copia de un archivo, tras cambiar textos o fotos:

```bash
python3 build-single.py
```

---

## Cómo está construido

- **Un solo archivo.** Sin React, sin Node, sin compilación. Se edita con
  cualquier editor de texto y se sube por FTP, GitHub Pages, Netlify o Vercel.
- **Sin tipografías externas.** Usa las fuentes del sistema, así que carga al
  instante y funciona aunque no haya conexión con Google.
- **Bilingüe real.** Cada texto existe en español y en inglés dentro del HTML.
  El botón ES/EN cambia todo el sitio sin recargar y recuerda la elección.
  Si el visitante llega con el navegador en inglés, el sitio abre en inglés solo.
- **Navegación por rutas.** Cada sección tiene su dirección propia
  (`edwardhh.com/#/conferencias`), así que se pueden compartir enlaces directos.

### Secciones

`#/inicio` · `#/servicios` · `#/ideas` · `#/trayectoria` · `#/proyectos` ·
`#/raiz` · `#/contacto`

Más tres rutas de ensayo: `#/futuro/tres-relojes`, `#/futuro/decada-atencion`
y `#/futuro/regreso-del-oficio`.

`#/servicios` reúne conferencias (catálogo de 70 temas), consultoría y docencia.
`#/raiz` reúne fe, kung fu, música y plantas.

---

## Cómo editar

### Cambiar un texto

Cada frase aparece dos veces, marcada por idioma:

```html
<span data-l="es">El futuro no se predice.</span>
<span data-l="en">The future is not predicted.</span>
```

Se edita el texto de adentro. **Hay que cambiar las dos versiones**, o una
quedará desactualizada.

### Cambiar una foto

Se reemplaza el archivo dentro de `assets/` conservando el mismo nombre. Si el
nombre cambia, hay que actualizarlo también en `index.html`.

### Agregar un artículo nuevo a «Futuro»

1. Copiar un bloque completo `<div class="route" data-route="futuro/...">`.
2. Cambiar el identificador de la ruta y los textos.
3. Agregar el enlace en el índice (`data-route="futuro"`).
4. Agregar el título en el objeto `TITLES` del JavaScript, al final del archivo.

---

## Publicar el sitio

Cualquiera de estas tres opciones sirve. La más simple es Netlify.

**Netlify (sin conocimientos técnicos).** Entrar a netlify.com, arrastrar la
carpeta completa a la ventana, y conectar el dominio `edwardhh.com` en
*Domain settings*.

**GitHub Pages.** Subir la carpeta a un repositorio nuevo, activar Pages en
*Settings → Pages*, y agregar un archivo `CNAME` con el texto `www.edwardhh.com`.

**Hosting tradicional.** Subir `index.html` y la carpeta `assets/` por FTP a la
raíz del sitio.

En los tres casos, en el panel del dominio hay que apuntar los registros DNS al
proveedor elegido.

---

## Pendientes antes de publicar

1. **Crear el correo `hola@edwardhh.com`.** El sitio ya lo usa. Mientras no
   exista, el único canal que funciona es WhatsApp. Casi todos los proveedores
   de dominio incluyen el correo sin costo adicional.
2. **Revisar los textos.** Los ensayos de la sección «Futuro», las ideas del
   cuaderno y las descripciones de conferencias son borradores escritos a partir
   del currículum. Dicen cosas en nombre de Edward y deben aprobarse o
   reescribirse antes de que el sitio sea público.
3. **Confirmar el teléfono.** El sitio anterior publicaba +52 6146 88 72 71 y el
   sitio actual usa 614 216 8738. Hay que verificar cuál es el correcto.

---

## Fotografías

26 imágenes recuperadas de los PDF a su resolución original y optimizadas para web.

| Archivo | Dónde se usa |
|---|---|
| `retrato.jpg` | Portada y biografía — retrato de estudio |
| `escenario-reloj.jpg` | Portada, bloque de la tesis |
| `panel-visionarios.jpg` | Ideas |
| `logo-omah.png` | Kung Fu y Proyectos |
| `kungfu-patada.jpg` | Kung Fu, apertura |
| `kungfu-forma.jpg`, `kungfu-duo.jpg`, `kungfu-campo.jpg`, `kungfu-bruce.jpg` | Kung Fu, seminarios |
| `logo-iogga.png`, `logo-edwcorp.png` | Proyectos, marcas |
| `iogga-escenario.jpg`, `iogga-pitch.jpg` | Proyectos, bloque de iogga |
| `taller-herradura.jpg` | Conferencias, catálogo |
| `taller-lasalle.jpg` | Conferencias, formatos |
| `consejo-inndech.jpg` | Conferencias, apertura |
| `sala-juntas.jpg`, `aula-grupo.jpg`, `taller-cerca.jpg` | Docencia |
| `italia.jpg`, `grupo-equipo.jpg` | Biografía |
| `musica.jpg` | Biografía, «Fuera del escenario» |
| `comunidad.jpg` | Visión → La raíz, sección de fe |
| `plantas.jpg` | La raíz, «Fuera del escenario» |
| `musica-guitarra.jpg` | La raíz, «Fuera del escenario» |
| `musica-instrumentos.jpg`, `musica-coro.jpg`, `musica-piano.jpg` | La raíz, fila de música |
| `meditacion.jpg`, `parado-cabeza.jpg` | La raíz, bloque de kung fu |
| `logo-edwardhh.png` | Barra superior |
| `logo-simbolo.png` | Disponible para redes y papelería |
| `favicon-32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` | Iconos del navegador |
| `aula-mesa.jpg`, `taller-sala.jpg`, `start-why.jpg`, `spaceapps.jpg`, `kungfu-saludo.jpg`, `kungfu-bn.jpg`, `podio.jpg`, `retrato-bn.jpg` | Disponibles, sin colocar |

### Cómo mandar fotos nuevas

Las imágenes pegadas en el chat **no llegan al servidor**; solo llegan PDF y HTML.
Hay que insertarlas en un documento de Google Docs o Word y descargarlo como PDF.
Se recuperan a resolución original, sin pérdida.

### Lo que aún se puede sumar

1. **Kung fu enseñando**, corrigiendo la postura de un alumno.
2. **Con plantas**, luz natural, sin pose.
3. **Con la guitarra**, sin mirar a la cámara.
4. **Capturas de pantalla de la app iogga.**

El sitio muestra las fotos en blanco y negro y las devuelve a color al pasar el
cursor, así que no hace falta editarlas antes de enviarlas.

---

© Omar Eduardo Hernández Hernández — Chihuahua, México.
