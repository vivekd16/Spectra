import streamlit as st
import os
import subprocess
import zipfile

# Function to run Demucs

def run_demucs(audio_file_path, audio_format, model, shift_trick, overlap):
    output_dir = "./separated_tracks"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    command = [
        'demucs',
        '-n', model,
        '-o', output_dir,
        '--mp3' if audio_format == 'mp3' else '--flac' if audio_format == 'flac' else '',
        '--shifts', str(shift_trick),
        '--overlap', str(overlap),
        audio_file_path
    ]
    # Remove empty strings from command
    command = [arg for arg in command if arg]
    subprocess.run(command, check=True)
    return output_dir

# Function to create a ZIP archive of the output directories
def create_zip(output_dirs, zip_name="output.zip"):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for dir_path in output_dirs:
            for root, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=os.path.dirname(dir_path))
                    zipf.write(file_path, arcname)
    return zip_name

# Model descriptions
demucs_models = {
    "htdemucs": "High-Quality Demucs model for general use.",
    "htdemucs_ft": "Fine-tuned version of htdemucs for better separation.",
    "mdx_extra_q": "Extra quality model for more detailed separation."
}

# Streamlit app layout
st.title('Spectra')

# File uploader for audio source
uploaded_files = st.file_uploader("Choose audio files", type=["mp3", "wav"], accept_multiple_files=True)

# Model selection with descriptions
selected_model = st.selectbox("Select Demucs Model", list(demucs_models.keys()), format_func=lambda x: f"{x} - {demucs_models[x]}")

# Audio format selection
audio_format = st.selectbox("Select Output Format", ["wav", "mp3", "flac"])

# Shift trick slider
shift_trick = st.slider("Select Number of Shifts for Shift Trick", min_value=0, max_value=10, value=0)

# Overlap slider
overlap = st.slider("Select Overlap Percentage", min_value=0.0, max_value=0.9, value=0.25, step=0.05)

# Button to trigger separation
if st.button('Separate Audio'):
    output_dirs = []  # List to store output directories for each file
    if uploaded_files:
        for uploaded_file in uploaded_files:
            audio_file_path = os.path.join("./", uploaded_file.name)
            with open(audio_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.info(f"Processing {uploaded_file.name}... This may take a while.")
            try:
                output_dir = run_demucs(audio_file_path, audio_format, selected_model, shift_trick, overlap)
                output_dirs.append(os.path.join(output_dir, selected_model, os.path.splitext(uploaded_file.name)[0]))
                st.success(f"{uploaded_file.name} separated successfully! Check below for the output files.")
                # Display output audio files
                audio_files = [f for f in os.listdir(os.path.join(output_dir, selected_model, os.path.splitext(uploaded_file.name)[0])) if f.endswith(('.mp3', '.wav', '.ogg', '.flac'))]
                for audio_file in audio_files:
                    st.audio(os.path.join(output_dir, selected_model, os.path.splitext(uploaded_file.name)[0], audio_file))
            except subprocess.CalledProcessError:
                st.error(f"An error occurred while processing {uploaded_file.name}.")
        # Create a ZIP file of all outputs
        zip_name = create_zip(output_dirs)
        with open(zip_name, "rb") as f:
            st.download_button("Download all outputs as ZIP", f, file_name=zip_name)
    else:
        st.error("Please upload audio files to proceed.")
