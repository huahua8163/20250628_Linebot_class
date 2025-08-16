import gradio as gr
from google import genai
from google.genai import types
client = genai.Client()

with gr.Blocks() as demo:
    gr.Markdown("## Text to Summarization(總結)")
    style_radio = gr.Radio(choices=["口語", "小學","專業","簡潔","俏皮"], label="摘要風格")
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
        elif style == "小學":
            style = "請使用小學生看得懂的風格\n"
        elif style == "專業": 
            style = "請使用專業風格\n"
        elif style == "簡潔":
            style = "請總結簡潔風格\n"
        elif style == "俏皮":
            style = "請變成俏皮風格\n"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=f"""你是一個專業的總結助手,請根據用戶提供的文本進行總結。
                你需要根據用戶選擇的風格進行總結。請確保總結的內容清晰且符合所選風格。
                目前使用者選擇的是{style}風格。
                
                所有的回覆必須是mardown語法。"""
            ),
            contents=[text]
        )
        


        summary = f"風格: {style}\n\n{response.text}"
        return summary

    demo.launch()