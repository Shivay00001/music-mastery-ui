"""
AI Music Mastery - Web Interface
Upload vocal, get fully mastered song with AI-generated instrumental
"""

import gradio as gr
import os
import json
from pathlib import Path

# Import the main system (assumes the previous code is in ai_music_mastery.py)
# For standalone use, include the MusicMasterySystem class here
try:
    from ai_music_mastery import MusicMasterySystem
except ImportError:
    # If running standalone, the classes should be defined above
    pass


def process_vocal(vocal_file, genre, instrumental_service, vocal_gain, instrumental_gain):
    """
    Process uploaded vocal and return mastered song
    """
    if vocal_file is None:
        return None, "Please upload a vocal file", None
    
    try:
        # Initialize system
        system = MusicMasterySystem(instrumental_service=instrumental_service)
        
        # Override mastering gains if custom values provided
        if vocal_gain != 1.2:
            system.mastering.mix_and_master.__defaults__ = (vocal_gain, instrumental_gain)
        
        # Generate output path
        output_path = f"output_{Path(vocal_file.name).stem}_mastered.wav"
        
        # Process
        metadata = system.process(
            vocal_path=vocal_file.name,
            genre=genre.lower(),
            output_path=output_path
        )
        
        # Format metadata for display
        metadata_text = f"""
🎵 **Song Metadata**

**Title:** {metadata['title']}
**Genre:** {metadata['genre'].capitalize()}
**Tempo:** {metadata['tempo_bpm']} BPM
**Key:** {metadata['key']}
**Mood:** {metadata['mood'].capitalize()}
**Duration:** {metadata['duration_seconds']:.1f} seconds

**Copyright:** {metadata['copyright']}
**License:** {metadata['license']}
        """
        
        # Return audio file and metadata
        return output_path, metadata_text, metadata
    
    except Exception as e:
        error_msg = f"❌ Error processing vocal: {str(e)}\n\nPlease check your input file and try again."
        return None, error_msg, None


def create_interface():
    """Create Gradio interface"""
    
    with gr.Blocks(title="AI Music Mastery", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🎵 AI Music Mastery System
        ### Transform your vocals into fully mastered songs with AI-generated instrumentals
        
        Upload your recorded vocal (lyrics + melody) and let AI create a complete, copyright-free song!
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📤 Input")
                
                vocal_input = gr.Audio(
                    label="Upload Vocal Recording",
                    type="filepath",
                    sources=["upload", "microphone"]
                )
                
                genre_input = gr.Dropdown(
                    choices=["Pop", "Rock", "Jazz", "Electronic", "Hip-Hop", "Classical", "Folk", "R&B"],
                    value="Pop",
                    label="Genre"
                )
                
                service_input = gr.Radio(
                    choices=["synthetic", "mubert", "musicgen"],
                    value="synthetic",
                    label="Instrumental Generation Method",
                    info="Synthetic: Fast, local. Mubert: API (requires key). MusicGen: AI model (requires audiocraft)"
                )
                
                with gr.Accordion("Advanced Settings", open=False):
                    vocal_gain_input = gr.Slider(
                        minimum=0.5,
                        maximum=2.0,
                        value=1.2,
                        step=0.1,
                        label="Vocal Volume",
                        info="Adjust vocal loudness in final mix"
                    )
                    
                    instrumental_gain_input = gr.Slider(
                        minimum=0.3,
                        maximum=1.5,
                        value=0.8,
                        step=0.1,
                        label="Instrumental Volume",
                        info="Adjust instrumental loudness in final mix"
                    )
                
                process_btn = gr.Button("🎼 Generate Mastered Song", variant="primary", size="lg")
            
            with gr.Column(scale=1):
                gr.Markdown("### 🎧 Output")
                
                audio_output = gr.Audio(
                    label="Mastered Song",
                    type="filepath"
                )
                
                metadata_output = gr.Markdown(label="Song Information")
                
                metadata_json = gr.JSON(label="Full Metadata", visible=False)
        
        gr.Markdown("""
        ---
        ### 📋 How It Works
        
        1. **Upload** your vocal recording (WAV or MP3)
        2. **Select** your desired genre
        3. **Click** Generate to process
        4. **Download** your mastered song!
        
        The system will:
        - ✅ Analyze your vocal (pitch, tempo, key, mood)
        - ✅ Generate matching AI instrumental
        - ✅ Align tempo and key automatically
        - ✅ Mix and master to studio quality
        - ✅ Create 100% copyright-free music
        
        ### 🔑 API Setup (Optional)
        
        For **Mubert API**: Set environment variable `MUBERT_API_KEY`
        ```bash
        export MUBERT_API_KEY="your_api_key_here"
        ```
        
        For **MusicGen**: Install audiocraft
        ```bash
        pip install audiocraft
        ```
        """)
        
        # Connect button to processing function
        process_btn.click(
            fn=process_vocal,
            inputs=[vocal_input, genre_input, service_input, vocal_gain_input, instrumental_gain_input],
            outputs=[audio_output, metadata_output, metadata_json]
        )
        
        gr.Markdown("""
        ---
        <div style="text-align: center; color: #666;">
        <p>🎵 AI Music Mastery System | 100% Copyright-Free Music Generation</p>
        <p>All generated music is original and royalty-free</p>
        </div>
        """)
    
    return demo


if __name__ == "__main__":
    # Create and launch interface
    demo = create_interface()
    demo.launch(
        share=False,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True
    )
