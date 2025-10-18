
# 🏦 AI Voice Banking Assistant
## 🎥 Local Demo

[📽️ Click here to watch the demo](Record_2025_10_18_22_56_56_694.mp4)

This project is an **AI-powered voice banking assistant** that can interact with users through voice commands.  
It listens to spoken input, generates intelligent responses using an LLM (Large Language Model), and replies back with **text-to-speech** along with **visual animations** for a better user experience.

---

## ✨ Features

- 🎤 **Voice Recognition** – Captures user voice using `speech_recognition`  
- 🤖 **AI Response Generation** – Uses an online LLM API for smart and short answers  
- 🔊 **Text-to-Speech Output** – Converts the assistant’s response into clear audio using `gTTS`  
- 🖼️ **Animated Interface** – Plays an animation during interaction to simulate a real assistant  
- ⏳ **Step-by-Step Execution** – Ensures sound is played fully before the next step starts  
- 👋 **Welcome Message** – Plays a short introduction message at startup

---

## 🧰 Technologies Used

- Python 3.10+
- `speech_recognition`
- `gtts`
- `pygame` (for sound playback)
- `os` and `time` modules
- LLM API (for generating assistant responses)


## 🚀 How to Run

1. Clone the repository or download the project:
   ```bash
   git clone https://github.com/saeedt70/Bank-voice-assistant.git
   cd voice-banking-assistant
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the assistant:

   ```bash
   python main.py
   ```

4. Speak when prompted and wait for the AI to respond with voice and animation 🎧

---

## ⚡ Example Interaction

```
🗣️ You say: “Hi, what can you do?”
🤖 Assistant replies: “I can help with your banking services.”
🔊 Voice plays with animation


## 🧭 Future Improvements

* Add multilingual support 🌍
* Integrate with real banking APIs (sandbox mode)
* Add chatbot memory and personalized answers
* Create a GUI dashboard


## 👨‍💻 Author

Developed by **saeed taheri**
📧 [your.email@example.com](mailto:saeedt70@gmail.com)
GitHub: [yourusername](https://github.com/saeedt70)




