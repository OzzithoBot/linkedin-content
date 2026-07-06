---
fecha: 2026-06-29
sector: Estructuras Metálicas
tipo: corta
estado: borrador
noticia_fuente: https://ej.aisc.org/index.php/engj/article/view/1343
fuentes_academicas: ["10.62913/engj.v62i2.1343", "10.62913/engj.v63i2.1381"]
---

# El tornillo que no aprietas bien hoy, es la conexión que falla mañana en el sismo

El *Engineering Journal* de AISC (Q2 2025) publicó la investigación de Judy Liu sobre **bearing y tearout en conexiones atornilladas de acero**. El hallazgo central: la capacidad de una conexión no la define solo el tornillo — la define el material que lo rodea.

Dos modos de falla que en obra pasan desapercibidos hasta que es tarde:

**Bearing (aplastamiento del orificio):** El tornillo aplasta el material de la placa alrededor del orificio. La capacidad depende de *d × t × Fu* (diámetro × espesor × resistencia última). Si la placa es delgada o el acero es de bajo Fu (ej. A36 vs A992), el bearing gobierna antes que el corte del tornillo.

**Tearout (desgarro del borde):** El material se desgarra desde el orificio hacia el borde libre. Capacidad = *1.2 × lc × t × Fu* (lc = distancia del centro del orificio al borde). **Aquí está el dato crítico:** AISC 360-22 J3.4 exige distancia mínima de borde **1.5d**. En campo he medido 1.2d "porque la placa era chica". Eso reduce la capacidad de tearout en **~30%**.

**El estudio de Liu (2025) lo cuantificó:** En conexiones con distancias de borde sub-estándar, el tearout ocurre a cargas 25-40% menores que el diseño nominal. Y lo peor: **no hay aviso previo**. El bearing da deformación plástica visible; el tearout es frágil, repentino.

En proyectos industriales y mineros que he supervisado en Perú, la secuencia de apriete y verificación de distancias de borde/espaciamiento (3d mínimo entre centros) es **innegociable**. Un perno A325 de ¾" mal instalado no falla solo — arrastra la conexión, la viga, y eventualmente el pórtico.

**Regla práctica que uso:** Si el detalle de conexión no cabe en la placa con 1.5d de borde y 3d de espaciamiento, **la placa se redimensiona**. No se negocia geometría por "ajustar".

¿En tus proyectos, quién verifica distancias de borde y espaciamiento en campo antes de apriete final? ¿El inspector de soldadura también revisa tornillos?

#EstructurasMetálicas #AISC360 #ConexionesAtornilladas #Bearing #Tearout #IngenieríaEstructural #Acero #ControlCalidad #Perú

---

## 📚 FUENTES

**Noticia/Paper principal:**
- [Investigation of Bearing and Tearout of Steel Bolted Connections](https://ej.aisc.org/index.php/engj/article/view/1343) — Judy Liu, PhD, *Engineering Journal*, Vol. 62 No. 2 (2025), DOI: 10.62913/engj.v62i2.1343

**Papers académicos:**
- [The Novel SnapLocX Column Splice](https://ej.aisc.org/index.php/engj/article/view/1381) — Judy Liu, *Engineering Journal*, Vol. 63 No. 2 (2026), DOI: 10.62913/engj.v63i2.1381
- [Steel Structures Research Update: Slotted-Hidden-Gap Connections and Intentional Eccentricity for Steel Brace](https://ej.aisc.org/index.php/engj/article/view/1207) — Judy Liu, *Engineering Journal*, Vol. 60 No. 2 (2023), DOI: 10.62913/engj.v60i2.1207

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

**Generar con Google Banana (Gemini Imagen 3):**
```
Technical engineering illustration showing steel bolted connection failure modes side by side: left panel shows bearing deformation (bolt crushing hole material, plastic deformation around hole), right panel shows tearout failure (material tearing from hole to free edge in triangular wedge). Center shows proper geometry with 1.5d edge distance and 3d spacing dimensions annotated. Clean white background, AISC blue/gray color scheme, isometric view with cross-section cutaway, dimension lines with values, professional structural engineering drawing style, 16:9 aspect ratio, high detail.
```