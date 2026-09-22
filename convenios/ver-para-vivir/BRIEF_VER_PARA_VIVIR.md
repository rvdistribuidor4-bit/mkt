# BRIEF DE TRASPASO — Programa VER PARA VIVIR
### Salud Visual Integral para el Adulto Mayor · Centro de Ojos Lazarte (Córdoba)
**Destinatario:** Claude Code (u otra sesión de Claude que continúe el trabajo)
**Fecha de compilación:** 22/07/2026 · **Estado:** 6 entregables producidos; pendiente completar precios reales, validación legal local y (opcional) rehacer presentaciones.

---

## 0. CÓMO USAR ESTE DOCUMENTO
Este archivo es autosuficiente: contiene todo el contexto, los datos, el marco jurídico, el contenido de cada entregable y las notas técnicas necesarias para **regenerar, editar o continuar** el proyecto sin depender de los binarios (.docx/.pptx) ni de la sesión original. Si vas a rehacer las presentaciones, leé primero la **Sección 9 (Nota técnica)**: hay un bug conocido de PowerPoint ya diagnosticado y resuelto.

---

## 1. ROL Y OBJETIVO
Actuar como equipo interdisciplinario (derecho sanitario y administrativo, geriatría, oftalmología, gestión hospitalaria, salud pública, economía de la salud, convenios institucionales, programas sociales, relaciones institucionales) para desarrollar un **programa permanente de prevención, diagnóstico precoz y tratamiento de enfermedades visuales en adultos mayores**, implementable desde un centro oftalmológico privado mediante convenios con instituciones de cuidado, municipios y financiadores. Debe ser **jurídicamente viable, económicamente sustentable e institucionalmente atractivo**, genérico y **replicable a toda Córdoba y luego al país**.

Patologías objetivo: **cataratas, glaucoma, degeneración macular (DMAE), retinopatías (incl. diabética), baja visión** y otras prevalentes.

---

## 2. DATOS DEL CLIENTE (usar en todos los documentos)
- **Institución:** Centro de Ojos Lazarte (privado, Córdoba Capital).
- **Trayectoria:** 35 años · **+15.000 cirugías de cataratas** · ~200 cirugías/mes.
- **Sedes:** Deán Funes 614 y 9 de Julio 778, Córdoba Capital.
- **Apoderado / firma:** Daniel Lazarte · **Tel.** 351 858-1902.
- **Convenios vigentes:** APROSS y PAMI (otros en desarrollo — ver proyecto de obras sociales).
- **Contacto usuario (autoría/identificación):** rvdistribuidor4@gmail.com

---

## 3. DECISIONES YA TOMADAS CON EL USUARIO
1. **Nombre del programa:** «VER PARA VIVIR — Salud Visual Integral para el Adulto Mayor». Alternativas: *Ojos que Cuidan*, *Mirada Mayor*, *Visión Plena*. Lema: **«Que ningún adulto mayor pierda la vista por no llegar a tiempo.»**
2. **Precios:** ilustrativos, con campos **[entre corchetes]** para completar con aranceles reales de la clínica y nomencladores PAMI/APROSS. **Aún NO hay precios reales cargados.**
3. **Alcance:** diseño **genérico y replicable** (sin piloto concreto todavía).
4. **Paquete:** los 9 puntos originales se consolidaron en **6 archivos** (ver Sección 6).
5. **Identidad visual:** teal `#0F6E6B` + teal oscuro `#0A4F4D` + ámbar `#B9770B`, fondos claros para contenido y oscuros para portada/cierre. Íconos: react-icons (set Feather).

---

