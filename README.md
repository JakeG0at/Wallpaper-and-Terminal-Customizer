# Wallpaper & Terminal Theme Changer

## Overview

This script is a Wallpaper and Terminal Theme Changer written in Python. It downloads random images from [Deep Dream Generator](https://deepdreamgenerator.com/best/today), sets them as your terminal theme and wallpaper, and also provides options to save them to your favorites. The color scheme of the terminal is changed with the help of [PyWal](https://github.com/dylanaraps/pywal), a tool created by Dylan Araps.

## Features

* **Download wallpapers**: Downloads a random image from Deep Dream Generator and sets it as your terminal theme and wallpaper using PyWal.
* **Save to favorites**: Allows you to save the downloaded image to your favorites for later use. You can save it either as a favorite wallpaper or a favorite theme.
* **See another background**: If you do not like the downloaded image, you can choose to download a different one.
* **Change terminal theme**: You can change the terminal theme to the daily image or to a random image from your favorites using PyWal.
* **Change wallpaper**: You can change your wallpaper to a random image from your favorites.

## Prerequisites

This script requires Python 3, as well as the following Python libraries:

* `os`
* `random`
* `requests`
* `shutil`
* `BeautifulSoup` from `bs4`
* `date`, `timedelta` from `datetime`
* `subprocess`

You also need to have [PyWal](https://github.com/dylanaraps/pywal) installed.

Please ensure that all of these are installed before running the script.

## Running the script

To run the script, navigate to the directory containing the script and type `python3 script_name.py` in the terminal, replacing `script_name.py` with the name of the script.

You will be prompted with a menu of options:

```
  WALLPAPER & TERMINAL THEME CHANGER

1. Download a new wallpaper and change the terminal theme   (^_^)
2. Change the terminal theme to the daily image             (o_o)
3. Change the terminal theme to a random image in favorites (¬‿¬)
4. Change the wallpaper to a random favorite wallpaper      (╹◡╹)
```

Enter the number corresponding to your choice and press `Enter`.

## Customization

The script has several variables at the top that you can customize to suit your needs:

* `vault` is the directory where the script saves the downloaded images.
* `favorites_dir` is the directory where the script saves your favorite wallpapers.
* `favorite_themes_dir` is the directory where the script saves your favorite terminal themes.

To change these, simply replace the paths with the paths to your desired directories.

## PyWal

This script uses PyWal, a tool that generates a color palette from the dominant colors in an image. It then applies the colors system-wide and on-the-fly in all of your favorite programs. PyWal was created by Dylan Araps, and you can find it on [GitHub](https://github.com/dylanaraps/pywal). We use PyWal to set the downloaded image as the terminal theme.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. All contributions are welcome!

## License

This project is open source, under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Credits

We thank Dylan Araps for creating PyWal, which this script uses to change terminal themes. PyWal is an amazing tool, and all credit for it goes to Dylan. You can check out PyWal [here](https://github.com/dylanaraps/pywal).

