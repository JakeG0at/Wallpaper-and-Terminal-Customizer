#!/usr/bin/env python3

import os
import random
import requests
import shutil
from bs4 import BeautifulSoup
from datetime import date, timedelta
import subprocess

# Set the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the download path
vault = os.path.join(BASE_DIR, 'vault')
favorites_dir = os.path.join(BASE_DIR, 'favorites')
favorite_themes_dir = os.path.join(BASE_DIR, 'favorite_themes')

def setup_directories():
    for directory in [vault, favorites_dir, favorite_themes_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

def download_wallpaper():
    while True:
        # Get the current date
        today = date.today().isoformat()

        # Check if an image has already been downloaded for today
        filename = today + '.jpg'
        download_path = os.path.join(vault, filename)
        if os.path.exists(download_path):
            print(f'An image has already been downloaded for today ({today}). Overwriting it.')

        # Download a random image from the website and save it to the directory
        url = 'https://deepdreamgenerator.com/best/today'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_elements = soup.find_all('img', class_='light-gallery-item')
        chosen_image = random.choice(image_elements)
        image_url = chosen_image['data-src']
        response = requests.get(image_url)
        with open(download_path, 'wb') as f:
            f.write(response.content)

        # Set the downloaded image as the terminal theme and wallpaper
        change_terminal_theme(download_path)

        # Prompt user to save the downloaded image to favorites, save the terminal theme, see another background, or none
        while True:
            print("\n" + "="*40)
            print("  SAVE OPTIONS")
            print("="*40 + "\n")

            print(" (w) Save to wallpaper favorites        (⌒▽⌒)\n")
            print(" (t) Save to theme favorites            (•̀ᴗ•́)و\n")
            print(" (s) See another background             (≧◡≦)\n")
            print(" (n) None                               (￣ω￣)\n")
            
            save_option = input("Enter your choice (w/t/s/n): ")
            if save_option.lower() == 'w':
                save_to_favorites(download_path, filename, favorites_dir)
                return
            elif save_option.lower() == 't':
                save_to_favorites(download_path, filename, favorite_themes_dir)
                return
            elif save_option.lower() == 's':
                break
            elif save_option.lower() == 'n':
                return
            else:
                print('Invalid input. Please enter "w", "t", "s", or "n".')
        if save_option.lower() != 's':
            break

def save_to_favorites(download_path, filename, destination_dir):
    destination_path = os.path.join(destination_dir, filename)
    if os.path.exists(destination_path):
        print(f'The image "{filename}" already exists in the destination directory.')
    else:
        shutil.copy(download_path, destination_path)
        print(f'The image "{filename}" has been saved to the destination directory.')
def change_terminal_theme(image_path):
    # Set the image as the terminal theme
    subprocess.run(['wal', '-i', image_path])

def change_terminal_colors(image_path):
    # Set the terminal colors without changing the background
    subprocess.run(['wal', '-n', '-i', image_path])

def print_menu():
    print("\n" + "="*40)
    print("  WALLPAPER & TERMINAL THEME CHANGER")
    print("="*40 + "\n")

    print("1. Download a new wallpaper and change the terminal theme   (^_^)\n")
    print("2. Change the terminal theme to the daily image             (o_o)\n")
    print("3. Change the terminal theme to a random image in favorites (¬‿¬)\n")
    print("4. Change the wallpaper to a random favorite wallpaper      (╹◡╹)\n")

def main():
    while True:
        print_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Download a new wallpaper and change the terminal theme
            download_wallpaper()
            latest_image = sorted(os.listdir(vault))[-1]
            image_path = os.path.join(vault, latest_image)
            change_terminal_theme(image_path)
            break

        elif choice == '2':
            # Change the terminal theme to the daily image
            latest_image = sorted(os.listdir(vault))[-1]
            image_path = os.path.join(vault, latest_image)
            change_terminal_theme(image_path)
            break

        elif choice== '3':
            # Change the terminal colors to a random image in favorites
            favorites = os.listdir(favorite_themes_dir)
            if not favorites:
                print('No images in favorites.')
                continue
            random_image = random.choice(favorites)
            image_path = os.path.join(favorite_themes_dir, random_image)
            change_terminal_colors(image_path)
            break

        elif choice == '4':
            # Change the wallpaper to a random image in favorites
            favorites = os.listdir(favorites_dir)

            if not favorites:
                print('No images in favorites.')
                continue
            random_image = random.choice(favorites)
            image_path = os.path.join(favorites_dir, random_image)
            change_terminal_theme(image_path)  # Replace 'feh' with the change_terminal_theme function
            break

        else:
            print('Invalid input. Please enter a number from 1 to 4.')

if __name__ == '__main__':
    main()