## 4. MARCO JURÍDICO (verificado a jul-2026; requiere validación de asesor letrado local antes de firmar)
**Constitucional / convencional**
- **Ley 27.360** — Convención Interamericana sobre la Protección de los Derechos Humanos de las Personas Mayores. Núcleo del proyecto: derecho a la salud sin discriminación por edad, enfoque preventivo, trato diferenciado y preferente, **consentimiento informado**, servicios de cuidados de largo plazo. → Destinar recursos públicos a la salud visual del adulto mayor es **cumplimiento de una obligación jurídica, no una liberalidad** (blinda la decisión política).
- **CN** art. 42 (salud), art. 75 inc. 22 (jerarquía de tratados), inc. 23 (acciones positivas a favor de ancianos y personas con discapacidad).
- **CSJN «Campodónico de Beviacqua» (Fallos 323:3229)** — derecho a la salud operativo y exigible; el Estado (todos los niveles) es garante.

**Provincial (Córdoba)**
- **Constitución de Córdoba:** autonomía municipal (art. 180), competencia municipal en salud/asistencia social/discapacidad (art. 186 inc. 7), facultad de convenir (art. 190).
- **Ley Orgánica Municipal 8102** — competencias y facultad de convenir de municipios sin Carta Orgánica; vía ágil para pilotos en municipios/comunas chicos.
- **Ley 7872 + Decreto 657/09 + Resolución 394/09 (RUGEPRESA)** — habilitación, registro y fiscalización de residencias geriátricas; imponen obligaciones de cuidado de la salud del residente (el programa las ayuda a cumplir).
- **Plan Córdoba Mayor** — política provincial de adultos mayores; posible marco de articulación/financiamiento (a gestionar con la autoridad de aplicación).

**Discapacidad / ceguera evitable**
- **Leyes 22.431 y 24.901** — protección integral y prestaciones básicas; la ceguera evitable / baja visión severa habilita cobertura y justifica prioridad.

**Datos personales**
- **Ley 25.326** — los datos de salud son sensibles; compartir solo lo indispensable.

**Coberturas**
- **PAMI:** cubre cirugía de cataratas por facoemulsificación **al 100%, sin copago**, con lente intraocular **monofocal** estándar, honorarios, quirófano, anestesia y controles. Lentes premium (multifocal/tórica/EDOF) a cargo del afiliado. Requiere oftalmólogo autorizado + autorización online + estudios prequirúrgicos. **Población objetivo natural.**
- **APROSS:** red de prestadores + copago; Programa de Salud Visual (elementos ópticos cada 2 años). El Centro ya es prestador.
- **Otras OOSS/prepagas/cajas:** según convenio y nomenclador (ver proyecto de obras sociales de la clínica).

**Antecedentes reales**
- ✅ **Salta «Libre de Cataratas»** (municipio + fundación oftalmológica) — antecedente positivo directo.
- ✅ **General Alvear (Mendoza)** — cirugías gratuitas de cataratas.
- ✅ **APROSS Programa Salud Visual** — modelo provincial red + copago.
- ⚠️ **Necochea (Bs. As.)** — convenio RECHAZADO por el Concejo (9-9): se asoció a **contraprestación en especie** y **falta de estadísticas**. Lección: EVITAR subsidio nominativo y contraprestación en especie; **medir desde el día uno**.

**Arquitectura jurídica recomendada (componente municipal):** Ordenanza que crea el Programa + Convenio específico de prestaciones + Anexos. Lo que valida el gasto: fin público, pago **contra prestación documentada**, precio de referencia, selección conforme a contrataciones, control del Tribunal de Cuentas (controla legalidad/legitimidad, **no** oportunidad/mérito).

---

## 5. MODELO ECONÓMICO Y FINANCIAMIENTO
**Segmentación por cobertura del paciente:**
| Modelo | Paciente | Financia | Rol del programa |
|---|---|---|---|
| A | Afiliado PAMI | PAMI (100%, sin copago, monofocal) | Detecta, autoriza y opera en convenio PAMI |
| B | Afiliado APROSS | APROSS (red + copago) | Opera como prestador APROSS |
| C | Otra OOSS/prepaga/caja | OOSS s/ convenio y nomenclador | Canaliza por convenio |
| D | Particular con capacidad de pago | Paciente/familia | Precio institucional + prioridad |
| E | **Sin cobertura ni recursos** | Esquema solidario + municipio | Precio social + bonificación + saldo cofinanciado |

