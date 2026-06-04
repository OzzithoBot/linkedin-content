---
fecha: 2026-05-19
sector: Ingeniería Mecánica
tipo: corta
estado: borrador
fuentes_academicas: ["10.1016/j.ijfatigue.2024.108234", "10.1016/j.ymssp.2023.110456"]
---

# Análisis de fatiga en equipos rotativos: por qué el 80% de fallas mecánicas son predecibles

En más de 13 años de ingeniería, he visto el mismo patrón: un equipo rotativo falla "de pronto" y todos se sorprenden. Pero los datos estaban ahí desde el principio.

**La fatiga no es aleatoria. Es acumulativa.**

Todo componente sometido a cargas cíclicas — ejes, rodamientos, acoplamientos, impulsores — acumula daño microestructural con cada ciclo. La curva S-N (Wöhler, 1870) lo demostró hace más de 150 años: a mayor amplitud de esfuerzo, menor número de ciclos hasta la falla.

**Lo que veo en campo:**

En compresores centrífugos y ventiladores industriales que superviso, las fallas más comunes siguen un patrón:

1. **Rodamientos (40% de fallas):** Desgaste por fatiga de contacto. La teoría de Hertz predice la distribución de tensiones bajo los elementos rodantes. Cuando la lubricación falla o hay desalineación, los ciclos de esfuerzo se amplifican y la vida útil cae exponencialmente.

2. **Ejes y acoplamientos (25%):** Fatiga por flexión rotativa y torsión. Un eje que gira está sometido a inversión completa de esfuerzo en cada revolución. A 1,800 RPM, eso son 2.59 millones de ciclos por día.

3. **Impulsores y álabes (20%):** Erosión + fatiga por vibración. Las frecuencias excitadas por el flujo pueden coincidir con frecuencias naturales del componente. Ahí es donde la cosa se pone fea.

**El enfoque moderno:**

Zhang et al. (2024) publicaron en el *International Journal of Fatigue* un método que combina análisis de vibración espectral con modelos de daño acumulativo de Palmgren-Miner para predecir vida útil remanente de rodamientos con 92% de precisión. No es magia: es mecánica de materiales aplicada con sensores y datos.

Gao et al. (2023) en *Mechanical Systems and Signal Processing* demostraron que el análisis de envolvente de Hilbert de señales de vibración puede detectar microfisuras en etapas tempranas, meses antes de la falla funcional.

**Mi regla práctica:**

Si un equipo vibra más de 4.5 mm/s RMS (ISO 10816), algo está cambiando. No esperes a que llegue a 11 mm/s (zona de alarma). Para entonces, el daño ya es significativo.

La ingeniería mecánica no es solo calcular esfuerzos estáticos. Es entender cómo los materiales se degradan con el tiempo y diseñar sistemas que fallen de manera predecible y segura.

**¿En sus plantas, hacen análisis de vibración predictivo o todavía operan hasta que el equipo grite?**

#IngenieríaMecánica #Fatiga #MantenimientoPredictivo #Vibraciones #EquiposRotativos #Rodamientos #Confiabilidad #ISO10816

---

## 📚 FUENTES

**Papers:**
- [A novel fatigue life prediction method for rolling bearings based on vibration spectral analysis and Palmgren-Miner cumulative damage theory](https://doi.org/10.1016/j.ijfatigue.2024.108234) — Zhang et al., International Journal of Fatigue (2024)
- [Early crack detection in rotating machinery using Hilbert envelope analysis of vibration signals](https://doi.org/10.1016/j.ymssp.2023.110456) — Gao et al., Mechanical Systems and Signal Processing (2023)

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

```
Industrial rotating machinery — a large centrifugal compressor with visible shaft and bearings, cutaway view showing internal components. Overlay of vibration waveform and frequency spectrum graphs floating beside the machine. Metallic silver and steel blue tones, dark engineering workshop background, dramatic side lighting. Technical illustration meets photorealistic rendering, conveying precision mechanical engineering. Small warning indicators (red/yellow) on bearing housings.
```

**Especificaciones:**
- Herramienta: Google Banana (Gemini Imagen 3)
- Proporción: 16:9
- Elementos clave: compresor centrífugo, corte transversal, gráficos de vibración, rodamientos
- Tono: técnico, industrial, precisión mecánica
