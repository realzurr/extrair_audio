'# Extração e processamento de áudio/vídeo

Este repositório contém scripts em Python para:

- extrair áudio de um vídeo;
- reduzir ruído do áudio;
- ajustar volume;
- reduzir o tamanho/resolução de um vídeo.

## Estrutura do projeto

- `extrair.py` — extrai o áudio de `video.mp4` e salva em `audio_extraido.wav`.
- `ajuste.py` — aplica redução de ruído e salva em `audio_processado.wav`.
- `ajuste_volume.py` — normaliza o volume do áudio e salva em `audio_processado_volume.wav`.
- `tamanho.py` — redimensiona um vídeo e reduz a bitrate de saída.

## Requisitos

Antes de executar os scripts, instale as dependências:

```bash
pip install moviepy pydub noisereduce numpy
```

Se necessário, também pode instalar `ffmpeg`, porque o `moviepy` depende dele para processamento de vídeo/áudio.

## Como usar

### 1) Extrair áudio do vídeo

Coloque o vídeo de entrada em um arquivo chamado `video.mp4` na raiz do projeto e execute:

```bash
python extrair.py
```

Isso gera:

- `audio_extraido.wav`

### 2) Reduzir ruído do áudio

```bash
python ajuste.py
```

Isso gera:

- `audio_processado.wav`

### 3) Ajustar volume do áudio

```bash
python ajuste_volume.py
```

Isso gera:

- `audio_processado_volume.wav`

### 4) Reduzir tamanho do vídeo

Abra o arquivo `tamanho.py` e ajuste os caminhos de entrada e saída:

```python
input_video_path = "seu_video.mp4"
output_video_path = "video_reduzido.mp4"
```

Depois execute:

```bash
python tamanho.py
```

## Observações

- Os arquivos gerados (`.wav`, `.mp4`) são ignorados pelo Git por meio do arquivo `.gitignore`.
- O arquivo `.env` pode ser usado para armazenar variáveis locais sensíveis, sem enviá-las para o GitHub.
- Os scripts estão configurados de forma simples e direta, sem interface gráfica, então o uso é feito por linha de comando.

## Exemplo de fluxo completo

```bash
python extrair.py
python ajuste.py
python ajuste_volume.py
python tamanho.py
```

## Licença

Este projeto não possui uma licença específica definida no momento.
