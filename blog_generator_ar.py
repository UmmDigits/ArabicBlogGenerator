if st.button("أنشئ التدوينة"):
    if topic:
        st.info("جاري توليد التدوينة... الرجاء الانتظار")

        prompt_text = f"اكتب لي تدوينة {length} باللغة العربية حول الموضوع التالي: {topic}. " \
                      f"الأسلوب المطلوب هو {style}، والنغمة هي {tone}."
        if keywords:
            prompt_text += f" الرجاء تضمين هذه الكلمات المفتاحية في التدوينة: {keywords}."

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "أنت كاتب مقالات محترف باللغة العربية."},
                    {"role": "user", "content": prompt_text}
                ]
            )

            st.success("تم التوليد:")
            st.write(response.choices[0].message.content)

        except RateLimitError:
            st.error("لقد تجاوزت الحد الأقصى المسموح به من الاستخدام. يرجى التحقق من خطتك وبيانات الفوترة.")
        except AuthenticationError:
            st.error("حدث خطأ في المصادقة. يرجى التأكد من صحة مفتاح API.")
        except OpenAIError as e:
            st.error(f"حدث خطأ أثناء الاتصال بـ OpenAI: {str(e)}")

    else:
        st.warning("يرجى إدخال موضوع التدوينة أولاً.")
