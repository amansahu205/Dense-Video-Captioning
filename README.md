# Dense Video Captioning (DVC) — Local Pipeline

This repo contains the code and data used for the DVC final project (YouCook2 dataset). The main project artifacts live under this workspace root.

Quick status
- Data: present (`data/` with annotations, transcripts, features)
- Checkpoints: present (`checkpoints/` with .pt files)
- Notebooks: `DVC_Final.ipynb`, `DVC_Project_Local.ipynb` (contain run steps)
- Outputs: `outputs/` contains `demo_inference.json` and examples

Getting started (minimal)
1. Create and activate a Python 3.10+ environment.
2. Install core dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run the environment check (from notebook or CLI):

```bash
python run_demo.py
```

Files to inspect
- `DVC_Final.ipynb` — full runnable pipeline and instructions (preferred)
- `DVC_Project_Local.ipynb` — alternate notebook with the same sections
- `outputs/demo_inference.json` — example inference output and captions

Notes for submission
- Include this README, slides, 10-minute video (YouTube unlisted link recommended), and a link or zipped copy of the code.
- Verify repository is public or zipped archive is uploaded to Canvas.

Contact
If you want, I can generate a concise slide checklist and a runnable demo script.
