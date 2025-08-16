import gradio as gr

def greet(name):
    return name + "您好!"

with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="請輸入姓名", placeholder="請輸入您的姓名")
    output_textbox = gr.Textbox(label="輸出的位置", placeholder="輸出結果會顯示在這裡")
    greet_button = gr.Button("點擊我")
    
    @greet_button.click(
        inputs=[name_textbox],
        outputs=[output_textbox]
    )
    def greet(name):
        return name + "您好!"
    
demo.launch()