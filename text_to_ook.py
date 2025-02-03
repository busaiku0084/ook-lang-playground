import sys

BF_TO_OOK = {
    ">": "Ook. Ook?",
    "<": "Ook? Ook.",
    "+": "Ook. Ook.",
    "-": "Ook! Ook!",
    ".": "Ook! Ook.",
    ",": "Ook. Ook!",
    "[": "Ook! Ook?",
    "]": "Ook? Ook!"
}

def text_to_brainfuck(text):
    bf_code = []
    prev_ascii = 0  # 直前の ASCII 値を保持

    for char in text:
        if char == "\n":
            bf_code.append("\n")  # **改行をそのまま記録**
            prev_ascii = 0  # **改行後の文字の ASCII 調整**
            continue

        ascii_val = ord(char)  # 文字をASCIIコードに変換
        diff = ascii_val - prev_ascii  # 前の文字との差分を計算

        if diff > 0:
            bf_code.append("+" * diff)  # 差分の分だけ `+` を増やす
        elif diff < 0:
            bf_code.append("-" * abs(diff))  # 差分の分だけ `-` を増やす

        bf_code.append(".")  # 出力
        prev_ascii = ascii_val  # 現在の ASCII 値を記録

    return "".join(bf_code)

def brainfuck_to_ook(bf_code):
    ook_code = []
    for c in bf_code:
        if c == "\n":
            ook_code.append("\n")  # **改行をそのまま維持**
        elif c in BF_TO_OOK:
            ook_code.append(BF_TO_OOK[c])
    return " ".join(ook_code)

def text_to_ook(text):
    bf_code = text_to_brainfuck(text)
    return brainfuck_to_ook(bf_code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 text_to_ook.py 'Hello\nWorld'")
        sys.exit(1)

    text = sys.argv[1]
    ook_code = text_to_ook(text)

    # **ファイルに保存**
    with open("output.ook", "w") as f:
        f.write(ook_code + "\n")  # **最後に改行を追加**

    # **標準出力にも表示**
    print("\n🐵 **Generated Ook! Code:**")
    print(ook_code)
    print("\n✅ Saved to output.ook")
