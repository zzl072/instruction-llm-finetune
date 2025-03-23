# prepare_dolly.py
# 将 Dolly-15k 数据集转换为标准 Alpaca-style JSONL 格式

from datasets import load_dataset
import json
import os

def convert_dolly_to_jsonl(output_path):
    # 加载 Dolly 数据集
    dataset = load_dataset("databricks/databricks-dolly-15k")["train"]

    # 创建输出目录
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for example in dataset:
            instruction = example["instruction"]
            context = example["context"]
            response = example["response"]

            # input = context 或空字符串
            item = {
                "instruction": instruction,
                "input": context if context else "",
                "output": response
            }
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"[INFO] Saved {len(dataset)} samples to '{output_path}'")

if __name__ == "__main__":
    convert_dolly_to_jsonl("data/processed/dolly_clean.jsonl")
