#!/usr/bin/env python3
"""
Generador de imágenes para posts de LinkedIn
Usa Stable Diffusion 1.5 local con GPU (RTX 3050 6GB)

Uso:
  python generate_images.py list
  python generate_images.py generate POST.md [--force]
  python generate_images.py generate-all [--force]
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime

# ── Configuración ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
POSTS_DIR = BASE_DIR / "posts"
DATA_FILE = BASE_DIR / "data.json"
IMAGES_DIR = BASE_DIR / "images"

# Modelo local — ruta al cache de HuggingFace
SD15_CACHE = Path("C:/Users/jhers/.cache/huggingface/hub/models--runwayml--stable-diffusion-v1-5/snapshots/451f4fe16113bff5a5d2269ed5ad43b0592e9a14")

# Parámetros de generación
IMAGE_WIDTH = 768
IMAGE_HEIGHT = 512
NUM_INFERENCE_STEPS = 30
GUIDANCE_SCALE = 7.5

# ── Utilidades ─────────────────────────────────────────────────────────────────

def ensure_dirs():
    IMAGES_DIR.mkdir(exist_ok=True)


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"posts": []}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def extract_image_prompt(post_path: Path) -> str | None:
    """Extrae el prompt de imagen de un archivo de post .md"""
    content = post_path.read_text(encoding="utf-8")

    # Buscar la sección ## 🖼️ PROMPT PARA IMAGEN
    pattern = r"##\s*🖼️\s*PROMPT PARA IMAGEN.*?\`\`\`\s*(.*?)\s*\`\`\`"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fallback: buscar cualquier bloque de código después de "PROMPT"
    pattern2 = r"PROMPT.*?\`\`\`\s*(.*?)\s*\`\`\`"
    match2 = re.search(pattern2, content, re.DOTALL)
    if match2:
        return match2.group(1).strip()

    return None


def build_default_prompt(post: dict) -> str:
    """Genera un prompt por defecto basado en el título y sector del post"""
    sector = post.get("sector", "ingeniería")
    titulo = post.get("titulo", "")

    sector_styles = {
        "HVAC-R": "HVAC engineering, refrigeration systems, industrial cooling equipment, copper piping, evaporators, technical blueprints, clean professional environment",
        "Estructuras Metálicas": "steel structures, metal construction, industrial buildings, steel beams and connections, welding details, engineering precision",
        "Ingeniería Naval": "naval architecture, ship design, marine engineering, ocean vessels, shipyard, hull structures, maritime technology",
        "Ingeniería Mecánica": "mechanical engineering, precision machinery, industrial equipment, CAD designs, manufacturing processes",
        "Elementos Finitos": "finite element analysis, FEA mesh, stress visualization, computational simulation, color-mapped structural analysis, engineering software",
        "IA": "artificial intelligence, neural networks, data visualization, futuristic technology, digital brain, machine learning concepts",
        "Simulación Asistida por Computadora": "computer simulation, CFD flow visualization, engineering software, digital twin, computational analysis",
        "Gestión de Proyectos": "project management, Gantt charts, team collaboration, construction site planning, engineering project timeline",
    }

    style = sector_styles.get(sector, "engineering, technical, professional")

    return (
        f"Professional engineering illustration for LinkedIn post about {titulo}. "
        f"{style}. "
        f"Clean modern composition, subtle technical elements, "
        f"professional color palette with blue and teal accents, "
        f"high quality, photorealistic style"
    )


# ── Generador local con SD 1.5 ─────────────────────────────────────────────────

def init_pipeline():
    """Inicializa el pipeline de SD 1.5 desde cache local"""
    import torch
    from diffusers import StableDiffusionPipeline

    print(f"🔧 Cargando SD 1.5 desde cache local...")
    print(f"   GPU: {torch.cuda.get_device_name(0)}")

    pipe = StableDiffusionPipeline.from_pretrained(
        str(SD15_CACHE),
        torch_dtype=torch.float16,
        use_safetensors=True,
        safety_checker=None,
        requires_safety_checker=False,
    )

    pipe = pipe.to("cuda")
    pipe.enable_attention_slicing()  # Reduce uso de VRAM para 6GB

    print("✅ Pipeline listo")
    return pipe


def generate_image(pipe, prompt: str, output_path: Path) -> bool:
    """Genera una imagen con SD 1.5 y la guarda"""
    import torch

    print(f"🎨 Generando imagen...")
    print(f"   Prompt: {prompt[:100]}...")

    generator = torch.Generator("cuda").manual_seed(42)

    result = pipe(
        prompt=prompt,
        width=IMAGE_WIDTH,
        height=IMAGE_HEIGHT,
        num_inference_steps=NUM_INFERENCE_STEPS,
        guidance_scale=GUIDANCE_SCALE,
        generator=generator,
    )

    image = result.images[0]
    image.save(output_path, "PNG")
    size_kb = output_path.stat().st_size / 1024
    print(f"✅ Imagen guardada: {output_path} ({size_kb:.0f} KB)")
    return True


# ── Funciones principales ─────────────────────────────────────────────────────

def generate_for_post(post_file: str, force: bool = False):
    """Genera imagen para un post específico"""
    ensure_dirs()
    data = load_data()

    # Buscar el post en data.json
    post_entry = None
    for p in data.get("posts", []):
        if p["filename"] == post_file:
            post_entry = p
            break

    if not post_entry:
        print(f"❌ Post '{post_file}' no encontrado en data.json")
        return False

    post_path = POSTS_DIR / post_file
    if not post_path.exists():
        print(f"❌ Archivo no encontrado: {post_path}")
        return False

    # Determinar nombre de imagen
    stem = Path(post_file).stem
    image_filename = f"{stem}.png"
    image_path = IMAGES_DIR / image_filename

    # Verificar si ya existe
    if image_path.exists() and not force:
        print(f"ℹ️  Imagen ya existe: {image_path} (usar --force para regenerar)")
        return True

    # Extraer prompt
    prompt = extract_image_prompt(post_path)
    if not prompt:
        print(f"⚠️  No se encontró prompt en {post_file}, generando uno automático...")
        prompt = build_default_prompt(post_entry)

    # Inicializar pipeline y generar
    try:
        pipe = init_pipeline()
        success = generate_image(pipe, prompt, image_path)

        if success:
            # Actualizar data.json
            post_entry["imagen"] = f"images/{image_filename}"
            post_entry["imagen_generada"] = datetime.now().isoformat()
            post_entry["imagen_modelo"] = "sd15-local"
            save_data(data)
            print(f"📝 data.json actualizado")

        # Liberar memoria GPU
        import torch
        torch.cuda.empty_cache()

        return success

    except Exception as e:
        print(f"❌ Error generando imagen: {e}")
        import traceback
        traceback.print_exc()
        return False


def generate_all(missing_only: bool = True, force: bool = False):
    """Genera imágenes para todos los posts"""
    ensure_dirs()
    data = load_data()

    posts = data.get("posts", [])
    total = len(posts)
    generated = 0
    skipped = 0
    errors = 0

    print(f"📋 {total} posts encontrados en data.json")

    # Filtrar
    to_process = []
    for p in posts:
        filename = p["filename"]
        stem = Path(filename).stem
        image_path = IMAGES_DIR / f"{stem}.png"

        if missing_only and image_path.exists() and not force:
            skipped += 1
            continue
        to_process.append(p)

    if not to_process:
        print("✅ Todas las imágenes ya están generadas")
        return

    print(f"🎯 {len(to_process)} imágenes por generar ({skipped} omitidas)")

    # Inicializar pipeline una sola vez
    try:
        pipe = init_pipeline()
    except Exception as e:
        print(f"❌ Error inicializando pipeline: {e}")
        return

    for i, post_entry in enumerate(to_process, 1):
        filename = post_entry["filename"]
        stem = Path(filename).stem
        image_path = IMAGES_DIR / f"{stem}.png"

        print(f"\n[{i}/{len(to_process)}] {filename}")

        post_path = POSTS_DIR / filename
        if not post_path.exists():
            print(f"   ⚠️  Archivo no encontrado, saltando")
            errors += 1
            continue

        prompt = extract_image_prompt(post_path)
        if not prompt:
            prompt = build_default_prompt(post_entry)

        try:
            success = generate_image(pipe, prompt, image_path)
            if success:
                post_entry["imagen"] = f"images/{stem}.png"
                post_entry["imagen_generada"] = datetime.now().isoformat()
                post_entry["imagen_modelo"] = "sd15-local"
                generated += 1
            else:
                errors += 1
        except Exception as e:
            print(f"   ❌ Error: {e}")
            errors += 1

    # Guardar data.json actualizado
    save_data(data)

    # Liberar memoria GPU
    import torch
    torch.cuda.empty_cache()

    print(f"\n{'='*50}")
    print(f"✅ Generadas: {generated}")
    print(f"⏭️  Omitidas: {skipped}")
    print(f"❌ Errores: {errors}")
    print(f"📁 Imágenes en: {IMAGES_DIR}")


def list_posts_with_prompts():
    """Lista todos los posts y muestra si tienen prompt de imagen"""
    data = load_data()
    posts = data.get("posts", [])

    print(f"\n{'='*70}")
    print(f"{'ARCHIVO':<45} {'PROMPT':>6} {'IMAGEN':>8}")
    print(f"{'='*70}")

    for p in posts:
        filename = p["filename"]
        post_path = POSTS_DIR / filename

        has_prompt = "✅" if post_path.exists() and extract_image_prompt(post_path) else "❌"

        stem = Path(filename).stem
        has_image = "✅" if (IMAGES_DIR / f"{stem}.png").exists() else "❌"

        print(f"{filename:<45} {has_prompt:>6} {has_image:>8}")

    print(f"{'='*70}")
    print(f"Total: {len(posts)} posts")


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generador de imágenes para posts de LinkedIn (SD 1.5 local)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Comando")

    # Comando: generate
    gen_parser = subparsers.add_parser("generate", help="Generar imagen para un post")
    gen_parser.add_argument("post", help="Nombre del archivo del post")
    gen_parser.add_argument("--force", action="store_true", help="Regenerar aunque ya exista")

    # Comando: generate-all
    all_parser = subparsers.add_parser("generate-all", help="Generar imágenes para todos los posts")
    all_parser.add_argument("--force", action="store_true", help="Regenerar todas")
    all_parser.add_argument("--all", action="store_true", help="Incluir posts que ya tienen imagen")

    # Comando: list
    subparsers.add_parser("list", help="Listar posts y estado de imágenes")

    args = parser.parse_args()

    if args.command == "generate":
        success = generate_for_post(args.post, force=args.force)
        sys.exit(0 if success else 1)

    elif args.command == "generate-all":
        generate_all(missing_only=not args.all, force=args.force)

    elif args.command == "list":
        list_posts_with_prompts()

    else:
        parser.print_help()
        print("\nEjemplos:")
        print('  python generate_images.py list')
        print('  python generate_images.py generate 2026-05-13-hvac-larga.md')
        print('  python generate_images.py generate-all')
        print('  python generate_images.py generate-all --force')


if __name__ == "__main__":
    main()
