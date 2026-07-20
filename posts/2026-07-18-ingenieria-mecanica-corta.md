---
fecha: 2026-07-18
sector: Ingeniería Mecánica
tipo: corta
estado: borrador
noticia_fuente: https://www.ijraset.com/research-paper/vibration-driven-predictive-maintenance-of-rotating-equipment-using-machine-learning
fuentes_academicas: https://doi.org/10.22214/ijraset.2025.71321
---

# Tu bomba centrífuga te está diciendo que va a fallar. ¿La estás escuchando?

El mantenimiento predictivo basado en vibraciones es una de las técnicas más maduras y de mayor ROI en la industria. Los datos son contundentes: según un estudio de IJASET (2025), un modelo CNN entrenado con wavelet scalograms de señales de vibración logra 99.13% de exactitud en clasificación de fallas en equipos rotativos.

Los números comparativos hablan solos:

| Modelo | Exactitud |
|---|---|
| Raw time signal + CNN | 89.6% |
| FFT + CNN | 93.8% |
| Wavelet + SVM | 95.2% |
| Wavelet + CNN (propuesto) | **99.13%** |

El modelo entrenado con 1.2M de parámetros corre en un Raspberry Pi 4 con 42ms de tiempo de inferencia, consume 58% de CPU en pico, y ocupa solo 6.2 MB en TensorFlow Lite.

**La implicancia práctica:** una bomba de agua de 15 TR en un sistema de aire acondicionado comercial genera firmas de vibración únicas. Cuando el rodamiento de la polea de transmisión empieza a degradarse, la firma de alta frecuencia cambia — antes de que el operador note ruido o temperatura anómala. El análisis de wavelet detecta ese cambio semanas antes del fallo catastrófico.

Un segundo estudio (Springer, 2024) usó Fiber Bragg Grating (FBG) sensors combinados con Random Forest y RBFNN para detección de fallas, logrando identificación temprana de modos de falla en machinery rotativo.

**En la práctica:** he visto plantas industriales que todavía hacen mantenimiento basado en tiempo (cambios de aceite cada 6 meses sin análisis de condición). El ROI de un sistema de monitoreo continuo de vibraciones se paga en el primer fallo de rodamiento evitado. Una emergencia de reparación cuesta entre $15,000 y $150,000 en equipos de aire acondicionado industrial. Una intervención programada: $1,500 a $8,000.

¿Cuál es tu estrategia actual de mantenimiento para equipos rotativos?

#MantenimientoPredictivo #Vibraciones #IngenieríaMecánica #BombasCentrífugas #ConditionMonitoring #HVACPerú

---

## 📚 FUENTES

**Papers:**
- Kulkarni et al., "Vibration-Driven Predictive Maintenance of Rotating Equipment Using Machine Learning" — IJASET Vol.13(5), 2025 https://doi.org/10.22214/ijraset.2025.71321
- Nayak et al., "Enhancing fault detection and predictive maintenance of rotating machinery with FBG sensor and ML" — Int. J. Info. Tech. (Springer, 2024) https://doi.org/10.1007/s41870-024-02256-4

---

## 🖼️ PROMPT PARA IMAGEN (Google Banana / Gemini)

Espectrograma de wavelet a color mostrando señales de vibración de un rodamiento de bomba centrífuga en tres estados: saludable (verde), degradación moderada (amarillo), y falla inminente (rojo), con eje de tiempo en horas y frecuencia en Hz. Estilo técnico con cuadrícula. Formato 16:9.