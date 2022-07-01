import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with microphone:
        recognized_data = ""
        print("Проверка микорофна. Скажите что-нибудь")
        audio = recognizer.listen(microphone, None, 5)
recognized_data = recognizer.recognize_google(audio, language="ru").lower()
print("Вы сказали: " + recognized_data.lower())
