#!/usr/bin/env python3
import sys

OOK_TO_BF = {
    "Ook. Ook?": ">",
    "Ook? Ook.": "<",
    "Ook. Ook.": "+",
    "Ook! Ook!": "-",
    "Ook! Ook.": ".",
    "Ook. Ook!": ",",
    "Ook! Ook?": "[",
    "Ook? Ook!": "]"
}

def ook_to_brainfuck(ook_code):
    # 改行・余計な空白を除去
    ook_code = ook_code.replace("\n", " ").strip()
    words = ook_code.split()

    print(f"🐵 Debug: Ook! words split → {words}")
    print(f"🔢 Total words count: {len(words)} (should be even)")

    # 単語数が偶数であることを確認
    if len(words) % 2 != 0:
        print("🚨 Error: The number of words in Ook! code is not even.", file=sys.stderr)
        print("Received Ook! code:", ook_code, file=sys.stderr)
        raise ValueError("Invalid Ook! code")

    # Brainfuck 変換
    bf_code = []
    loop_balance = 0
    for i in range(0, len(words), 2):
        pair = words[i] + " " + words[i + 1]
        if pair in OOK_TO_BF:
            bf_code.append(OOK_TO_BF[pair])
            if bf_code[-1] == "[":
                loop_balance += 1
            elif bf_code[-1] == "]":
                loop_balance -= 1
        else:
            print(f"🚨 Error: Invalid Ook! instruction '{pair}'", file=sys.stderr)
            print("Received Ook! code:", ook_code, file=sys.stderr)
            raise ValueError("Invalid Ook! code")

    if loop_balance != 0:
        print(f"🚨 Error: Unmatched loop brackets (Balance: {loop_balance})", file=sys.stderr)
        raise ValueError("Unmatched loop brackets in Ook! code")

    return "".join(bf_code)


def execute_brainfuck(bf_code):
    tape = [0] * 30000
    ptr = 0
    output = []
    loop_stack = []
    i = 0

    while i < len(bf_code):
        cmd = bf_code[i]
        if cmd == ">":
            ptr += 1
        elif cmd == "<":
            ptr -= 1
        elif cmd == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == ".":
            output.append(chr(tape[ptr]))
        elif cmd == ",":
            tape[ptr] = ord(sys.stdin.read(1))
        elif cmd == "[":
            if tape[ptr] == 0:
                loop_level = 1
                while loop_level > 0:
                    i += 1
                    if bf_code[i] == "[":
                        loop_level += 1
                    elif bf_code[i] == "]":
                        loop_level -= 1
            else:
                loop_stack.append(i)
        elif cmd == "]":
            if tape[ptr] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1

    print("".join(output), flush=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: ook.py <filename>", flush=True)
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        ook_code = f.read().replace("\n", " ").strip()  # ← 改行をスペースに変換

    bf_code = ook_to_brainfuck(ook_code)
    execute_brainfuck(bf_code)

if __name__ == "__main__":
    main()
