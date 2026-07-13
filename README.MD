# Fashion AI: Text-to-Image Generation with SDXL, ControlNet & LoRA

## Overview

Fashion AI is an end-to-end AI system for generating high-quality fashion images from text prompts using **Stable Diffusion XL (SDXL)**, **ControlNet**, and **LoRA fine-tuning**. The project also includes a vector database for fashion knowledge retrieval, prompt engineering, image evaluation, and a web interface.

---

## Features

* SDXL-based text-to-image generation
* ControlNet-guided image generation
* LoRA fine-tuning for custom fashion styles
* Fashion prompt engineering
* ChromaDB vector database
* FastAPI backend
* Gradio frontend
* CLIP Score evaluation
* FID Score evaluation
* Fashion metadata management

---

## Tech Stack

* Python
* PyTorch
* Diffusers
* Hugging Face Transformers
* Stable Diffusion XL
* ControlNet
* LoRA (PEFT)
* ChromaDB
* FastAPI
* Gradio
* OpenCV
* Pandas
* Matplotlib

---

## Project Structure

```text
backend/
frontend/
database/
evaluation/
metadata/
scripts/
notebooks/
outputs/
```

---

## Installation

```bash
git clone https://github.com/ayushtonystar-del/fashion_ai.git

cd fashion_ai

pip install -r requirements.txt
```

---

## Run Backend

```bash
python backend/api.py
```

---

## Run Frontend

```bash
python frontend/app.py
```

---

## Project Workflow

1. Dataset Preparation
2. Metadata Generation
3. Prompt Engineering
4. Knowledge Base Creation
5. ChromaDB Indexing
6. SDXL Image Generation
7. ControlNet Conditioning
8. LoRA Fine-tuning
9. Image Evaluation
10. Deployment

---

## Future Improvements

* Multi-GPU Training
* Docker Deployment
* Kubernetes Support
* Fashion Recommendation Engine
* AI Stylist Chatbot
* RAG-powered Fashion Assistant

---

## License

MIT License
