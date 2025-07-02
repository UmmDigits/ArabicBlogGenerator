if topic.strip() != "":
    st.info("⏳ جاري توليد التدوينة... الرجاء الانتظار")
    
    # 📌 Build the prompt
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

        # 💾 Download option
        st.download_button("💾 تحميل التدوينة كـ .txt", blog, file_name="blog.txt")

    except openai.AuthenticationError:
        st.error("❌ فشل في التحقق من مفتاح API.")
    except openai.RateLimitError:
        st.error("⚠️ تم تجاوز الحد الأقصى للطلبات. الرجاء المحاولة لاحقاً.")
    except openai.OpenAIError as e:
        st.error(f"❌ خطأ من OpenAI: {e}")
    except Exception as e:
        st.error(f"❌ خطأ غير متوقع: {e}")
else:
    st.warning("📌 يرجى إدخال عنوان التدوينة أعلاه.")
