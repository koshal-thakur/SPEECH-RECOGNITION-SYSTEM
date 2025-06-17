import speech_recognition as sr
from recognizer import SpeechRecognizer

def main():
    recognizer = SpeechRecognizer()

    print("Welcome to the Speech-to-Text System!")
    print("Please choose an option:")
    print("1. Recognize from audio file")
    print("2. Recognize from microphone input")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        file_path = input("Enter the path to the audio file: ")
        text = recognizer.recognize_from_file(file_path)
        print("Recognized Text:", text)
    elif choice == '2':
        text = recognizer.recognize_from_mic()
        print("Recognized Text:", text)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()