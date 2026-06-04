---
fecha: 2026-05-13
sector: Estructuras Metálicas
tipo: corta
estado: borrador
noticia_fuente: N/A
---

# 🔩 ¿Tornillos apretados a mano? El error silencioso que compromete conexiones estructurales

En obra he visto conexiones atornilladas de grado A325 instaladas con llave de mano y sin verificación de pretensado. El resultado: uniones que no transmiten el momento de diseño y que pueden fallar bajo cargas de servicio.

Después de años revisando conexiones en estructuras industriales y marítimas, estos son los puntos que **siempre** verifico:

**1. Método de apriete según AISC 360-22, Capítulo J3**
Los tornillos A325 y A490 requieren pretensado mínimo del 70% de la resistencia a tensión mínima (F_nt). Para un A325 de ¾": eso son ~170 kN de pretensado. No se logra con una llave de tubo. Usa el método de giro de tuerca (turn-of-nut), llave calibrada (torque control) o indicadores directos de tensión (DTI washers).

**2. Verificación de la condición de superficie (Clase A vs Clase B)**
El coeficiente de deslizamiento φR_n depende directamente del tratamiento superficial. Clase A (superficies limpias con cepillo de alambre) da μ = 0.33. Clase B (granallado o chorro de arena) sube a μ = 0.50. Eso es **51% más capacidad** por la misma cantidad de tornillos. En conexiones tipo fricción, esto define si necesitas 6 u 8 pernos.

**3. Distancias mínimas de borde y espaciamiento**
AISC J3.4 exige distancia mínima de borde de 1.5d (d = diámetro del tornillo) y espaciamiento mínimo de 3d. En campo, he encontrado pernos a 1.2d del borde de la placa — eso reduce la capacidad al cortante del borde (bearing) y puede provocar desgarro (tearout) prematuro.

**4. Secuencia de aprieto: del centro hacia afuera**
Siempre aprieto en espiral desde el centro geométro de la conexión hacia los extremos. Aprieto escalonado en 3 pasadas: 50% → 75% → 100% del pretensado objetivo. Esto evita que los tornillos interiores pierdan carga cuando se aprietan los exteriores.

**5. Inspección post-instalación**
Todo tornillo pretensado debe verificarse. Con llave calibrada, el torque de verificación debe estar dentro del ±10% del valor de diseño. Si más del 15% de los tornillos fallan la verificación, se reemplaza el grupo completo. No se "reaprieta" selectivamente.

---

**Pregunta para el grupo:** En sus proyectos, ¿el método de giro de tuerca (turn-of-nut) sigue siendo el más confiable para verificar pretensado, o han migrado a DTI washers como práctica estándar? ¿Qué tan frecuente es encontrar conexiones sin verificación de pretensado en sus obras?

#EstructurasMetálicas #IngenieríaEstructural #AISC #ConexionesAtornilladas #ConstrucciónMetálicas #DiseñoEstructural

---


---

## 📚 FUENTES

**Referencia técnica:**
- AISC 360-22 Chapter J3 — None

**Papers:**
- [Modern approaches to structural health monitoring](https://doi.org/10.1061/(ASCE)ST.1943-541X.0003512) — Performance-based seismic design of steel moment frames — AISC
- [Sustainable steel structures: Design and performance](https://doi.org/10.1201/b11396-128) — Behaviour of Steel Structures in Seismic Areas (2012)

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

**Generar con Google Banana (Gemini Image):**

**Para generación con IA:**
```
Photorealistic close-up of a structural steel beam-to-column bolted connection on a construction site, showing grade A325 high-strength bolts with washers on a steel gusset plate, natural daylight, industrial atmosphere, safety yellow beam, rust patina on steel surfaces, hard hats and safety vests visible in background, shallow depth of field focusing on the bolt group, 16:9 aspect ratio, technical and professional tone, hyperrealistic detail
```
**Especifications:** Photorealistic style, 16:9 aspect ratio, key elements: steel bolted connection, A325 bolts, gusset plate, construction site environment, technical and industrial tone
