from moviepy.editor import VideoFileClip

# Caminho do vídeo de entrada
video_path = "video.mp4"

# Carregar o vídeo
video = VideoFileClip(video_path)

# Extrair o áudio
audio = video.audio

# Caminho para salvar o áudio extraído
audio_path = "audio_extraido.wav"

# Salvar o áudio extraído
audio.write_audiofile(audio_path)

print(f"Áudio extraído e salvo em {audio_path}")
