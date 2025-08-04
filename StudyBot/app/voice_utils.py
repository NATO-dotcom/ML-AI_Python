import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen(retries=3):
    """
    Listen to the microphone and return recognized text.
    Retries a few times on failure, then returns None.
    """
    for attempt in range(retries):
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower().strip()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError:
            speak("Speech service is unavailable. Please check your internet connection.")
            break
    speak("Failed to recognize speech after several attempts.")
    return None
