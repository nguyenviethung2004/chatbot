from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
import time


def generate_groq_response(prompt: str) -> str:
   start = time.time()
   api_key = os.getenv("GROK_API_KEY")
   

   if not api_key:
      raise ValueError("❌ Không tìm thấy GROQ_API_KEY trong file .env")
   
   client = Groq(api_key=api_key)

   try:
      response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,     
            max_tokens=512       
        )
      print(f"⏱️ Thời gian gọi Groq API: {time.time() - start:.2f} giây")
      return response.choices[0].message.content.strip()

   except Exception as e:
        print("❌ Lỗi khi gọi Groq API:", e)
        return "Lỗi khi gọi mô hình."



# if __name__ == "__main__":

#     prompt = """

# """

#     # 🚀 Gọi hàm sinh tóm tắt
#     summary = ask_groq(prompt)
#     print("📘 Tóm tắt hội thoại:\n")
#     print(summary)
    

