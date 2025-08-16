import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("""
    # 歡迎使用姓名問候機器人
    請輸入您的姓名，點擊按鈕即可獲得問候語。
    """)
    inout_textbox = gr.Textbox(placeholder="請輸入您的姓名", label="姓名")
    output_textbox = gr.Textbox(label="問候語", placeholder="輸出結果會顯示在這裡")

    @input_textbox.change(inputs=[input_textbox], outputs=[output_textbox])
    def update_output(text):
        return text

demo.launch()