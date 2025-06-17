class SpeechRecognizer:
    def __init__(self, model):
        self.model = model

    def recognize_from_file(self, file_path):
        # Load audio file and recognize speech
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)  # read the entire audio file
        try:
            text = recognizer.recognize_google(audio)  # using Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

    def recognize_from_mic(self):
        # Recognize speech from microphone
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please speak something...")
            audio = recognizer.listen(source)  # listen for the first phrase and extract it into audio data
        try:
            text = recognizer.recognize_google(audio)  # using Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"