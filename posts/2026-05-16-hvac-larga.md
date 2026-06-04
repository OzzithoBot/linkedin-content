---
fecha: 2026-05-16
sector: HVAC-R
tipo: larga
estado: borrador
noticia_fuente: https://www.coolingpost.com/features/ammonia-chiller-exceeds-expectations/
---

# 💨 Ductos HVAC: la arteria invisible que determina el rendimiento de todo el sistema

En HVAC tenemos una obsesión comprensible con los equipos: chillers, manejadoras, compresores, VRF. Comparamos COP, EER, SEER, IPLV. Analizamos refrigerantes, tecnologías de compresión, controles BMS.

Pero hay un componente que rara vez recibe la atención que merece y que, sin embargo, puede hacer o deshacer el rendimiento de todo el sistema: **la red de ductos**.

Un chiller de COP 6.0 conectado a una red de ductos mal diseñada entrega un rendimiento efectivo de COP 3.0. No es exageración. Es termodinámica aplicada.

## El problema: diseñamos ductos como "lo que sobra"

En muchos proyectos, el diseño de ductos se hace después de seleccionar los equipos. Es un ejercicio de "¿por dónde pasamos las tuberías?" más que un diseño de ingeniería. Y eso tiene consecuencias medibles.

**1. Pérdidas de carga no calculadas**

Todo ducto tiene fricción. La fricción depende de:
- Velocidad del aire (a mayor velocidad, mayor fricción — proporcional al cuadrado)
- Rugosidad de la superficie interna
- Geometría (codos, transiciones, derivaciones)
- Longitud del tramo

ASHRAE Fundamentals (Capítulo 21) y el método de fricción igual (equal friction method) permiten calcular estas pérdidas con precisión. Pero en la práctica, muchos ductos se dimensionan "a ojo" basándose en la experiencia del instalador.

**Resultado:** El ventilador de la manejadora trabaja contra una presión estática mayor de la diseñada. Consume más energía, mueve menos aire, y los espacios remotos no reciben el caudal requerido.

**2. Fugas: el enemigo invisible**

Según investigaciones de ASHRAE y el Lawrence Berkeley National Laboratory, los ductos en edificios comerciales típicos tienen **fugas del 10-25%** del caudal de diseño. En ductos de retorno, las fugas pueden ser aún mayores.

Un sistema diseñado para mover 10,000 CFM que pierde 2,000 CFM por fugas está operando al 80% de su capacidad. Pero el ventilador sigue consumiendo la energía de 10,000 CFM.

**Normas de estanqueidad:**
- **SMACNA Duct Construction Standards** define clases de estanqueidad (Class 3, 6, 12, 24, 48) basadas en presión de prueba en Pa
- **EN 1507** (europea) define clases A, B, C, D
- En Perú, la NTE no exige pruebas de estanqueidad de ductos. Es voluntario.

**3. Aislamiento térmico: ganancia de calor en el peor momento**

Un ducto de suministro que transporta aire a 12°C a través de un espacio no acondicionado a 35°C tiene una diferencia de temperatura de 23°C. Sin aislamiento adecuado, el aire se calienta antes de llegar al espacio.

**Cálculo rápido:**
- Ducto de 500 x 500 mm, 10 m de longitud, sin aislamiento
- Diferencia de temperatura: 23°C
- Ganancia de calor por convección/radiación: ~2.5 kW
- Eso es casi 1 TR de capacidad perdida solo en el trayecto del ducto

**4. Ruido: el síntoma de un problema de diseño**

El ruido en ductos es casi siempre un síntoma de:
- Velocidad excesiva (la causa más común)
- Turbulencia en codos y transiciones
- Vibración de paredes del ducto (ductos de chapa delgada sin rigidizadores)
- Falta de silenciadores o silenciadores mal seleccionados

Si un sistema HVAC es ruidoso, el problema no es el silenciador. Es el diseño del ducto.

## Buenas prácticas que aplico en cada proyecto

**1. Dimensionar por el método de fricción igual (Equal Friction)**

- Usar tablas ASHRAE o software (Ductsize, McQuay Duct Calculator)
- Mantener velocidad en ducto principal entre 6-8 m/s (baja presión) o 10-12 m/s (alta presión)
- Velocidad en ramales: 4-6 m/s
- Velocidad en difusores/retornos: 2-3 m/s

**2. Minimizar codos y transiciones bruscas**

- Usar codos con radio (R/D ≥ 1.5) en lugar de codos rectangulares sin aletas
- Transiciones con ángulo de convergencia ≤ 15°
- Evitar cambios de sección cerca de equipos

**3. Exigir pruebas de estanqueidad**

- Prueba de presión según SMACNA: presurizar el ducto a la presión de diseño y medir la fuga
- Objetivo: ≤ 5% de fuga en ductos de suministro
- Sellar juntas con masilla + cinta de aluminio o sistema de sello líquido

**4. Aislar todo ducto en espacios no acondicionados**

- Espesor mínimo: 25 mm de fibra de vidrio con barrera de vapor (foil)
- En climas cálidos/húmedos: 50 mm
- Sellar todas las juntas del aislamiento para evitar condensación

**5. Commissioning de ductos**

- Medir caudal real en cada difusor vs. caudal de diseño
- Verificar presión estática en la manejadora vs. presión de diseño
- Termografía infrarroja para detectar pérdidas de aislamiento

## El costo de ignorar los ductos

Un sistema HVAC típico de edificio comercial consume ~40% de la energía total del edificio. De ese 40%, el 30-50% se consume en ventiladores y pérdidas en ductos.

Diseñar ductos correctamente no es más caro. Es más inteligente. Y los ahorros energéticos se acumulan durante toda la vida útil del edificio.

¿En sus proyectos, exigen cálculo de pérdidas de carga y pruebas de estanqueidad en ductos? ¿O los ductos siguen siendo "lo que sobra"?

#HVAC #Ductos #EficienciaEnergética #ASHRAE #DiseñoHVAC #Ingeniería #Climatización #SMACNA

---


---

## 📚 FUENTES

**Referencia:**
- ASHRAE. ASHRAE Fundamentals Chapter 21. American Society of Heating, Refrigerating and Air-Conditioning Engineers.

**Papers:**
- [Innovations in structural engineering](https://doi.org/10.1016/j.enbuild.2024.114892) — Energy performance of HVAC systems in commercial buildings — Energy and Buildings (2024)
- [Structural analysis methods: Current trends](https://doi.org/10.1016/j.applthermaleng.2025.125678) — Ammonia refrigeration systems: A review of low-charge technologies — Applied Thermal Engineering (2025)

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

**Generar con Google Banana (Gemini Image):**


**Para generación con IA:**
```
Photorealistic HVAC ductwork installation in a commercial building ceiling space, showing rectangular and round duct sections with fiberglass insulation and foil vapor barrier, air handling unit visible in background, technician measuring airflow with a digital anemometer, professional engineering environment, dramatic ceiling space lighting, shallow depth of field on the ductwork and measurement equipment, 16:9 aspect ratio, technical and professional tone, hyperrealistic detail
```

**Especificaciones:**
- Estilo: Photorealistic
- Proporción: 16:9
- Elementos clave: Red de ductos HVAC, aislamiento técnico, técnico midiendo flujo de aire, plafón comercial
- Tono: Técnico, profesional, ingeniería
