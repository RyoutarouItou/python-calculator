# 電卓のウェブ版（Gradio）
# 計算そのものは tutorial.py の関数を使います

import gradio as gr

from tutorial import add, subtract, multiply, divide

OPERATIONS = {
    "足し算 (+)": ("+", add),
    "引き算 (-)": ("-", subtract),
    "掛け算 (×)": ("×", multiply),
    "割り算 (÷)": ("÷", divide),
}


def calculate(a, b, operation):
    if a is None or b is None:
        return "数字を2つとも入力してください。"

    symbol, func = OPERATIONS[operation]
    result = func(a, b)
    if result is None:
        return "エラー: 0 で割ることはできません。"
    return f"{a} {symbol} {b} = {result}"


with gr.Blocks(title="簡単な電卓") as demo:
    gr.Markdown("# 簡単な電卓")

    with gr.Row():
        a = gr.Number(label="1つ目の数")
        b = gr.Number(label="2つ目の数")

    operation = gr.Radio(
        choices=list(OPERATIONS),
        value="足し算 (+)",
        label="計算の種類",
    )
    button = gr.Button("計算する", variant="primary")
    output = gr.Textbox(label="結果", interactive=False)

    button.click(calculate, inputs=[a, b, operation], outputs=output)


if __name__ == "__main__":
    # 127.0.0.1 は「このパソコンの中だけ」という意味
    demo.launch(server_name="127.0.0.1")
