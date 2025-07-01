import streamlit as st
import openai

# Load API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Arabic Blog Generator", layout="centered")
st.title("✍️ مولد تدوينات باللغة العربية")

topic = st.text_input("أدخل موضوع التدوينة")

if st.button("أنشئ التدوينة"):
    if topic:
        st.info("جاري توليد التدوينة... الرجاء الانتظار")

        prompt_text = f"اكتب لي تدوينة باللغة العربية حول الموضوع التالي: {topic}."

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

        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("يرجى إدخال موضوع التدوينة أولاً.")
