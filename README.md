# Instagram向け「バズ画像」生成（image2ワークフロー）

このリポジトリは、Instagramで拡散されやすい“縦長・強コントラスト・一目で意味が伝わる”画像を、`image2`想定のプロンプト設計で量産するための最小構成です。

## できること

- 9:16（1080x1920）前提の画像を生成
- フック重視の日本語プロンプトをテンプレ化
- 1回の実行で複数バリエーションを生成

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
```

`.env` を作成して API キーを設定:

```bash
OPENAI_API_KEY=your_api_key
```

## 使い方

```bash
python generate_instagram_image2.py \
  --theme "未来都市×和風ネオン" \
  --hook "見た瞬間に保存したくなる" \
  --count 4
```

生成画像は `outputs/` に保存されます。

## バズりやすくするポイント

1. **最初の0.3秒で意味が伝わる構図**（主役1つ + 背景は引き算）
2. **保存したくなる実用性**（例: before/after、チェックリスト風）
3. **シリーズ化**（色違い・季節違いで連投）
4. **コメント誘導**（「どっちが好き？」の二択デザイン）

`prompts/instagram_viral_image2.md` に、すぐ使える追加プロンプトを用意しています。
