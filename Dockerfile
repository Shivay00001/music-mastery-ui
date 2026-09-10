FROM python:3.9-slim

# Install ffmpeg for audio processing (often required by music libraries)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Gradio port
EXPOSE 7860

# Set environment variable to make Gradio listen on all interfaces
ENV GRADIO_SERVER_NAME="0.0.0.0"

ENTRYPOINT ["python", "music_mastery_ui.py"]
