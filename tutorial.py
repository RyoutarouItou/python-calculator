# 簡単な電卓プログラム
# 足し算・引き算・掛け算・割り算ができます


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # 0 で割ることはできない
    return a / b


def read_number(message):
    # 数字が入力されるまで何度でも聞き直す
    while True:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            print("数字を入力してください。")


def main():
    print("=== 簡単な電卓 ===")

    while True:
        print()
        print("計算の種類を選んでください:")
        print("  1: 足し算 (+)")
        print("  2: 引き算 (-)")
        print("  3: 掛け算 (×)")
        print("  4: 割り算 (÷)")
        print("  q: 終了")

        choice = input("番号を入力: ").strip()

        if choice == "q":
            print("電卓を終了します。")
            break

        if choice not in ("1", "2", "3", "4"):
            print("1〜4 か q を入力してください。")
            continue

        a = read_number("1つ目の数: ")
        b = read_number("2つ目の数: ")

        if choice == "1":
            print(f"結果: {a} + {b} = {add(a, b)}")
        elif choice == "2":
            print(f"結果: {a} - {b} = {subtract(a, b)}")
        elif choice == "3":
            print(f"結果: {a} × {b} = {multiply(a, b)}")
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("エラー: 0 で割ることはできません。")
            else:
                print(f"結果: {a} ÷ {b} = {result}")


if __name__ == "__main__":
    main()
