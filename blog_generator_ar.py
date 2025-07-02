import streamlit as st
import openai
from openai import OpenAIError, AuthenticationError, RateLimitError

# Load API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Page settings
st.set_page_config(page_title="Arabic Blog Generator", layout="centered")
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

        except AuthenticationError:
            st.error("❌ فشل في التحقق من مفتاح API.")
        except RateLimitError:
            st.error("⚠️ تم تجاوز الحد الأقصى لعدد الطلبات. الرجاء المحاولة لاحقاً.")
        except OpenAIError as e:
            st.error(f"❌ حدث خطأ من OpenAI: {e}")
        except Exception as e:
            st.error(f"❌ خطأ غير متوقع: {e}")
