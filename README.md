# ook-lang-playground

🐄 Ook! 言語で "Hello World!" 🐵🚀

## **📌 Ook! とは？**
Ook! は、Brainfuck をベースにした **難解プログラミング言語** です。
**「Ook.」「Ook?」「Ook!」** の3つの単語だけを組み合わせてプログラムを書きます。
本来はオランウータンのための言語（という設定）ですが、人間でも頑張れば書けます。💡

## **📂 ファイル構成**
```
📂 ook-lang-playground
├── 📄 README.md          # ← このファイル！
├── 📜 Dockerfile         # Ook! 実行環境を構築するための Dockerfile
├── 📜 docker-compose.yml # 環境構築と実行を簡単にするための設定
├── 📜 ook.py             # Ook! を Brainfuck に変換して実行するスクリプト
└── 📜 hello.ook          # "Hello World!" を出力する Ook! コード
```

## **🚀 環境構築**
### **1️⃣ Docker を使って環境を準備**
```sh
docker-compose build
```

### **2️⃣ コンテナを起動**
```sh
docker-compose up -d
```

## **🎉 Ook! で `Hello World!` を実行**
### **🐵 実行コマンド**
```sh
docker-compose exec ook-lang python3 /app/ook.py /app/hello.ook
```

**📝 出力例**
```sh
🐵 Debug: Ook! words split → ['Ook.', 'Ook?', ..., 'Ook.', 'Ook!']
🔢 Total words count: 282 (should be even)
Hello World!
```

### **📜 `hello.ook` のコード**
`hello.ook` の中身は **282単語** の Ook! コードで構成されており、
Brainfuck に変換されて `Hello World!` を出力します。

```txt
Ook. Ook? Ook. Ook? Ook. Ook? Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook? Ook! Ook.
...
(省略: 約280単語の Ook! コード)
...
Ook. Ook. Ook! Ook.
```

### **🐵 Ook! の文法**
| Ook! コード | Brainfuck 相当 | 説明 |
|------------|--------------|------|
| `Ook. Ook?` | `>`  | ポインタを右へ移動 |
| `Ook? Ook.` | `<`  | ポインタを左へ移動 |
| `Ook. Ook.` | `+`  | メモリの値を1増やす |
| `Ook! Ook!` | `-`  | メモリの値を1減らす |
| `Ook! Ook.` | `.`  | メモリの値を出力 |
| `Ook. Ook!` | `,`  | 入力を受け取る |
| `Ook! Ook?` | `[`  | ループ開始 |
| `Ook? Ook!` | `]`  | ループ終了 |

## **📝 その他**
- 公式 Ook! の仕様は [ここ](https://esolangs.org/wiki/Ook!) で確認できます。
- もし **`hello.ook` の単語数が奇数** だったら、間違いなくエラーになります！🚨
- `Brainfuck` と同じくらいの難易度なので、**書くのはかなり大変です！** 🐵🔥
