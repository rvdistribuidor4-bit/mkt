# Convenios

Espacio de **uso exclusivo de Ricky** para todo lo relacionado con **nuevas negociaciones**
del **Centro de Ojos Lazarte** (oftalmología, Córdoba): convenios con financiadores, alianzas
institucionales, programas y las contrapartes de cada negociación.

## 🚀 Empezá por acá

1. **[`reporte-2026-09.md`](reporte-2026-09.md)** — panorama general y estrategia.
2. **[`estado-contactos.md`](estado-contactos.md)** — quién ya se contactó y con qué resultado (de los correos).
3. **[`base-datos-contactos.csv`](base-datos-contactos.csv)** — 📊 **la base de datos** (124 entidades, filtrable en Excel/Sheets).

## Frentes de negociación

| Frente | Carpeta / archivo | Estado |
|---|---|---|
| 🏛️ **Gerenciar Salud** (intermediaria) | [`gerenciar-salud.md`](gerenciar-salud.md) | 🟡 En negociación (a responder) |
| 🏥 **Financiadores directos** (prepagas / OOSS / ART) | [`base-datos-contactos.csv`](base-datos-contactos.csv) · [`estado-contactos.md`](estado-contactos.md) | 🟢 En curso (varios) |
| 👁️ **VER PARA VIVIR** (municipios + hogares) | [`ver-para-vivir/`](ver-para-vivir/) | 🔵 Diseñado, por lanzar piloto |
| 🧑‍🏭 **Sindicatos / patronales / colegios** | [`sindicatos/`](sindicatos/) | 🔵 Batería lista, envío parcial |
| ⚖️ **Transición jurídica** (Persona → Sociedad) | [`transicion-juridica/`](transicion-juridica/) | 🔵 Habilitador, por ejecutar |

## Estructura

```
convenios/
├── README.md                      ← este índice
├── reporte-2026-09.md             ← análisis general + estrategia + plan
├── estado-contactos.md            ← quién se contactó / quién no (de los correos)
├── base-datos-contactos.csv       ← BASE DE DATOS maestra (124 entidades)
├── gerenciar-salud.md             ← ficha: negociación con Gerenciar Salud
├── prepagas-nacionales.md         ← (primer borrador; superado por el CSV)
├── _plantilla-convenio.md         ← plantilla para cada negociación nueva
├── gerenciar-salud-fuentes/       ← xlsx original de Gerenciar (potenciales clientes)
├── ver-para-vivir/                ← programa salud visual adulto mayor (municipios/hogares)
│   ├── BRIEF_VER_PARA_VIVIR.md    ← documento maestro del programa
│   └── fuentes/                   ← dictamen, modelo de convenio, presentación
├── sindicatos/                    ← salud visual sindical 45+
│   ├── Bateria-8-Emails.md        ← 8 emails de apertura listos
│   └── fuentes/                   ← propuesta + presentación
└── transicion-juridica/           ← migración a persona jurídica (RUGEPRESA/ARCA/APROSS)
    └── fuentes/                   ← guía integral de transición
```

## Base de datos — cómo leerla

`base-datos-contactos.csv` (abrir en Excel/Google Sheets). Columnas:
**Categoría · Entidad · Email · Teléfono · Web/Portal · Córdoba · Prioridad · Estado · Último_contacto · Notas · Próximo_paso**

- **Estado:** Convenio vigente · En negociación · En curso · Enviado · Respondió · Rechazado · Email inválido (bounce) · Sin contactar.
- **Prioridad:** P1 (alta) · P2 (media) · P3 (baja/nicho).
- **Email "a relevar":** falta conseguir la dirección exacta (hay web/teléfono para hacerlo).

## Cómo agregar / actualizar

1. Nuevo prospecto → agregar fila en `base-datos-contactos.csv`.
2. Negociación que avanza → crear ficha propia con `_plantilla-convenio.md`.
3. Actualizar el `Estado` en el CSV a medida que avanza cada contacto.
