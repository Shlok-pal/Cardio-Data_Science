# 👋 Hi, I'm Shlok Pal

🎓 Computer Engineer | 📊 Aspiring Data Scientist | 🤖 AI & Analytics Enthusiast

---

## 🚀 About This Project

This repository contains a small Data Science project that includes:
- a FastAPI backend (`app/`) exposing model endpoints
- a Streamlit UI (`StreamlitCardio.py`) for quick demos
- a training script (`train_model.py`) and dataset (`data/`)

It's intended as a lightweight demo for cardiovascular risk modeling and serving.

---

## 🧰 Tech & Skills

- Python, Pandas, NumPy
- scikit-learn (or similar) for model training
- FastAPI for API serving
- Streamlit for UI
- Git & GitHub

---

## 🚀 Quick Start

### Clone

- HTTPS:

```bash
https://github.com/Shlok-pal/Cardio-Data_Science.git
```

- SSH:

```bash
git@github.com:Shlok-pal/Cardio-Data_Science.git
```

### Requirements

Python 3.9+ recommended. Create a venv and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app.main:app --reload --port 8000
```

Docs: http://localhost:8000/docs

### Run the Streamlit UI

```bash
streamlit run StreamlitCardio.py
```

### Train/retrain the model

```bash
python train_model.py
```

---

## 📂 Project Structure

- `app/` - FastAPI app (`main.py`, `models.py`, `schema.py`)
- `StreamlitCardio.py` - Streamlit demo UI
- `train_model.py` - Training script
- `data/` - Input dataset (`Cardiovascular_Disease.csv`)
- `models/` - Saved model artifacts
- `requirements.txt` - Python dependencies

---

## 📫 Contact

- Email: contact@shlokpal.com.np
- LinkedIn: https://www.linkedin.com/in/shlok-pal/
- GitHub: https://github.com/Shlok-pal

---

Created by Shlok Pal

Copyright (c) 2026 Shlok Pal. All rights reserved.
