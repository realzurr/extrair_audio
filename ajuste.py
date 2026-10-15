from pydub import AudioSegment
from pydub.effects import normalize
import noisereduce as nr
import numpy as np
import wave

# Caminho do áudio extraído
audio_path = "audio_extraido.wav"

# Carregar o áudio com pydub
audio = AudioSegment.from_wav(audio_path)

# Normalizar o volume do áudio
normalized_audio = normalize(audio)

# Converter o áudio normalizado para um array numpy para redução de ruído
samples = np.array(normalized_audio.get_array_of_samples())

# Obter a taxa de amostragem do áudio
with wave.open(audio_path, "rb") as wav_file:
    sr = wav_file.getframerate()

# Aplicar redução de ruído
reduced_noise = nr.reduce_noise(y=samples, sr=sr)

# Criar um novo áudio a partir do array com redução de ruído
denoised_audio = normalized_audio._spawn(reduced_noise)

# Caminho para salvar o áudio processado
processed_audio_path = "audio_processado.wav"

# Salvar o áudio processado
denoised_audio.export(processed_audio_path, format="wav")

print(f"Áudio processado e salvo em {processed_audio_path}")
