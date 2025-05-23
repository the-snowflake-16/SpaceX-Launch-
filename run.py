import requests
import os
from datetime import datetime
import webbrowser

def find_information(launches):
    found = False
    try:
        while(found == False):
            user_input = os.environ.get('user_input_year', None)
            if user_input == None:
                user_input_year = input("Enter year of start: ")
            else:
                user_input_year = user_input
            for launch in launches:
                launch_data = launch['date_utc'][:4]
                if launch_data == user_input_year:
                    found = True
                    print(f"Найден запуск в году {user_input_year}: {launch['name']}")
                    
                    images = launch['links']['flickr']['original']
                    if images:

                        for i, img_url in enumerate(images, 1):
                            print(f"Открываю фото {i}/{len(images)}...")
                            webbrowser.open(img_url)
                            input("Нажми Enter, чтобы открыть следующее фото...")
                    else:
                        print("Фото не найдены")

                    video = launch['links']['youtube_id']
                    if video:
                        print("Открываю видео...")
                        webbrowser.open(f"https://www.youtube.com/watch?v={video}")
                    else:
                        print("Видео не найдено")

                    return

                else:
                    pass

            if not found:
                print(f"Запуск за {user_input_year} год не найден. Попробуйте ещё раз.")
    except KeyboardInterrupt:
        print("\nStopted by user.")


def main():
    url = "https://api.spacexdata.com/v4/launches"
    space = requests.get(url)
    launches = space.json()
    find_information(launches)

if __name__ == "__main__":
    main()

