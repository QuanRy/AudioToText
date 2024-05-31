# ---------------------------------------------- БИБЛИОТЕКИ ------------------------------------------------------------
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os
# ----------------------------------------------------------------------------------------------------------------------

def extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath):  # Извлечение аудио дорожки из видео

    # Загружаем видео и извлекаем аудио как временный файл
    video_clip = VideoFileClip(video_filepath)
    temp_audio_filepath = "temp_audio.mp3"                 # Используем временный файл для аудио
    video_clip.audio.write_audiofile(temp_audio_filepath)

    audio = AudioSegment.from_file(temp_audio_filepath)
    audio = audio.set_channels(1)                         # Преобразуем в моно
    audio = audio.set_frame_rate(16000)                # Устанавливаем частоту дискретизации 16kHz

    audio.export(output_audio_filepath, format="wav", parameters=["-acodec", "pcm_s16le"])   # Сохраняем обработанное аудио в .WAV

    # Удаляем временный аудиофайл
    os.remove(temp_audio_filepath)
    print (" Видео успешно переконвертировано!")

def convert_audio_to_wav (input_audio_filepath, output_wav_audio_filepath):       # Конвертируем аудио файл в расширение .WAV
    audio = AudioSegment.from_file(input_audio_filepath)
    audio = audio.set_channels(1)                       # Преобразуем в моно
    audio = audio.set_frame_rate(16000)              # Устанавливаем частоту дискретизации 16kHz

    audio.export(output_wav_audio_filepath, format="wav", parameters=["-acodec", "pcm_s16le"])  # Сохраняем обработанное аудио в WAV
    print(" Аудио успешно переконвертировано!")

def continue_process_transcription(audio_filepath):          # Продолжение траснкрибации - определение формата
    output_audio_filepath = os.path.abspath("../test_formats/WAV/output_audio_NEW.wav")  # Путь сохранения аудио файла
    file = open(output_audio_filepath, "w")   # создадим файл / обновим содершимое
    file.close()

    if audio_filepath.lower().endswith('.wav'):                      # Если файл уже в формате WAV
        convert_audio_to_wav(audio_filepath, output_audio_filepath)

    elif (audio_filepath.lower().endswith('.mp4') or audio_filepath.lower().endswith('.mov')
          or audio_filepath.lower().endswith('.ts') or audio_filepath.lower().endswith('.mkv')\
          or audio_filepath.lower().endswith('.avi') or audio_filepath.lower().endswith('.wmv')):  # если формат видео
        extract_audio_from_video_with_pydub(audio_filepath, output_audio_filepath)

    else:
        convert_audio_to_wav(audio_filepath, output_audio_filepath)

    return output_audio_filepath