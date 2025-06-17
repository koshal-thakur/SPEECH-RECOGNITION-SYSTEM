def load_model(model_name):
    # Load the specified speech recognition model
    if model_name == "wav2vec":
        from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
        model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
        tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
        return model, tokenizer
    elif model_name == "speech_recognition":
        import speech_recognition as sr
        return sr.Recognizer()
    else:
        raise ValueError("Unsupported model name")

def process_audio(file_path):
    # Preprocess the audio file for recognition
    import librosa
    audio, sr = librosa.load(file_path, sr=None)
    return audio, sr