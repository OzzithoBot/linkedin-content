"""Descargar modelo SD 1.5 para ComfyUI"""
import subprocess
import os
import sys

COMFY_CLI = r"C:\Users\jhers\Desktop\AGENT\02_LINKEDIN_CONTENT\.venv\Scripts\comfy.exe"
COMFY_WORKSPACE = r"C:\Users\jhers\Documents\comfy\ComfyUI"
MODEL_URL = "https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"
MODEL_PATH = "models/checkpoints"

env = os.environ.copy()
env["COMFYUI_WORKSPACE"] = COMFY_WORKSPACE

cmd = [
    COMFY_CLI,
    "--workspace", COMFY_WORKSPACE,
    "--skip-prompt",
    "model", "download",
    "--url", MODEL_URL,
    "--relative-path", MODEL_PATH,
]

print(f"Ejecutando: {' '.join(cmd)}")
result = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=600)

print(f"Exit code: {result.returncode}")
if result.stdout:
    print(f"STDOUT:\n{result.stdout[-500:]}")
if result.stderr:
    print(f"STDERR:\n{result.stderr[-500:]}")