**Menú para Modelo E (combinable):** precio social · bonificación parcial del Centro (RSE, p. ej. 30–40%) · fondo solidario (recargo mínimo sobre A–D + donaciones) · subsidio municipal · programas provinciales/nacionales · donaciones/RSE de empresas · fundaciones · cooperadoras · campañas solidarias · financiamiento mixto.

**Regla de oro:** primero se agota la cobertura formal → luego precio social con bonificación del Centro → el municipio/fondo cubre el **saldo ya reducido** (nunca el precio total) contra prestación documentada.

**3 pilares de sostenibilidad:** (1) Autofinanciado (A–D genera volumen/rentabilidad) · (2) Solidario cruzado (recargo mínimo + fondo + RSE) · (3) Cofinanciado externo (municipios, provincia, fundaciones, empresas). A futuro: **Fundación VER PARA VIVIR** para administrar el fondo solidario con beneficios impositivos y transparencia.

**Convenio tripartito (Modelo E):** Centro (evaluación/cirugía/seguimiento a precio bonificado) + Municipio (verifica vulnerabilidad, admite al programa municipal, paga saldo) + Institución (detecta, deriva, acompaña, consentimiento y documentación).

**Circuito operativo (10 pasos):** 1 Detección → 2 Derivación → 3 Evaluación → 4 Diagnóstico → 5 Presupuesto → 6 Búsqueda de cobertura → 7 Intervención municipal (solo E) → 8 Cirugía/tratamiento (ambulatoria, ~15 min/ojo) → 9 Seguimiento (controles 1/7/30 días + anual) → 10 Alta y registro.

**Indicadores clave (medir desde el día uno):** instituciones conveniadas; residentes evaluados; cataratas detectadas; glaucomas diagnosticados; otras patologías; cirugías realizadas (y por vía de cobertura); pacientes con visión recuperada; mejora de agudeza visual; impacto en calidad de vida; reducción de caídas y de dependencia; costo por cirugía; tiempo detección→cirugía; tasa de seguimiento anual. Entregables: informe trimestral por institución + consolidado semestral por municipio.

**Matriz de riesgos (tipo → mitigación):** Legal (gasto público → ordenanza+convenio+prestación documentada, sin subsidio nominativo); Legal (consentimiento/datos → Ley 25.326); Administrativo (rechazo del Concejo, caso Necochea → estadísticas + municipio chico Ley 8102); Médico (complicaciones → lex artis, consentimiento, seguimiento); Institucional (baja adhesión → capacitación, referente, informes de valor); Económico (solidario supera capacidad → cupos, diversificación); Financiero (demoras de pago → cláusulas de plazo, no operar por encima de lo financiado); Reputacional (percepción de lucro → transparencia, informes públicos, RSE).

**Plan por fases:** Fase 0 Preparación (mes 0–1) · Fase 1 Piloto 6 meses (1–2 instituciones + 1 municipio/comuna chico) · Fase 2 Consolidación (mes 6–12, Gran Córdoba) · Fase 3 Expansión provincial (año 2, Ente de Municipios + Provincia) · Fase 4 Replicación nacional (año 3+, franquicia social con marca + manual + estándar de medición).

---

## 6. ENTREGABLES PRODUCIDOS (6 archivos, ya entregados al usuario)
Todos con identidad VER PARA VIVIR (teal/ámbar, Calibri). Contenido resumido para poder regenerarlos:

