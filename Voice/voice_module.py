import speech_recognition as sr
from playsound import playsound


key_text_01 = "چطور می تونم کمکتون کنم"


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say the wakeup word to activate the assistant:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    wakeup_word = "استارت"  # Change this to your chosen wakeup word
    try:
        spoken_word = recognizer.recognize_google(audio, language ='fa-IR').lower()
        if wakeup_word in spoken_word:
            print("Assistant activated! What can I do for you?")
            playsound('beep-02.wav')
            playsound('key_voice_01.wav')

            # Add your assistant's functionality here
        else:
            playsound('voice_command_unknown.wav')
            print("Wakeup word not detected.")
    except sr.UnknownValueError:
        playsound('exit_voice_command.wav')
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")

if __name__ == "__main__":
    main()
