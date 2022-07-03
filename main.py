import pyttsx3
import speech_recognition as sr


'''with microphone:
        recognized_data = ""
        print("Проверка микорофна. Скажите что-нибудь")
        audio = rec.listen(microphone, None, 5)
recognized_data = rec.recognize_google(audio, language="ru").lower()
print("Вы сказали: " + recognized_data.lower())'''

#Test

def record():
        mic = sr.Microphone()
        with mic:
                recognized_data = ""
                recog = sr.Recognizer()
                #mic = sr.Microphone()
                audio = recog.listen(mic, 5, 5)        
                try:
                        recognized_data = recog.recognize_google(audio, language="ru").lower()
                        print("Вы сказали:" + recognized_data.lower())
                except sr.WaitTimeoutError:
                        print("Повторите команду ещё раз")
                        return
                except sr.UnknownValueError:
                        pass
                return recognized_data


'''

diction = {
        name: ("кальцит", "кацит"),
        commands: {
                task_manager: ("диспетчер задач", "открой диспетчер задач"),
                ctrl_panel: ("панель управления", "открой парель управления"),
                browser_search: ("поиск в интернете", "найди в интернете", "поищи", "найди мне"),
                shutdown: ("закройся", "выключись", "отдыхай"),
                open_host: ("открой hosts", "открой файл hosts", "открой файл хостс", "открой хостс", "открой hosts в блокноте",
                                "открой файл hosts в блокноте", "открой хостс в блокноте", "открой файл хостс в блокноте"),
                volume_up: ("увеличь громкость на"),
                volume_down: ("уменьши громкость на"),
                multip: ("умножь на, умножь")
        }
        
}
''' 
def speak(voice):
        print(voice)   
        speak_engine.say(voice)
        speak_engine.runAndWait()
        speak_engine.stop()
speak_engine = pyttsx3.init()

speak("Кальцит слушает")

def main():
        global recog
        global recor
        global mic
        recog = sr.Recognizer()
        mic = sr.Microphone()
        recor = record()

        
if __name__ == '__main__':
        record()