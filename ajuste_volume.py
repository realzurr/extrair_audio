from pydub import AudioSegment
from pydub.effects import normalize

# Caminho do áudio extraído
audio_path = "audio_extraido.wav"

# Carregar o áudio com pydub
audio = AudioSegment.from_wav(audio_path)

# Normalizar o volume do áudio
normalized_audio = normalize(audio)

# Caminho para salvar o áudio processado
processed_audio_path = "audio_processado_volume.wav"

# Salvar o áudio processado
normalized_audio.export(processed_audio_path, format="wav")

print(f"Áudio processado e salvo em {processed_audio_path}")
