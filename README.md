# Spectra

Spectra is a Streamlit-based web application for music source separation using Demucs. The app allows users to upload audio files and separate them into individual components such as vocals, drums, bass, and other instruments.

## Live Demo

Check out the live demo : [Live Demo](https://spectra-7wejilybx6qfjyk3ilvrrw.streamlit.app/?embed_options=dark_theme)
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
   streamlit run app.py
   ```

## Usage

1. Upload your audio files using the file uploader.
2. Select the desired Demucs model and configure the separation options.
3. Click on "Separate Audio" to start the separation process.
4. Download the separated tracks as a ZIP file.


## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vivekd16"><br /><sub><b>Vivek Deshmukh</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Himanshu-Lohokane"><br /><sub><b>Himanshu Lohokane</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Maviyamahagami"><br /><sub><b>Maviya Mahagami</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## References
- [Demucs by Facebook Research](https://github.com/facebookresearch/demucs): A state-of-the-art music source separation tool used in this project.
