# Spectra

Spectra is a Streamlit-based web application for music source separation using Demucs. The app allows users to upload audio files and separate them into individual components such as vocals, drums, bass, and other instruments.

## Live Demo

Check out the live demo of this application on Hugging Face Spaces: [Live Demo](https://huggingface.co/spaces/Vivek6041/Spectra)

*Note: The live demo may run slower due to the use of 2 vCPUs and 16 GB RAM.*

## Features
- **Audio File Upload**: Supports MP3 and WAV file formats.
- **Model Selection**: Choose from different Demucs models with descriptions.
- **Audio Separation Options**: Select output format and configure shift trick and overlap.
- **Batch Processing**: Process multiple audio files at once.
- **Download Outputs**: Download all separated tracks in a ZIP file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vivekd16/Spectra
   ```

2. Navigate to the project directory:
   ```bash
   cd spectra
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run music_source_separation_app.py
   ```

## Usage

1. Upload your audio files using the file uploader.
2. Select the desired Demucs model and configure the separation options.
3. Click on "Separate Audio" to start the separation process.
4. Download the separated tracks as a ZIP file.
