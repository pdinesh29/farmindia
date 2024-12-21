from django.shortcuts import render
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# if api_key is None:
#     print("API Key not found! Check the .env file.")
# genai.configure(api_key=api_key)

# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-2.0-flash-exp",
#   generation_config=generation_config,
# )

# chat_session = model.start_chat(
#   history=[
#   ]
# )
# x=str(input())
# response = chat_session.send_message(x)

# print(response.text)
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')