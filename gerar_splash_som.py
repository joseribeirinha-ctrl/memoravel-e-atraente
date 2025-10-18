# gerar_splash_som.py
import requests
from io import BytesIO
from pydub import AudioSegment
URL_ONDAS = "https://cdn.pixabay.com/download/audio/2022/03/15/audio_13c24a0b12.mp3?filename=ocean-waves-ambient-19999.mp3"
URL_ACORDE = "https://cdn.pixabay.com/download/audio/2021/09/02/audio_94c8a4e1b7.mp3?filename=orchestral-soft-intro-116199.mp3"
OUTPUT_PATH = "public/sounds/splash-sound.mp3"
def download_mp3(url):
    resp = requests.get(url); resp.raise_for_status(); return AudioSegment.from_file(BytesIO(resp.content), format="mp3")
ondas = download_mp3(URL_ONDAS)[:2000]; acorde = download_mp3(URL_ACORDE)[:1500]
ondas = ondas - 3; acorde = acorde - 6
mix = ondas.fade_in(200).overlay(acorde.fade_in(300).fade_out(400), position=1200); mix = mix.fade_out(400)
mix.export(OUTPUT_PATH, format="mp3", bitrate="320k")
print("✅ Som gerado em:", OUTPUT_PATH)