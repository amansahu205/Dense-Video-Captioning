"""Minimal demo runner for the DVC project.

Usage: python run_demo.py
This script performs lightweight checks and prints sample info from the workspace.
"""
import sys
import os
import json

ROOT = os.path.dirname(__file__)

def check_python():
    print(f"Python: {sys.version.split()[0]}")

def list_checkpoints():
    ckpt_dir = os.path.join(ROOT, "checkpoints")
    if not os.path.isdir(ckpt_dir):
        print("No checkpoints/ directory found.")
        return
    files = [f for f in os.listdir(ckpt_dir) if f.endswith('.pt')]
    print(f"Checkpoints ({len(files)}):", files[:10])

def show_demo_inference():
    path = os.path.join(ROOT, "outputs", "demo_inference.json")
    if not os.path.exists(path):
        print("No demo_inference.json found in outputs/")
        return
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("Demo video url:", data.get('video_url'))
    captions = data.get('captions', [])
    print(f"Demo captions: {len(captions)} segments (showing first 3)")
    for c in captions[:3]:
        print(f"  [{c.get('start')}–{c.get('end')}] {c.get('caption')}")

def main():
    check_python()
    list_checkpoints()
    show_demo_inference()

if __name__ == '__main__':
    main()
