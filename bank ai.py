import os
import uuid
import time
import threading
import tkinter as tk
from PIL import Image, ImageTk
import pygame
from gtts import gTTS
import speech_recognition as sr
from openai import OpenAI
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

#pic folder and anim frame
IMAGE_FOLDER = "img"    # 0-10.png
FRAME_DELAY = 100       # ms
pygame.mixer.init()

# llm api
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",  # Ollama local
    api_key="ollama",                        # dummy
)
MODEL = "gpt-oss:20b-cloud"

# class Assistant
class VoiceAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("VoiceAssistant")
        self.root.resizable(False, False)

        # load frame
        self.frames = []
        for i in range(11):
            img_path = os.path.join(IMAGE_FOLDER, f"{i}.png")
            if os.path.exists(img_path):
                img = Image.open(img_path).resize((300, 300))
                self.frames.append(ImageTk.PhotoImage(img))

        self.label = tk.Label(root, image=self.frames[0])
        self.label.pack(pady=10)

        # start buttm
        self.start_button = tk.Button(root, text="▶️ start", command=self.start_welcome)
        self.start_button.pack(pady=10)

        self.animating = False
        self.current_frame = 0

        # llm chat
        self.conversation = [{"role": "system", "content": "You are a test helpful bank assistant. Speak Arabic. Keep all answers short, max 2 sentences."}]

        # step by step control
        self.busy = False  # True when voice play

    # wellcome
    def start_welcome(self):
        self.start_button.pack_forget()
        welcome_text = "مرحباً! أنا مساعد الذكاء الاصطناعي في البنك. هل يمكنني مساعدتك؟"
        self.busy = True
        threading.Thread(target=self.speak_text, args=(welcome_text, True), daemon=True).start()

    # start listening 
    def start_listening(self):
        threading.Thread(target=self.listen_loop, daemon=True).start()

    #loop listening
    def listen_loop(self):
        r = sr.Recognizer()
        while True:
            # wait untill finish answer
            while self.busy:
                time.sleep(0.1)

            with sr.Microphone() as source:
                print("\n🎙️ Speak please")
                r.adjust_for_ambient_noise(source)
                try:
                    audio = r.listen(source, timeout=6)
                except Exception:
                    continue

            try:
                user_text = r.recognize_google(audio, language="ar-SA")
                print(f"📝 You siad: {user_text}")

                if user_text.lower() in ["exit", "quit"]:
                    print("👋 bye!")
                    self.root.quit()
                    break

                # add user message to chat
                self.conversation.append({"role": "user", "content": user_text})

                # recive answer LLM
                self.busy = True
                threading.Thread(target=self.get_llm_response, daemon=True).start()

            except sr.UnknownValueError:
                print("❌ لم أفهم ما كنت تقوله")
            except sr.RequestError:
                print("⚠️ خطأ في خدمة التعرف على الكلام")

    # play voice answer llm
    def get_llm_response(self):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=self.conversation
            )
            reply = resp.choices[0].message.content.strip()
            print(f"🤖 answer assistant: {reply}")

            # add answet text ro chat
            self.conversation.append({"role": "assistant", "content": reply})

            # play voice and animation
            self.speak_text(reply)

        except Exception as e:
            print(f"❌ Error in LLM: {e}")
            self.busy = False

    # convert text to audio and play
    def speak_text(self, text, is_welcome=False):
        filename = f"reply_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang='ar')
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        self.animating = True
        self.animate()

        # if isset welcome 
        if is_welcome:
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            self.busy = False
            self.start_listening()
        else:
            threading.Thread(target=self.cleanup_file, args=(filename,), daemon=True).start()

    # animation
    def animate(self):
        if self.animating and pygame.mixer.music.get_busy():
            self.label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(FRAME_DELAY, self.animate)
        else:
            self.animating = False
            self.label.config(image=self.frames[0])
            self.busy = False

    # remove mp3 
    def cleanup_file(self, filename):
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        try:
            pygame.mixer.music.unload()
        except:
            pass
        time.sleep(0.2)
        try:
            os.remove(filename)
        except:
            print(f"⚠️ الملف {filename} لا يزال قيد الاستخدام، لا يمكن حذفه")

# run main
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistant(root)
    root.mainloop()
