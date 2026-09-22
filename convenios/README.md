# Convenios

Espacio de **uso exclusivo de Ricky** para todo lo relacionado con **nuevas negociaciones**:
acuerdos comerciales, alianzas, contrapartes y condiciones.

Acá se registra cada negociación —desde el primer contacto hasta el cierre— con sus
términos, estados y próximos pasos. Independiente del trabajo por cliente en `clientes/`.

## Estructura

```
convenios/
├── README.md                 ← este índice
├── _plantilla-convenio.md    ← copiar para cada negociación nueva
├── reporte-2026-09.md        ← análisis de lo hecho + estrategia + plan
├── prepagas-nacionales.md    ← directorio nacional + estado de contacto
├── gerenciar-salud.md        ← ficha: negociación con Gerenciar Salud
└── <nombre-contraparte>.md   ← una ficha por negociación
```

> Contexto actual: las negociaciones en curso son para el cliente
> **Centro de Microcirugía Lazarte** (oftalmología, Córdoba). Empezar por
> `reporte-2026-09.md` para el panorama completo.

## Cómo agregar un convenio

1. Copiar `_plantilla-convenio.md` con un nombre claro (ej. `laboratorio-x.md`).
2. Completar los datos de la contraparte, términos y estado.
3. Agregar la fila en la tabla de abajo.
4. Commitear con un mensaje descriptivo.

## Negociaciones

| Contraparte | Rubro | Tipo de convenio | Estado | Ficha |
|---|---|---|---|---|
| Grupo Gerenciar Salud | Gerenciadora de convenios | Incorporación a su red de financiadores | 🟡 En negociación (a responder) | [`gerenciar-salud.md`](gerenciar-salud.md) |
| Prepagas nacionales (campaña directa) | Financiadores | Convenio prestacional directo | 🔵 Por iniciar | [`prepagas-nacionales.md`](prepagas-nacionales.md) |

**Leyenda de estado:** 🟢 Cerrado · 🟡 En negociación · 🔵 Contacto inicial · 🔴 Pausado/Caído
