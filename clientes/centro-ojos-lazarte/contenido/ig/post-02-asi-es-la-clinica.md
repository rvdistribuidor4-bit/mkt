# Carrusel institucional · «Así es el Centro de Ojos Lazarte»

**Formato:** carrusel de 6 placas, 1080 × 1350 px
**Archivos:** `placa-clinica-1-portada.jpg` … `placa-clinica-6-cierre.jpg`
**Fuente editable:** `carrusel-clinica.html` + `render_placas_foto.py`
**Costo de producción:** US$0 — fotos reales del cliente, HTML renderizado

---

## Por qué este post

Es el que la cuenta no tiene y más falta le hace. **El paciente de oftalmología
llega con miedo**: no sabe si el lugar es serio, si lo van a atender bien, si
tiene los equipos. Mostrarle el lugar antes de que venga baja esa barrera más
que cualquier placa de consejos.

Además es el tipo de contenido que **genera guardados y visitas al perfil**, que
es exactamente lo que necesita una cuenta de 28 seguidores: no más likes, sino
gente que entra a ver quién sos.

Y sirve de **post anclado**: explica qué es la clínica y no caduca nunca.

## Las seis placas

| # | Foto | Mensaje |
|---|---|---|
| 1 | Sala de espera | *Antes de venir, mirá dónde vas a estar* |
| 2 | Admisión | *Acá empieza tu turno* · PAMI, obras sociales y particulares |
| 3 | Pasillo | *Dos sedes en el centro de Córdoba* |
| 4 | Consultorio | *Donde se hace el control* |
| 5 | Equipos | *Equipamiento para estudios de alta complejidad* |
| 6 | Consultorio con lámpara | *Más de 35 años cuidando la vista de Córdoba* + CTA |

## Texto del posteo

```
¿Nunca viniste? Mirá dónde vas a estar 👁️

Sabemos que ir al oftalmólogo por primera vez da un poco de cosa: no sabés
cómo es el lugar, ni con qué te vas a encontrar. Así que te lo mostramos.

Admisión, sala de espera, consultorios y el equipamiento para estudios de
alta complejidad — todo en el mismo lugar donde te atendés.

Dos sedes en el centro de Córdoba:
📍 Deán Funes 614 (centro integral)
📍 9 de Julio 778 (consultorios externos)

Atendemos PAMI, obras sociales y particulares.
Más de 35 años cuidando la vista de los cordobeses.

📲 Turnos y consultas por WhatsApp — link en la bio

#oftalmología #córdoba #saludvisual #centrodeojoslazarte #cirugíadecataratas
```

## Textos alternativos (accesibilidad)

1. Sala de espera del Centro de Ojos Lazarte, con sillones rojos.
2. Mostrador de admisión de pacientes, con cartel de atención PAMI gratuita.
3. Pasillo con sillas de espera a lo largo de la pared.
4. Consultorio con lámpara de hendidura, sillón de examen y cartel de agudeza visual.
5. Sala con dos equipos de diagnóstico oftalmológico con pantalla.
6. Consultorio con lámpara de hendidura sobre unidad de refracción.

## Verificaciones hechas

- **Ninguna foto tiene pacientes ni personas identificables.** Revisado uno por
  uno, incluido el borde derecho del pasillo.
- **Ninguna afirmación de resultado ni superlativo.** El post describe
  instalaciones, no promete nada. No lleva disclaimer porque no da información
  médica.
- «Estudios de alta complejidad» y «más de 35 años» son de la propia
  comunicación del cliente, no inventados acá.
- ⚠️ Una foto estaba mal etiquetada por mí como `microscopio-quirurgico`: es una
  **lámpara de hendidura sobre unidad de refracción**, no un microscopio de
  cirugía. Renombrada a `consultorio-lampara`. El copy nunca dijo «quirófano».

## Cómo volver a generarlo

```bash
cd clientes/centro-ojos-lazarte/contenido/ig
python3 render_placas_foto.py carrusel-clinica.html
```

## Lo que sumaría

- **La fachada de las dos sedes.** Es lo que busca el paciente para saber que
  llegó al lugar correcto, y es la única foto del recorrido que falta.
- **El Dr. Lazarte y el equipo**, con consentimiento escrito.
