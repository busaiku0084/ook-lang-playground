FROM python:3.9-slim

# パッケージリスト更新
RUN apt-get update && apt-get clean

# 作業ディレクトリを作成
WORKDIR /app

# コンテナが終了しないようにする
CMD ["tail", "-f", "/dev/null"]
