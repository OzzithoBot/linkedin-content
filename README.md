# 💼 02_LINKEDIN_CONTENT — ZV PERU SAC

**Objetivo:** Gestionar la creación y publicación de contenido técnico-ingenieril en el perfil personal de LinkedIn de Jherson, enfocado en HVAC, estructuras metálicas e ingeniería naval.

---

## 🎯 Objetivo

Generar contenido de valor para posicionar el perfil profesional en LinkedIn con:
- Publicaciones técnicas sobre HVAC, estructuras metálicas, ingeniería naval
- Calendario editorial organizado
- Noticias del sector curadas
- Enfoque en normas, estándares y software (NO beneficios generales)

---

## 📁 Estructura

```
02_LINKEDIN_CONTENT/
├── posts/                    ← Posts generados listos para publicar
│   ├── 2026-05-10-hvac-corta.md
│   ├── 2026-05-10-estructuras-larga.md
│   ├── 2026-05-10-naval-corta.md
│   ├── 2026-05-12-hvac-corta.md
│   ├── 2026-05-12-estructuras-larga.md
│   ├── 2026-05-13-naval-corta.md
│   └── 2026-05-13-estructuras-corta.md
├── noticias/                 ← Noticias curadas del sector
└── calendario/               ← Calendario editorial
```

---

## 📝 Reglas de Contenido

1. **Perfil personal** — No publicitar empresa
2. **Contenido técnico-ingenieril** — No genérico ni comercial
3. **Enfoque en normas/estándares/software** — AISC, ASHRAE, AWS, NTE, IMO
4. **Prompt de imagen obligatorio** — Cada post incluye prompt para generación de imagen
5. **Datos concretos** — Mínimo 1 dato/estadística por publicación
6. **Pregunta de cierre** — Siempre cerrar con pregunta abierta para engagement

---

## 📋 Historial de Actualizaciones

| Fecha | Actualización |
|-------|---------------|
| 2026-05-13 | Generados 7 posts faltantes de semana 2 (13-16 mayo). Semana 2 completada al 100%. Noticias guardadas en noticias/. Calendario actualizado. |
| 2026-05-13 | Migración de PUBLICA/posts/ a 02_LINKEDIN_CONTENT/posts/. Cron jobs actualizados con nueva ruta y skill linkedin-content-pipeline. Generados posts faltantes del 12 y 13 de mayo. |
| 2026-05-11 | Carpeta migrada a AGENT. README creado. |
| 2026-05-10 | Primeros posts generados (HVAC, Estructuras, Naval). Calendario editorial creado. |

---

## 🔄 Automatización

- **Cron Matutino (7:00 AM Lun-Dom):** Genera post corto del día
- **Cron Vespertino (13:00 PM Lun-Dom):** Genera post largo del día
- **Skill:** linkedin-content-pipeline
- **Ruta de guardado:** `02_LINKEDIN_CONTENT/posts/YYYY-MM-DD-[sector]-[tipo].md`

---

## 🖼️ Generador de Imágenes

Cada post incluye un prompt de imagen en la sección `## 🖼️ PROMPT PARA IMAGEN`. Las imágenes se generan automáticamente con **Stable Diffusion 1.5** usando la GPU local (RTX 3050 6GB).

### Uso

```bash
# Listar posts y estado de imágenes
python generate_images.py list

# Generar imagen para un post específico
python generate_images.py generate 2026-05-13-hvac-larga.md

# Generar todas las imágenes faltantes
python generate_images.py generate-all

# Regenerar todas (incluyendo existentes)
python generate_images.py generate-all --force
```

### Estructura

```
02_LINKEDIN_CONTENT/
├── generate_images.py       ← Script generador (SD 1.5 local)
├── generate_images.bat      ← Wrapper para Windows
├── requirements.txt         ← Dependencias Python
├── .venv/                   ← Entorno virtual (PyTorch + diffusers)
├── images/                  ← Imágenes generadas (60 PNG)
│   ├── 2026-05-10-hvac-corta.png
│   ├── 2026-05-10-estructuras-larga.png
│   └── ...
├── posts/                   ← Posts markdown
└── data.json                ← Metadatos (incluye referencia a imagen)
```

### Especificaciones

- **Modelo:** Stable Diffusion 1.5 (local, desde cache de HuggingFace)
- **Resolución:** 768×512 (3:2)
- **Pasos de inferencia:** 30
- **Guidance scale:** 7.5
- **Tiempo por imagen:** ~15-45 segundos (RTX 3050 6GB)
- **VRAM usada:** ~4 GB
- **Estilo:** Photorealistic, técnico, profesional
