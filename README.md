# AI Music Mastery - Web Interface

A sleek Gradio-based web interface for the AI Music Mastery system. This application allows users to upload a vocal track (or record via microphone), select a genre, and automatically generate a fully mastered song with an AI-generated instrumental track.

## 🚀 Key Features

- **Vocal Uploads**: Upload your vocals via file (`.wav`, `.mp3`) or record directly from your microphone.
- **Genre Selection**: Choose from popular genres including Pop, Rock, Jazz, Electronic, Hip-Hop, Classical, Folk, and R&B.
- **Instrumental Generators**: Supports multiple backend generation methods:
  - **Synthetic**: Fast, local synthetic generation.
  - **Mubert API**: Requires a Mubert API key for generation.
  - **MusicGen**: AI model integration (requires `audiocraft`).
- **Advanced Mixing**: Fine-tune the final output by adjusting individual vocal and instrumental volume gains.
- **Rich Metadata Output**: Returns song metadata including Title, Tempo, Key, Mood, Duration, and Licensing information.

## ⚙️ Prerequisites

- Python 3.8+
- `gradio` package

*Note: The actual AI processing backend (`ai_music_mastery.py`) must be present in the same directory for the system to process audio. If not present, the UI will still load standalone for demonstration.*

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shivay00001/music-mastery-ui.git
   cd music-mastery-ui
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) For advanced generation methods:
   - **Mubert**: Set your API key via `export MUBERT_API_KEY="your_api_key_here"`
   - **MusicGen**: Install audiocraft (`pip install audiocraft`)

## 💻 Usage

Start the web interface by running:
```bash
python music_mastery_ui.py
```
The application will launch a local web server (usually at `http://127.0.0.1:7860`). Open this address in your web browser to interact with the system.

## License
This project is licensed under the terms provided in the LICENSE file.

## 🐳 Docker Support

Run the web interface easily via Docker:

`ash
docker compose up --build
`

The UI will be available at http://localhost:7860
