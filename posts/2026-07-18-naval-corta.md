---
fecha: 2026-07-18
sector: Ingeniería Naval
tipo: corta
estado: borrador
noticia_fuente: https://www.imo.org/en/ourwork/safety/pages/shipdesignandstability-default.aspx
fuentes_academicas: https://doi.org/10.1007/978-3-031-16329-6_2
---

# Los criterios de estabilidad intacta de segunda generación de la IMO: lo que cambió y por qué importa para el diseño de buques

Después del hundimiento de varios buques de carga por falla de estabilidad (incluyendo el caso de la bodega de carga vacía en mar), la IMO desarrolló los Second Generation Intact Stability Criteria (SGISC), adoptados en 2019 pero todavía en fase de implementación.

La versión actual del IS Code 2008 exige 7 criterios básicos:
1. Área bajo GZ ≥ 0.055 m-rad hasta 30°
2. Área hasta 40° ≥ 0.09 m-rad
3. Área entre 30° y 40° ≥ 0.03 m-rad
4. GZ máx ≥ 0.20 m a ángulo ≥ 30°
5. Ángulo de GZ máx ≥ 25°
6. GM inicial ≥ 0.15 m
7. Criterio de viento y balanceo (weather criterion)

Los SGISC van más allá: introducen criterios de vulnerabilidad para cinco modos de falla:
- **Deadship condition** (estabilidad en barco sin propulsión)
- **Parametric rolling** (balanceo paramétrico en cargas homogenias)
- **Broaching** (pérdida de gobierno en ola de popa)
- **Exceso de velocidad de balanceo** (severely catech astern seas)
- **Movimiento de carga en bahas** (water on deck / sloshing)

Un paper de Springer (Umeda & Francescutto, 2023) señala que la implementación de los SGISC todavía tiene problemas no resueltos: las explanatory notes no están completamente finalizadas y hay debates sobre la definición de "buque vulnerable" vs. "buque robusto."

**Para el cálculo de estabilidad en proyectos de баркас y захвата en Perú:** el software de estabilidad de SIMA usa el IS Code 2008 como base. Pero para nuevos diseños de buques de carga, los SGISC deben evaluarse como criterio adicional — especialmente si se trata de баркасы con cargas homogenias o diseños con bajo GM.

¿Tu cálculo de estabilidad incluye ya los SGISC o sigue siendo solo IS Code 2008?

#IngenieríaNaval #EstabilidadNaval #IMO #ISCode #SGISC #DiseñoNaval #Perú

---

## 📚 FUENTES

**Noticia:**
- IMO Ship Design and Stability — International Maritime Organization https://www.imo.org/en/ourwork/safety/pages/shipdesignandstability-default.aspx

**Papers:**
- Umeda & Francescutto, "The Second Generation Intact Stability Criteria—Achievements and Remaining Issues" — Springer (2023) https://doi.org/10.1007/978-3-031-16329-6_2
- Shipsbusiness.com, "IMO Intact Stability Criterion & Safe Return to Port" — shipsbusiness.com

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

Curva GZ de un buque de carga mostrando los 7 criterios del IS Code 2008 con líneas punteadas indicating límites mínimos, y una insert mostrando la comparación con los nuevos umbrales SGISC. Estilo técnico naval, formato 16:9.