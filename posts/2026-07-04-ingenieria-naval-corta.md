---
fecha: 2026-07-04
sector: Ingeniería Naval
tipo: corta
estado: borrador
noticia_fuente: https://www.imo.org/en/ourwork/safety/pages/shipdesignandstability-default.aspx
fuentes_academicas: ["10.1016/j.oceaneng.2024.118901", "10.1016/j.marstruc.2025.103892"]
---

# Criterios de estabilidad intacta IMO de 2da generación: el fin de la "curva GZ estática" como único criterio

La OMI (SDC Sub-Committee) está finalizando los **Second Generation Intact Stability Criteria (SGISC)** — la mayor revisión del *Intact Stability Code (2008 IS Code)* en 16 años. Entrada en vigor estimada: **2028 obligatorio para nuevos건조**.

El cambio filosófico: **de criterios estáticos (área bajo curva GZ, ángulo de escora máx) a criterios dinámicos basados en física del movimiento en mar real.**

Cinco criterios nuevos que todo arquitecto naval debe conocer:

| # | Fenómeno | Criterio 1ra Gen (IS Code 2008) | Criterio 2da Gen (SGISC) |
|---|----------|--------------------------------|---------------------------|
| 1 | **Balance puro (dead ship)** | Área GZ > 0.055 m-rad | **Simulación en mar irregular** — probabilidad de escora > 30° < 5% |
| 2 | **Balance paramétrico** | No considerado explícitamente | **Modelo de Mathieu/Hill** — umbral GM variacional vs frecuencia de ola |
| 3 | **Surf-riding / Broaching** | No considerado | **Análisis de bifurcación** — velocidad crítica vs Froude number |
| 4 | **Water-on-deck (green water)** | Freeboard mínimo estático | **CFD/SPH simulado** — masa de agua en cubierta vs reserva de flotabilidad |
| 5 | **Viento severo + ola** | Heel moment viento estático | **Time-domain simulation** — combinación viento racha + ola de diseño |

**Lo que esto significa en la práctica:**
- **Ya no basta con Maxsurf/GHS/Hydrostatics** dando "área GZ OK". Necesitas **simulación en dominio del tiempo (WAMIT, ANSYS AQWA, OrcaFlex, Veres, ODT)** con espectros de ola (JONSWAP, Pierson-Moskowitz) y modelo de viento turbulento.
- **Buques de alto riesgo** (PCTC, Ro-Ro, pesqueros, offshore supply, naval) requieren **análisis Nivel 2 (simulación completa)**. Buques estándar pueden usar **Nivel 1 (fórmulas simplificadas calibradas)**.
- **Diseño de casco cambia:** Formas de casco que "pasan" criterio estático pueden fallar en paramétrico/broaching. La optimización de líneas (CFD + estabilidad) se vuelve **mandatoria, no opcional**.

En Perú, la DICAPI (Dir. Gral. de Capitanías) aún opera bajo IS Code 2008. Pero **cualquier buque que se construya en astillero extranjero para bandera peruana post-2028 deberá cumplir SGISC**. Y SIMA Callao, si quiere competir en mercado internacional, debe tener capacidad de análisis Nivel 2 **ya**.

**Mi recomendación:** Si diseñas o apruebas estabilidad de buques > 24m, **empieza a validar tus herramientas de simulación time-domain AHORA**. La curva de aprendizaje es 12-18 meses.

¿Tu oficina/astillero ya corre simulaciones de estabilidad en mar irregular (time-domain) o aún depende solo de GZ estática?

#IngenieríaNaval #IMO #EstabilidadIntacta #SGISC #SecondGenerationIntactStability #ArquitecturaNaval #Hidrodinámica #Buques #DICAPI #SIMA #Perú #NavalArchitecture

---

## 📚 FUENTES

**Noticia/Referencia:**
- [Ship Design and Stability — IMO](https://www.imo.org/en/ourwork/safety/pages/shipdesignandstability-default.aspx) — International Maritime Organization (2026)

**Papers académicos:**
- [Second generation intact stability criteria: Review and benchmarking for parametric rolling](https://doi.org/10.1016/j.oceaneng.2024.118901) — *Ocean Engineering* (2024)
- [Surf-riding and broaching criteria for second generation intact stability](https://doi.org/10.1016/j.marstruc.2025.103892) — *Marine Structures* (2025)

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

**Generar con Google Banana (Gemini Imagen 3):**
```
Technical naval architecture illustration comparing 1st vs 2nd generation intact stability criteria: Left panel — Traditional static GZ curve (righting arm vs heel angle) with shaded areas for "Area A > 0.055 m-rad", "Max GZ at 30°", "Downflooding angle". Right panel — Time-domain simulation in irregular waves: ship hull 3D model in wave field (JONSWAP spectrum), roll angle time history showing parametric roll resonance, broaching trajectory, green water on deck visualization. Annotations: "Level 2: Time-domain simulation required", "Parametric roll threshold", "Surf-riding bifurcation". Clean technical style, naval architecture blue/white palette, 16:9 aspect ratio, high detail, IMO document aesthetic.
```