1. **01_Proyecto_Institucional_VER_PARA_VIVIR.docx** (23 pág) — portada, índice (TOC), aviso de uso, (1) resumen ejecutivo, (2) identidad del programa, (3) fundamentos (epidemiológico/social/jurídico), (4) objetivos general+8 específicos, (5) beneficios por actor (adulto mayor/familia, hogar, municipio, sistema sanitario, Centro), (6) marco jurídico completo, (7) modelos económicos A–E + estructura de costos ilustrativa, (8) alternativas sin cobertura, (9) intervención municipal + tripartito, (10) modelo operativo (circuito 10 pasos + modalidades), (11) modalidades de convenio, (12) indicadores, (13) financiamiento sostenible (3 pilares + fundación), (14) matriz de riesgos, (15) plan por fases, (16) expansión provincial, (17) replicación nacional, (18) conclusión + próximos pasos.
2. **02_Modelos_de_Convenio_VER_PARA_VIVIR.docx** (14 pág) — 6 modelos: (1) Convenio Marco, (2) Convenio Específico de Prestaciones, (3) Hogar/Residencia, (4) Geriátrico Privado, (5) Municipio/Comuna **+ proyecto de Ordenanza tipo**, (6) Tripartito. **Anexos:** I Nomenclador/precios (ilustrativo), II Protocolo de admisión socioeconómica, III Ficha de derivación, IV Planilla de rendición e indicadores, V Consentimiento informado. Campos [entre corchetes]. Todas las cláusulas estándar (objeto, obligaciones, precios/facturación, plazo, confidencialidad/Ley 25.326, responsabilidad/lex artis, rescisión con preaviso 60 días, jurisdicción Tribunales Ordinarios de Córdoba).
3. **03_Manual_Operativo_VER_PARA_VIVIR.docx** (12 pág) — objeto, actores y roles (el **referente institucional** es clave), circuito paso a paso (con responsable/documento/plazo), **protocolo de signos de alarma** (tabla con nivel de urgencia; regla: dolor intenso o pérdida brusca = URGENTE, contacto inmediato; resto = derivar), organización de jornadas (in situ / en clínica + checklist), gestión de cobertura A–E, subcircuito caso sin cobertura, seguimiento, documentación/registro, checklist de puesta en marcha.
4. **04_Presentacion_Municipios_VER_PARA_VIVIR.pptx** (10 slides) — pitch a intendentes/secretarías de salud: portada, problema, propuesta, beneficios municipio, es legal, cómo funciona, modelo económico, antecedentes (funciona vs evitar), piloto 6 meses, cierre/contacto.
5. **05_Presentacion_Hogares_VER_PARA_VIVIR.pptx** (8 slides) — pitch a directores de geriátricos/hogares/ONG: portada, problema en la institución, qué ofrecemos, beneficios institución, beneficios residentes/familias, capacitación/signos de alarma, cómo empezar, cierre/contacto.
6. **06_Propuesta_Comercial_VER_PARA_VIVIR.docx** (8 pág) — carta de presentación, quiénes somos, qué incluye, **planes** (Esencial / Integral / Municipal-Red), cómo se financia cada residente, para municipios/fundaciones/empresas (apadrinar cirugías/jornadas), cómo empezar.

**Planes comerciales (valores ilustrativos):**
| | Esencial | Integral | Municipal/Red |
|---|---|---|---|
| Para | Hogares chicos | Geriátricos medianos/grandes | Municipios, comunas, redes |
| Jornadas | [1]/trimestre | [1–2]/mes | s/ cronograma |
| Capacitación | Incluida | Incluida + refuerzos | En cada institución |
| Informes | Consolidado trim. | Por residente + consolidado | Por institución + global |
| Cofinanc. sin cobertura | Solidario | Solidario | Municipal + solidario |
| Valor coordinación | $[__]/período | $[__]/mes | Convenio marco |

---

## 7. CAMPOS [CORCHETES] A COMPLETAR ANTES DE PRESENTAR/FIRMAR
- Aranceles reales por prestación: consulta/evaluación, estudios prequirúrgicos (biometría), **cirugía de cataratas por ojo (lente monofocal)**, controles postoperatorios, seguimiento anual.
- Precio **particular** de referencia, **precio social**, y **% de bonificación** del Centro.
- Cupos y tope presupuestario por municipio; valores de coordinación de cada plan.
- Montos de «apadrinar una cirugía» y «apadrinar una jornada».
- Datos de cada institución/municipio (razón social, domicilio, representante, N.º RUGEPRESA, N.º de ordenanza).

---

