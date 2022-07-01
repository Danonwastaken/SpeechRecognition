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

diction = {
        "name": ("кальцит", "кацит"),
        "commands": {
                "task_manager": ("диспетчер задач", "открой диспетчер задач"),
                "ctrl_panel": ("панель управления", "открой парель управления"),
                "browser_search": ("поиск в интернете", "найди в интернете", "поищи", "найди мне"),
                "shutdown": ("закройся", "выключись", "отдыхай"),
                "open_host": ("открой hosts", "открой файл hosts", "открой файл хостс", "открой хостс", "открой hosts в блокноте",
                                "открой файл hosts в блокноте", "открой хостс в блокноте", "открой файл хостс в блокноте"),
                "volume_up": ("увеличь громкость на"),
                "volume_down": ("уменьши громкость на"),
                "Multip": ("Умножь")
        }
        
}
