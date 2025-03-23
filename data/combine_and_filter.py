# combine_and_filter.py
# 合并 Alpaca + Dolly，并做 tokenizer 长度过滤

import json
from transformers import AutoTokenizer
import os

# 设置路径
alpaca_path = "data/processed/alpaca_clean.jsonl"
dolly_path = "data/processed/dolly_clean.jsonl"
output_path = "data/processed/combined_filtered.jsonl"

# 加载 Mistral 的 tokenizer
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")


# Token 长度过滤范围
MIN_TOKENS = 10
MAX_TOKENS = 1024

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def count_tokens(example):
    full_input = example["instruction"]
    if example["input"]:
        full_input += " " + example["input"]
    full_input += " " + example["output"]
    return len(tokenizer.encode(full_input))

def main():
    alpaca = load_jsonl(alpaca_path)
    dolly = load_jsonl(dolly_path)

    combined = alpaca + dolly
    print(f"[INFO] Combined total: {len(combined)} examples")

    filtered = []
    for ex in combined:
        num_tokens = count_tokens(ex)
        if MIN_TOKENS <= num_tokens <= MAX_TOKENS:
            filtered.append(ex)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for ex in filtered:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")

    print(f"[INFO] After filtering by token length [{MIN_TOKENS}, {MAX_TOKENS}]: {len(filtered)} samples")
    print(f"[INFO] Saved to: {output_path}")


if __name__ == "__main__":
    main()
