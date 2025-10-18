from gtts import gTTS

# 📝 متن عربی مورد نظر
arabic_text = "اي، تمت العملية بنجاح. مشكور، وإن شاء الله نشوفك مرّة ثانية"

# 🗣️ ساخت فایل صوتی با زبان عربی
tts = gTTS(text=arabic_text, lang='ar')

# 💾 ذخیره کردن فایل صوتی
tts.save("voice.mp3")

print("✅ فایل صوتی با موفقیت ساخته شد!")
