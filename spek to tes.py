import speech_recognition as sr

# ایجاد نمونه Recognizer
r = sr.Recognizer()

# استفاده از میکروفون
with sr.Microphone() as source:
    print("لطفاً صحبت کنید...")
    r.adjust_for_ambient_noise(source)  # تنظیم برای نویز محیط
    audio = r.listen(source)  # ضبط صدا

try:
    # تبدیل صدا به متن با Google Speech Recognition
    text = r.recognize_google(audio, language="ar-SA")  # عربی سعودی
    print("متن شما: ", text)
except sr.UnknownValueError:
    print("گوگل نتوانست چیزی بفهمد.")
except sr.RequestError as e:
    print("خطا در ارتباط با سرویس گوگل؛ ", e)
