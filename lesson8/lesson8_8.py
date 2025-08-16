import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## Text to Summarization(總結)")
    style_radio = gr.Radio(choices=["口語", "學術","專業","簡潔","俏皮"], label="摘要風格")
    input_text = gr.Textbox(
        label="請輸入要總結的文本", 
        placeholder="請輸入要總結的文本", 
        lines=10, 
        submit_btn=True
    )
    output_md = gr.Markdown()

    @input_text.submit(inputs=[input_text, style_radio], outputs=[output_md])
    def summarize(text, style):
        if style == "口語":
            style = "請轉換口語風格\n"
        elif style == "學術":
            style = "請使用學術風格\n"
        elif style == "專業": 
            style = "請使用專業風格\n"
        elif style == "簡潔":
            style = "請總結簡潔風格\n"
        elif style == "俏皮":
            style = "請變成俏皮風格\n"
            
        summary = f"風格: {style}\n\n{text}"
        return summary

    demo.launch()