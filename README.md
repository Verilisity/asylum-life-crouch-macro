# Crouch Wall Clip Macro

A macro for the Roblox game [Asylum Life](https://www.roblox.com/games/132352755769957) that automates the crouch wall clip bug.

## Builds

For simple usage, you can download a pre-compiled executable from the [releases page](httpss://github.com/Verilisity/asylum-life-crouch-macro/releases). This is the easiest way to get started without needing to install Python or any dependencies. Might give antivirus false positives, there is no way they are getting me to pay for a code signing certificate.

## Installation

1. Clone the repository

```bash
git clone https://github.com/Verilisity/asylum-life-crouch-macro.git
```

2. Navigate to the project directory

```bash
cd asylum-life-crouch-macro
```

3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

4. Activate the virtual environment

```bash
venv\Scripts\activate.bat
```

5. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Usage

from a terminal in the project directory, run:

```bash
venv\Scripts\python.exe index.py
```

on first run, it will drop a `al-macro-settings.json` file in the project directory. You can edit this file to change the keybind used for the macro. 

## Settings

Most settings that can be changed in the `al-macro-settings.json` will take effect immediately, except for the keybind setting. If you change the keybind, you will need to restart the macro for the change to take effect.
The settings file `al-macro-settings.json` contains the following settings:

### `keybind`

The keybind that triggers the macro, default is `\` (backslash). You can change this to any key, or use a combination of keys (e.g., `ctrl+shift+z`). This is the only setting that requires restarting the macro to take effect.

### `emoteIndex`

An index specifying which slot your crouch emote is equiped. It's a number starting at `0` representing the topmost emote slot, going up to `7` clockwise. Default is `6` representing the rightmost emote slot.

### `toggleShiftlock`

If set to `true`, the macro will toggle shiftlock before performing the crouch wall clip. This is useful if you prefer to disable shiftlock before using the macro. Default is `false`.

### `delay`

How long to wait between clicking the emote and performing the crouch wall clip. Defaults to `0.7` seconds which will work on pretty much any wall. Higher values may be more reliable but slower, lower values may work better on walls that require you to turn around before fully crouching, it'll also be faster but less reliable.

### `mouseMoveDistance`

How many pixels to move the mouse to rotate the camera. You should play around with this value to get it to work with your roblox sensitivity. Your character should turn around 180 degrees when the mouse is moved for the best results. Default is `450` which was tested on a sensitivity of `0.84`, and gets close to a 180 degree turn.