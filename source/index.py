import ctypes
import json
import os
from ctypes import wintypes
from time import sleep
from typing import Any

import keyboard
from win32gui import GetForegroundWindow, GetWindowText

settingsPath = os.path.join(os.path.dirname(__file__), "al-macro-settings.json")
defaultSettings = {
    "keybind": "\\",
    "emoteIndex": 6,
    "toggleShiftlock": False,
    "delay": 0.7,
    "mouseMoveDistance": 450,
}
emotePositions = [
    (941, 253),
    (1140, 336),
    (1219, 526),
    (1137, 722),
    (953, 791),
    (767, 716),
    (687, 537),
    (756, 345),
]

def ensureSettingsFile() -> dict[str, Any]:
    if not os.path.exists(settingsPath):
        with open(settingsPath, "w") as f:
            json.dump(defaultSettings, f, indent=4)
        return defaultSettings.copy()
    else:
        with open(settingsPath, "r") as f:
            try:
                settings = json.load(f)
                return settings
            except json.JSONDecodeError:
                print("Settings file is corrupted, resetting to default.")
                with open(settingsPath, "w") as f:
                    json.dump(defaultSettings, f, indent=4)
                return defaultSettings.copy()

def getSetting(key) -> Any:
    settings = ensureSettingsFile()
    return settings.get(key, defaultSettings.get(key))

def mouseMove(offset_x, offset_y):
    MOUSEEVENTF_MOVE = 0x0001
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, offset_x, offset_y, 0, 0)

class RECT(ctypes.Structure):
    _fields_ = [
        ('left', ctypes.c_long),
        ('top', ctypes.c_long),
        ('right', ctypes.c_long),
        ('bottom', ctypes.c_long)
    ]
    
    @property
    def width(self):
        return self.right - self.left
    
    @property
    def height(self):
        return self.bottom - self.top

def getRobloxRect() -> RECT:
    hwnd = ctypes.windll.user32.FindWindowW(None, "Roblox")
    if hwnd == 0:
        raise Exception("Roblox window not found.")
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect

def translateToRobloxCoords(x: int, y: int, resize: bool = True) -> tuple[int, int]:
    rect = getRobloxRect()
    if resize:
        x = int(x * (rect.width / 1920))  # Assuming 1920 is the base width
        y = int(y * (rect.height / 1080))  # Assuming 1080 is the base height
    return rect.left + x, rect.top + y

def mouseMoveAbs(x, y):
    MOUSEEVENTF_MOVE = 0x0001
    ctypes.windll.user32.SetCursorPos(x, y)

def mouseClick():
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def isRobloxFocused() -> bool:
    try:
        foreground_window = GetForegroundWindow()
        window_title = GetWindowText(foreground_window)
        return window_title == "Roblox"
    except Exception as e:
        print(f"Error checking Roblox focus: {e}")
        return False

def callback():
    if not isRobloxFocused():
        print("Roblox is not focused, skipping macro execution.")
        return
    keyboard.press_and_release("b")
    if getSetting("toggleShiftlock"):
        keyboard.press_and_release("ctrl")
    emotePosition = emotePositions[getSetting("emoteIndex")]
    sleep(0.5)
    mouseMoveAbs(*translateToRobloxCoords(*emotePosition, resize=True))
    sleep(0.1)
    mouseMove(0, 1)
    sleep(0.1)
    mouseClick()
    sleep(getSetting("delay"))
    mouseMove(getSetting("mouseMoveDistance"), 0)
    keyboard.press("w")
    keyboard.press("space")
    sleep(0.2)
    keyboard.release("w")
    keyboard.release("space")

def main():
    keyboard.add_hotkey(getSetting("keybind"), callback, suppress=True)
    keyboard.wait()

if __name__ == "__main__":
    main()