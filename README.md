# Dense Video Captioning (DVC) — Local Pipeline

This repository contains the code, data artifacts, and notebooks for a final project on dense video captioning over the YouCook2 dataset. The goal is to take an untrimmed cooking video and predict text captions for the events that happen inside it, with timestamps.

Project story
- Problem: standard video captioning gives one description for a whole video, but dense video captioning needs event-level captions and temporal boundaries.
- Approach: use visual features from S3D, transcript grounding from Whisper ASR, and a T5-based text model to generate timestamped captions.
- Model: the main notebook documents the end-to-end pipeline, including video preprocessing, text/audio feature handling, and caption generation.
- Evaluation: the project includes example inference output in `outputs/demo_inference.json`; add your final metric table and qualitative examples in the slide deck.
- Results: the repo currently preserves the pipeline, sample outputs, and checkpoints, but the final presentation should summarize the metrics and best examples.
- Limitations: this is a resource-heavy pipeline and full training/inference is not practical on CPU alone; large video/data downloads are required for the full workflow.

Presentation video
- YouTube link: https://youtu.be/LiwOHimTcq8?si=hH66QVTxH7oDvIJg
- Status: unlisted presentation recording for the final project submission.

What to do first
1. Read this README once to understand the project flow.
2. Run `python run_demo.py` to confirm the workspace is set up.
3. Open `DVC_Final.ipynb` for the primary step-by-step notebook.
4. Review `data/annotations/subset_annotations.json` and `outputs/demo_inference.json` for the lightweight demo artifacts.
5. Add your slide deck and video link before submission.

Repository structure
- `DVC_Final.ipynb` — main notebook with the full pipeline and project notes.
- `DVC_Project_Local.ipynb` — alternate notebook version of the same workflow.
- `run_demo.py` — lightweight CLI check that prints environment, checkpoint, and demo-output info.
- `requirements.txt` — Python dependencies used by the notebooks and helper script.
- `data/` — annotations, ASR transcripts, and extracted features.
- `checkpoints/` — saved model weights (`*.pt`), kept out of git.
- `outputs/` — demo inference JSON and example outputs.

Notebook execution flow
- Required to understand the project:
	- Environment check
	- Install dependencies
	- Project directory setup
	- Annotation loading and subset creation
	- Pipeline overview and sample output review
- Required only for full end-to-end reproduction:
	- Download annotations
	- Download raw videos
	- Extract visual features
	- Train / resume checkpoints
	- Run evaluation and inference
- Optional for quick inspection:
	- `run_demo.py`
	- `outputs/demo_inference.json`
	- `data/annotations/subset_annotations.json`

Runtime expectations and dependencies
- Recommended Python: 3.10 or newer.
- Recommended environment: GPU-enabled machine for any serious training or feature extraction.
- Core dependencies are listed in `requirements.txt` and include `torch`, `transformers`, `openai-whisper`, `h5py`, `opencv-python`, `evaluate`, `nltk`, `huggingface_hub`, `tqdm`, `Pillow`, `numpy`, and `pycocoevalcap`.
- Full dataset processing requires access to the YouCook2 annotations and the raw video files.
- The notebooks were written assuming the project root is `D:\MS\UMD\Courses\Spring-2026\NLP`.

Reproducible setup and demo

Windows / PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_demo.py
```

Linux / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_demo.py
```

To inspect the saved demo output:

```bash
python -c "import json; print(json.load(open('outputs/demo_inference.json', encoding='utf-8')))"
```

To regenerate the small subset used for fast experiments:

```bash
pip install nbconvert
jupyter nbconvert --to notebook --execute DVC_Final.ipynb --ExecutePreprocessor.timeout=600
```

If you want to generate the subset manually, the notebook logic samples 50 train videos and 20 validation videos into `data/annotations/subset_annotations.json` with a fixed seed for reproducibility.

Project artifacts
- Data: present in `data/` with annotations, transcripts, and features.
- Checkpoints: present in `checkpoints/` with saved model weights, but excluded from git.
- Demo output: present in `outputs/demo_inference.json`.
- Notebooks: `DVC_Final.ipynb` and `DVC_Project_Local.ipynb` document the full pipeline.

Submission notes
- Add the final slide deck as a `.pptx` or `.pdf`.
- Add the 10-minute presentation link near the top of this README once it is uploaded.
- Confirm the GitHub repository is public and accessible to the instructor.

If you want, I can also:
- Add a tiny runnable example that only uses `subset_annotations.json`, or
- Generate a slide checklist you can paste into your deck notes.