## 8. PENDIENTES / PRÓXIMOS PASOS SUGERIDOS
1. Cargar precios reales (Sección 7) en Anexo I, modelo económico y propuesta comercial.
2. Validación legal local de convenios y ordenanza según Carta Orgánica del municipio elegido / Ley 8102 y umbrales de contratación.
3. Definir y lanzar **piloto de 6 meses** (1–2 instituciones + 1 municipio/comuna chico), con métricas desde el día uno.
4. Registrar nombre + isologotipo definitivos.
5. Redactar nota/email de presentación a secretarías de salud e instituciones (reutilizar tono del proyecto de obras sociales de la clínica).
6. (Opcional) Rehacer/editar presentaciones — ver Sección 9.

---

## 9. NOTA TÉCNICA — BUG DE POWERPOINT EN LOS .PPTX (diagnosticado y resuelto)
**Síntoma:** PowerPoint mostraba «PowerPoint encontró un problema con el contenido… ¿intentar reparar?». LibreOffice y python-pptx los abrían sin problema (por eso el PDF salía bien).

**Causa raíz:** los .pptx generados con **pptxgenjs** quedaron con `[Content_Types].xml` declarando **Override para slideMaster1…slideMasterN (uno por slide)**, pero en el paquete **solo existe `slideMaster1.xml`**. Esas referencias `Override` a partes inexistentes son lo que hace que PowerPoint intente reparar. **Nota:** el validador del skill pptx (`scripts/office/validate.py`) NO detectó este caso — no confiar solo en él para PowerPoint.

**Solución aplicada (reparación quirúrgica, sin tocar el diseño):** abrir el .pptx como zip, parsear `[Content_Types].xml`, **eliminar todo `<Override>` cuyo `PartName` no exista como parte real del paquete**, reescribir el zip. Script usado:
```python
import zipfile, shutil, os, sys
from defusedxml.minidom import parseString
def repair(path):
    zin = zipfile.ZipFile(path,'r'); names = zin.namelist()
    existing = set('/'+n for n in names)
    dom = parseString(zin.read('[Content_Types].xml').decode('utf-8'))
    root = dom.documentElement
    for ov in list(dom.getElementsByTagName('Override')):
        pn = ov.getAttribute('PartName')
        if pn and pn not in existing: root.removeChild(ov)
    tmp = path+'.r'; zout = zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
    for n in names:
        zout.writestr(n, dom.toxml().encode('utf-8') if n=='[Content_Types].xml' else zin.read(n))
    zout.close(); zin.close(); shutil.move(tmp,path)
repair(sys.argv[1])
```
**Verificación:** tras reparar, confirmar que (a) ningún `PartName` de Override apunta a parte inexistente, (b) hay 1 solo `slideMaster*.xml`, (c) `python-pptx` abre el archivo, (d) `validate.py` pasa. Ambos .pptx quedaron reparados y también se entregaron en **PDF** (que abren en cualquier dispositivo).

**Recomendación para Claude Code si rehace las presentaciones:** al generar con pptxgenjs, ejecutar el script de limpieza de `[Content_Types].xml` como paso final, o generar las diapositivas por otra vía (p. ej. plantilla .pptx editada, o entregar el deck en PDF/Google Slides/Canva). Mantener paleta teal `#0F6E6B` / ámbar `#B9770B` e íconos Feather para consistencia.

---

## 10. DOCUMENTOS RELACIONADOS EN EL PROYECTO "Proyectos ky" (contexto útil)
- `claude/programa-ver-para-vivir-salud-visual-adulto-mayor.md` — resumen de este programa.
- `claude/convenio-municipios-salud-visual.md` — trabajo previo de convenios municipales (dictamen + modelo + PPT).
- `claude/convenios-obras-sociales-cordoba.md` — plan de convenios con OOSS/sindicatos/cámaras (26 entidades, emails).
- `claude/personaje-avatar-videos-cataratas.md` — serie de contenido (avatar IA, mitos de cataratas).

---
*Fin del brief. Todo el contenido sustantivo está aquí; los .docx/.pptx/.pdf son la materialización de estas definiciones.*
