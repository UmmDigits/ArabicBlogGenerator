import streamlit as st
import openai
from openai import OpenAIError, AuthenticationError, RateLimitError

# Set up your OpenAI API Key
openai.api_key = "your-api-key-here"

st.set_page_config(page_title="Arabic Blog Generator", layout="centered")
st.title("✍️ مولد تدوينات باللغة العربية")

topic = st.text_input("أدخل موضوع التدوينة")
length = st.selectbox("اختر طول التدوينة", ["قصيرة", "متوسطة", "طويلة"])
style = st.selectbox("اختر أسلوب التدوينة", ["رسمي", "غير رسمي"])
tone = st.selectbox("اختر نغمة التدوينة", ["ودي", "مهني", "مرح"])
keywords = st.text_input("أدخل كلمات مفتاحية (اختياري)")

if st.button("أنشئ التدوينة"):
    if topic:
        st.info("جاري توليد التدوينة... الرجاء الانتظار")

        prompt_text = f"اكتب لي تدوينة {length} باللغة العربية حول الموضوع التالي: {topic}. " \
                      f"الأسلوب المطلوب هو {style}، والنغمة هي {tone}."
        if keywords:
            prompt_text += f" الرجاء تضمين هذه الكلمات المفتاحية في التدوينة: {keywords}."

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "أنت كاتب مقالات محترف باللغة العربية."},
                    {"role": "user", "content": prompt_text}
                ]
            )
            st.success("تم التوليد:")
            st.write(response.choices[0].message.content)

        except RateLimitError:
            st.error("لقد تجاوزت الحد الأقصى المسموح به من الاستخدام.")
        except AuthenticationError:
            st.error("مفتاح API غير صحيح.")
        except OpenAIError as e:
            st.error(f"حدث خطأ: {str(e)}")
    else:
        st.warning("يرجى إدخال موضوع التدوينة أولاً.")
