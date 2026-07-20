---
fecha: 2026-07-20
sector: Gestión de Proyectos
tipo: corta
estado: borrador
noticia_fuente: https://civinnovate.com/2026/06/18/earned-value-management-construction-guide-2026
fuentes_academicas: https://doi.org/10.1038/s41598-025-05834-z
---

# El error más común en EVM: confundir "presupuesto gastado" con "valor generado"

En mis años gestionando proyectos HVAC, el error más frecuente que veo es日报 de cost reporting básico disfrazado de EVM. El jefe de proyecto muestra: "Llevamos gastado S/ 450,000 de S/ 600,000" y concluye que vamos al 75%. Eso no es EVM. Es solo cost tracking.

Earned Value real necesita tres variables: Planned Value (PV), Earned Value (EV), y Actual Cost (AC). El CPI = EV/AC te dice si estás cost-efficient. El SPI = EV/PV te dice si estás en schedule.

El estudio de FCT Abuja (2026) encontró que la gestión de costos con EVM scoring 4.09–4.18/5 — pero solo cuando se implementa con la estructura correcta de Work Breakdown Structure y control accounts.

Un paper de Scientific Reports (2025) encontró que EVM clásico tiene limitaciones en proyectos de construcción con alta variabilidad de alcance, donde Earned Schedule (ES) outperforms el EVM tradicional hasta en un 23% en forecasting.

**Los errores que成本的 proyectos que he visto (incluyendo los míos):**

1. **No cargar el schedule con presupuesto.** Sin time-phased budget en el baseline, no puedes calcular PV por período, y por tanto no puedes calcular SPI.

2. **Ajustar % completo retroactivamente para "mejorar" el CPI.** Esto es mortal. Si el supervisor cambia el % completo para que CPI = 1.0 se ve bien, el sistema de EVM ya no significa nada.

3. **Reportar solo a nivel proyecto.** Un proyecto puede tener CPI = 0.95 promediando un package de estructura en 0.70 y otro en 1.20. El problema está en el package de 0.70, no en el promedio.

**La regla simple:** si no tienes budget baseline time-phased cargado en MS Project o similar, no tienes EVM — tienes cost tracking básico.

¿Cuál es tu CPI actual y qué package está tirando el promedio?

#GestiónDeProyectos #EVM #ControlDeCostos #ProjectManagement #HVAC #ZVPerú #IngenieríaDeProyectos

---

## 📚 FUENTES

**Noticia:**
- Civinnovate, "Earned Value Management (EVM) in Construction Projects: Complete 2026 Guide" (Jun 2026) https://civinnovate.com/2026/06/18/earned-value-management-construction-guide-2026

**Papers:**
- Comparative analysis of earned value management techniques in construction projects — Scientific Reports (Nature, 2025) https://doi.org/10.1038/s41598-025-05834-z
- Johnson et al., "Evaluating the Effectiveness of Earned Value Management in Construction Project Control in FCT Abuja" — IJRISS (2026) https://rsisinternational.org/journals/ijriss/uploads/vol10-iss5-pg12039-12049-202606/_pdf.pdf

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

Panel de control de proyecto mostrando tres gráficos: curva S con PV vs EV vs AC, indicador circular de CPI (0.85 en rojo) y SPI (1.05 en verde), y tabla de work packages con sus respectivos índices de desempeño codificados por color. Estilo executive dashboard, formato 16:9.