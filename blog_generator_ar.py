import streamlit as st
import openai
from openai import error as openai_error

# Set up your OpenAI API Key
openai.api_key = "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"

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

        except openai_error.RateLimitError:
            st.error("لقد تجاوزت الحد الأقصى المسموح به من الاستخدام. يرجى التحقق من خطتك وبيانات الفوترة.")
        except openai_error.AuthenticationError:
            st.error("حدث خطأ في المصادقة. يرجى التأكد من صحة مفتاح API.")
        except openai_error.OpenAIError as e:
            st.error(f"حدث خطأ أثناء الاتصال بـ OpenAI: {str(e)}")

    else:
        st.warning("يرجى إدخال موضوع التدوينة أولاً.")
