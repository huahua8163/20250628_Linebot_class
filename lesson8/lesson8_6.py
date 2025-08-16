import gradio as gr
from google import genai

client = genai.Client()

# 建立gradio Blocks架構
with gr.Blocks() as demo:
    gr.Markdown("## 公司內部機器人")
    #建立輸入框
    input_text = gr.Textbox(label="請輸入您的姓名", placeholder="請輸入您的姓名", submit_btn=True)

    #建立gradio.Accordion
    with gr.Accordion("點擊展開常見Q&A", open=False):
        gr.Examples(
            examples=[
                ["2025國定假日?"],
                ["這個AI機器人可以做什麼?"],
                ["如何聯繫人資部?"],
                ["公司內部規定有哪些?"],
                ["如何申請休假?"],
                ["如何查詢薪資?"],
                ["如何更新個人資料?"],
                ["公司福利有哪些?"],
                ["如何參加培訓課程?"],
                ["如何提交報銷?"]
            ],
            inputs=input_text
        )

 
     #建立輸出框
    output_text = gr.Textbox(
        label="機器人的回覆", 
        placeholder="輸出結果會顯示在這裡",
        interactive=False)

    @input_text.submit(inputs=[input_text], outputs=[output_text])
    def respond(message):
        # 在這裡處理用戶訊息
        response = client.models.generate_content(
           model="gemini-2.5-flash",
           contents=[message]
        )
        return response.text

    demo.launch()
