# 🧠 Instruction-Tuned Chat Assistant (LoRA + LLaMA-7B)

A lightweight, instruction-following conversational AI trained using open-source datasets and efficient fine-tuning methods. This is a personal research and engineering project aiming to explore end-to-end fine-tuning, deployment, and optimization of large language models (LLMs).

---

## ✨ Highlights

- ✅ Fine-tunes LLaMA/Mistral 7B using LoRA (parameter-efficient tuning)
- ✅ Uses publicly available instruction datasets (Alpaca, ShareGPT, UltraChat)
- ✅ Runs inference locally via `llama.cpp` on MacBook
- ✅ Lightweight web-based UI with Gradio (WIP)
- ⏳ Multi-stage pipeline with planned deployment to HuggingFace Spaces

---

## 🧠 Project Motivation

Recent advances in instruction-tuned LLMs have enabled conversational agents that can follow user instructions with high fidelity. This project explores how far an individual developer can go with limited compute by leveraging LoRA, quantization, and open datasets to train and deploy a lightweight chat assistant.

---

## 🧪 Current Features

| Stage               | Status | Description                                         |
|---------------------|--------|-----------------------------------------------------|
| Data Cleaning       | ✅ Done  | Converted multiple datasets into standard format     |
| LoRA Fine-tuning    | ✅ Done  | Initial training completed on LLaMA 7B               |
| Inference Testing   | ✅ Done  | Verified output on local machine using ggml format   |
| Web UI              | ⏳ WIP   | Building a Gradio-based chat interface               |
| Deployment Planning | 🔜 Soon | HuggingFace or local API endpoint                    |

---

## 📁 Directory Structure

```text
instruction-chat-llm/
├── data/               # Processed instruction-style datasets
├── training/           # Fine-tuning scripts with PEFT + Transformers
├── inference/          # llama.cpp, ggml model, prompt scripts
├── ui/                 # Web interface (Gradio or Streamlit)
├── docs/               # Internal planning and documentation
└── README.md           # Project overview (this file)
