import yt_dlp

# Função para listar as qualidades disponíveis
def listar_qualidades(url):
    ydl_opts = {
        'listformats': True  # Configura o yt-dlp para listar os formatos
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)  # Extrai as informações do vídeo sem baixar

        if result:
          if 'formats' in result:
              formats = [f"Ext: {format['ext']} - Resolução: {format.get('resolution', 'N/A')} - FPS: {format.get('fps', 'N/A')}" for format in result['formats']]
              formats.sort(key=lambda format:format.split(' ')[1])
              for format in formats:
                  print(format)
          else:
              print("Não foi possível obter as qualidades do vídeo.")

# URL do vídeo que você deseja analisar
url_do_video = 'https://www.youtube.com/watch?v=4jm-1EcLWM4'

listar_qualidades(url_do_video)