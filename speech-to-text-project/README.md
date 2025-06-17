# Speech-to-Text Project

This project implements a basic speech-to-text system using pre-trained models and libraries such as SpeechRecognition and Wav2Vec. The system allows users to convert speech from audio files or microphone input into text.

## Project Structure

```
speech-to-text-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── recognizer.py    # Contains the SpeechRecognizer class
│   ├── utils.py         # Utility functions for model loading and audio processing
│   └── config.py        # Configuration settings and constants
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd speech-to-text-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the speech-to-text system, execute the following command:

```
python src/main.py
```

### Features

- **Speech Recognition from Audio Files**: Convert speech from audio files into text.
- **Real-time Speech Recognition**: Capture and convert speech from the microphone in real-time.

## Dependencies

This project requires the following Python libraries:

- SpeechRecognition
- Wav2Vec
- (Any other dependencies listed in `requirements.txt`)

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.