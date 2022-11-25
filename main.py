from pathlib import Path
from gtts import gTTS


def text_to_mp3(file_path='test.txt', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.txt':
        try:
            open(file_path, "r")
        except Exception:
            print('Error opening the file')
        else:
            with open(file_path, "r") as file:
                str1 = file.readline()
                # creating an audio file
                audio = gTTS(text=str1, lang=language)
                # getting the file name
                file_name = Path(file_path).stem
                audio.save(f'{file_name}.mp3')
                print(f'{file_name}.mp3 saved successfully')
    return "File doesn't exist"


def main():
    file_path = input('Enter a file path: ')
    language = input('Choose language, for example en or ru: ')
    text_to_mp3(file_path=file_path, language=language)


if __name__ == '__main__':
    main()
