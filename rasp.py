import requests
import pygame
import json

SERVER_URL = "https://math-festival-xmkrr.run.goorm.site"

while True:
    response = requests.get(f"{SERVER_URL}/get_terminal_input")
    try:
        data = response.json()
        terminal_input = data.get('terminal_input')

        if terminal_input:
            response = requests.get(f"{SERVER_URL}/get_answer?question={terminal_input}")
            try:
                answer_data = response.json()

                selected_house_options = ['az', 'hu', 're', 'sl', 'cs','gr']
                selected_house = answer_data.get('selected_house')

                if selected_house and selected_house in selected_house_options:
                    m4a_file_path = f"/home/pi/Desktop/{selected_house}.m4a" #라즈베리파이 내부 음성 파일
                    pygame.mixer.init()
                    pygame.mixer.music.load(m4a_file_path)
                    pygame.mixer.music.play()
                else:
                    print("Invalid or no house name received from the server.")
            except json.JSONDecodeError:
                print("Server didn't return valid JSON data.")
        elif response.status_code == 200:
            print("Server didn't receive terminal data.")
    except json.JSONDecodeError:
        print("Server didn't return useful JSON data.")
    except requests.RequestException as e:
        print(f"Error: {e}")

    terminal_input = None