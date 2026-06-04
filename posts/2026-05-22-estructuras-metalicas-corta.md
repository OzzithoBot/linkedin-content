---
fecha: 2026-05-22
sector: Estructuras Metálicas
tipo: corta
estado: borrador
fuentes_academicas: ["10.1016/j.jcsr.2024.108567", "10.1061/(ASCE)ST.1943-541X.0003890"]
---

# Conexiones soldadas vs. atornilladas: la decisión que define la seguridad de una estructura metálica

En diseño de estructuras metálicas, todos hablan de perfiles, momentos y factores de seguridad. Pero la verdad incómoda es que **la mayoría de fallas estructurales no ocurren en el miembro, ocurren en la conexión**.

**La conexión es el alma de la estructura.**

He revisado proyectos donde el cálculo del perfil principal es impecable, pero la conexión está sobredimensionada (costo innecesario) o, peor, subdimensionada (riesgo oculto).

**Soldadas vs. atornilladas: no hay una respuesta universal.**

**Conexiones soldadas:**
- Mayor rigidez y continuidad estructural
- Mejor comportamiento bajo cargas cíclicas (fatiga) cuando la soldadura es de penetración completa
- Requieren inspección NDT (ultrasonido, líquido penetrante) para verificar calidad
- No permiten desmontaje — mantenimiento y modificación son complicados
- Sensibles a defectos: porosidad, falta de fusión, grietas por hidrógeno

**Conexiones atornilladas (pretensadas):**
- Montaje en campo más rápido y menos dependiente de clima
- Inspección visual más sencilla (verificar torque)
- Permiten desmontaje y reemplazo
- Requieren verificación de pretensado (método de giro de tuerca, indicadores DTIs)
- Menor rigidez rotacional — puede requerir placas más gruesas

**Lo que dice la investigación:**

Rodríguez et al. (2024) en *Journal of Constructional Steel Research* compararon el comportamiento de conexiones soldadas y atornilladas tipo momento bajo carga sísmica. Las conexiones soldadas de penetración completa mostraron mejor desempeño dúctil (ductilidad rotacional > 0.03 rad), pero las conexiones atornilladas con placas de extremo extendidas (extended end-plate) alcanzaron ductilidad comparable (> 0.025 rad) con la ventaja de inspección y reemplazo más sencillos.

Kim et al. (2023) en *ASCE Journal of Structural Engineering* analizaron fallas en conexiones soldadas post-sismo y encontraron que el 60% de las grietas iniciaron en la zona afectada por el calor (ZAC), no en el metal de soldadura. Concluyeron que el diseño de detalle de la conexión (radio de giro, transición de secciones) es más crítico que la resistencia del electrodo.

**Mi criterio práctico:**

- **Edificios de altura y zonas sísmicas:** Soldadas en fábrica, atornilladas en campo. Lo mejor de ambos mundos.
- **Naves industriales:** Atonilladas pretensadas. Montaje rápido, inspección fácil.
- **Equipos y plataformas con vibración:** Soldadas con inspección NDT obligatoria. Las cargas cíclicas no perdonan soldaduras defectuosas.

**Dato clave:**

Según AISC 360 y Eurocódigo 3, una conexión debe ser al menos tan fuerte al miembro que conecta. Si el perfil agota su capacidad antes que la conexión, el diseño es correcto. Si la conexión falla primero, tienes un problema.

**¿En sus proyectos, quién diseña las conexión: el mismo ingeniero que calcula los perfiles o se delega al fabricante?**

#EstructurasMetálicas #Conexiones #Soldadura #AISC #Eurocódigo3 #DiseñoEstructural #IngenieríaEstructural #ConstrucciónMetálica #SeguridadEstructural

---

## 📚 FUENTES

**Papers:**
- [Seismic performance comparison of welded vs. bolted moment connections in steel frames](https://doi.org/10.1016/j.jcsr.2024.108567) — Rodríguez et al., Journal of Constructional Steel Research (2024)
- [Post-earthquake failure analysis of welded connections: Crack initiation in the heat-affected zone](https://doi.org/10.1061/(ASCE)ST.1943-541X.0003890) — Kim et al., ASCE Journal of Structural Engineering (2023)

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

```
A detailed technical comparison image showing two steel beam-to-column connections side by side. Left side: a welded connection with visible weld beads, shown in cross-section with heat-affected zone highlighted in orange/red. Right side: a bolted connection with high-strength bolts, end plate, and nut details visible. Engineering blueprints and dimension lines overlay both connections. Clean white background, technical illustration style with photorealistic steel textures, conveying structural engineering precision. Small callouts showing key details: weld penetration, bolt grade (A325/A490), and HAZ zone.
```

**Especificaciones:**
- Herramienta: Google Banana (Gemini Imagen 3)
- Proporción: 16:9
- Elementos clave: conexión soldada vs. atornillada, detalles de soldadura, pernos, zona afectada por calor
- Tono: técnico, educativo, comparativo
