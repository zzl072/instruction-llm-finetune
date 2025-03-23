# prepare_alpaca.py
# 作用：从 HuggingFace 下载 Alpaca 数据，转换为 JSONL 文件格式

from datasets import load_dataset
import json
import os

def convert_to_jsonl(output_path):
    # 使用 datasets 自动加载 alpaca 数据（只下载一次）
    dataset = load_dataset("tatsu-lab/alpaca")["train"]

    # 如果输出文件夹不存在，就自动创建
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 打开输出文件，逐行写入
    with open(output_path, "w", encoding="utf-8") as f:
        for example in dataset:
            item = {
                "instruction": example["instruction"],
                "input": example["input"],
                "output": example["output"]
            }
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"[INFO] Successfully saved {len(dataset)} training samples to '{output_path}'")

if __name__ == "__main__":
    convert_to_jsonl("data/processed/alpaca_clean.jsonl")
