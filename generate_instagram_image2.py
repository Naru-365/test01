#!/usr/bin/env python3
"""Instagram向けバズ画像を image2 想定プロンプトで生成するスクリプト。"""

from __future__ import annotations

import argparse
import base64
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def build_prompt(theme: str, hook: str) -> str:
    return (
        "Create an Instagram-viral vertical image (1080x1920). "
        f"Theme: {theme}. "
        f"Hook: {hook}. "
        "One dominant focal subject, cinematic lighting, high contrast, premium editorial aesthetic, "
        "ultra-detailed but uncluttered composition, clear depth, emotionally memorable. "
        "No logo, no watermark, no embedded text."
    )


def generate_images(theme: str, hook: str, count: int, out_dir: Path, model: str) -> list[Path]:
    client = OpenAI()
    out_dir.mkdir(parents=True, exist_ok=True)

    prompt = build_prompt(theme=theme, hook=hook)
    created_files: list[Path] = []

    for i in range(count):
        result = client.images.generate(
            model=model,
            prompt=f"{prompt} Variant {i + 1}: add subtle composition change.",
            size="1024x1536",
        )

        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"insta_viral_{timestamp}_{i + 1}.png"
        file_path = out_dir / filename
        file_path.write_bytes(image_bytes)
        created_files.append(file_path)

    return created_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Instagram向け image2 画像生成")
    parser.add_argument("--theme", required=True, help="例: 未来都市×和風ネオン")
    parser.add_argument("--hook", required=True, help="例: 見た瞬間に保存したくなる")
    parser.add_argument("--count", type=int, default=4, help="生成枚数")
    parser.add_argument("--output", default="outputs", help="出力先ディレクトリ")
    parser.add_argument("--model", default="gpt-image-1", help="画像生成モデル名")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    generated = generate_images(
        theme=args.theme,
        hook=args.hook,
        count=args.count,
        out_dir=Path(args.output),
        model=args.model,
    )

    print("生成完了:")
    for p in generated:
        print(f"- {p}")


if __name__ == "__main__":
    main()
