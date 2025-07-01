import streamlit as st
import openai
from openai import OpenAIError, AuthenticationError, RateLimitError

# ✅ Set your API key (for local testing only — don’t use this in public apps)
openai.api_key = "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"

# ✅ Streamlit Page Settings
st.set_page_config(page_title="✍️ مولد تدوينات باللغة العربية", layout="centered")
st.title("✍️ مولد تدوينات باللغة العربية")

# ✅ Input fields
topic = st.text_input("📌 أدخل موضوع التدوينة")
length = st.selectbox("📏 اختر طول التدوينة", ["قصيرة", "متوسطة", "طويلة"])
style = st.selectbox("🖋️ اختر الأسلوب", ["رسمي", "غير رسمي"])
tone = st.selectbox("🎯 اختر النغمة", ["ودي", "مهني", "مرح"])
keywords = st.text_input("🔑 كلمات مفتاحية (اختياري)")

# ✅ Generate blog post
if st.button("أنشئ التدوينة"):
    if topic.strip() == "":
        st.warning("⚠️ يرجى إدخال موضوع التدوينة أولاً.")
    else:
        st.info("⏳ جاري توليد التدوينة... الرجاء الانتظار")

        # Create the prompt
        prompt_text = f"اكتب لي تدوينة {length} باللغة العربية حول: {topic}.\n"
        prompt_text += f"الأسلوب: {style}. النغمة: {tone}.\n"
        if keywords:
            prompt_text += f"يرجى تضمين هذه الكلمات المفتاحية: {keywords}."

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "أنت كاتب مقالات محترف باللغة العربية."},
                    {"role": "user", "content": prompt_text}
                ]
            )
            blog = response.choices[0].message.content.strip()
            st.success("✅ تم توليد التدوينة بنجاح!")
            st.write(blog)

       
