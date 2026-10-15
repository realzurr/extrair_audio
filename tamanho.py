from moviepy.editor import VideoFileClip

# Caminho do vídeo original
input_video_path = "{{arquivo}}.mp4"
output_video_path = "{{Arquivo2}}.mp4"

# Carregar o vídeo
video = VideoFileClip(input_video_path)

# Diminuir a resolução (por exemplo, 720p)
new_resolution = (720,1280)
video_resized = video.resize(new_resolution)

# Reduzir a taxa de bits
# Especificar uma taxa de bits alvo, por exemplo, 500k (500 kbps)
target_bitrate = "500k"

# Salvar o vídeo com a nova resolução e taxa de bits reduzida
video_resized.write_videofile(output_video_path, bitrate=target_bitrate, codec="libx264")

print(f"Vídeo reduzido salvo em {output_video_path}")
