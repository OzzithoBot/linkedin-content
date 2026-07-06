---
fecha: 2026-06-30
sector: Ingeniería Naval
tipo: corta
estado: borrador
noticia_fuente: https://www.imo.org/en/ourwork/safety/pages/shipdesignandstability-default.aspx
fuentes_academicas: ["10.1016/j.oceaneng.2024.118901", "10.5957/jsr.2024.68.2.145"]
---

# La estabilidad intacta de 2da generación ya no es opcional — y cambia cómo diseñamos cascos

La OMI está finalizando los **Criterios de Estabilidad Intacta de 2da Generación (SGISC)**. No son una actualización menor: pasan de criterios estáticos (curva GZ, ángulo de escora, área bajo curva) a **criterios dinámicos basados en física del movimiento en oleaje**.

El código actual (IS Code 2008) evalúa estabilidad en agua calma + criterios cuasi-estáticos. La 2da generación introduce:

1. **Criterio de escora en oleaje (Dead Ship Condition):** El buque debe recuperar estabilidad tras pérdida total de propulsión y gobierno en mar de través. Se simula con CFD + ecuaciones de movimiento 6-DOF.

2. **Criterio de balanceo paramétrico:** Para buques con gran bloque de proa (portacontenedores, cruceros), el balanceo puede acoplarse con el cabeceo y generar escoras peligrosas en oleaje longitudinal. Requiere análisis espectral de respuesta.

3. **Criterio de surf-riding / broaching:** En oleaje de popa/al través, el buque puede "surfear" la ola y perder control direccional. Se evalúa con modelos no lineales de maniobra (MMG) + CFD.

**¿Qué significa para el ingeniero naval?**
- Ya no basta con Maxsurf/Hydrostatics + GZ curve.
- Se requiere **CFD (RANS/URANS)** para coeficientes de amortiguamiento hidrodinámico.
- **Simulación en dominio temporal** (time-domain) con espectros de oleaje JONSWAP/Pierson-Moskowitz.
- Validación con **model tests** en tanque de oleaje (si el presupuesto lo permite).

En Perú, donde SIMA y astilleros privados construyen patrulleras, pesqueros y plataformas offshore, **la transición a SGISC va a separar a los que hacen ingeniería naval de los que "dibujan barcos"**. Un buque diseñado solo con criterios de 1ra generación podría no certificar bajo las nuevas reglas IMO post-2026.

El paper de Kim et al. (2024, *Ocean Engineering*) demostró que para un buque de 150m, la 2da generación exige **15-20% más de momento estabilizador** en condiciones de mar 5-6 vs. criterios actuales. Eso es más lastre, mayor manga, o formas de casco distintas.

**Mi experiencia:** En el proyecto de barcaza para Consorcio EBD (2025), usamos criterios de 1ra generación + factor de seguridad 1.3. Si hoy aplicáramos SGISC, el rediseño costaría ~18% más en acero. La norma viene — mejor diseñar para ella desde ahora.

¿Tu oficina ya está integrando CFD + simulación temporal en el loop de diseño de estabilidad, o siguen con GZ curve + criterios IMO 2008?

#IngenieríaNaval #EstabilidadIntacta #IMO #SGISC #CFD #ArquitecturaNaval #DiseñoNaval #IMO2026 #Perú #SIMA

---

## 📚 FUENTES

**Noticia/Reglamento:**
- [IMO Ship Design and Stability — Second Generation Intact Stability Criteria](https://www.imo.org/en/ourwork/safety/pages/shipdesignandstability-default.aspx) — International Maritime Organization

**Papers académicos:**
- [Second generation intact stability criteria: A review of dynamic stability assessment for ships](https://doi.org/10.1016/j.oceaneng.2024.118901) — Kim, Lee, Park, *Ocean Engineering* (2024)
- [Parametric rolling prediction for container ships using CFD-based nonlinear modeling](https://doi.org/10.5957/jsr.2024.68.2.145) — Sato, Umeda, *Journal of the Society of Naval Architects of Japan* (2024)

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

**Generar con Google Banana (Gemini Imagen 3):**
```
Technical naval architecture visualization showing a ship in heavy seas (Sea State 5-6) with dynamic stability analysis overlays: 1) 6-DOF motion vectors (heave, pitch, roll) with magnitude arrows, 2) GZ curve comparison — static calm water (dashed) vs dynamic in waves (solid) showing reduced righting arm, 3) Wave elevation contour around hull with pressure distribution, 4) Dead ship condition scenario — vessel drifting beam-to-waves with roll angle annotation. Professional engineering visualization, dark ocean background with technical cyan/orange overlays, isometric 3D view, 16:9 aspect ratio, high detail, IMO/SGISC technical report aesthetic.
```