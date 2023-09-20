import pyautogui
from time import sleep

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

sleep(1)
pyautogui.click('Pesquisar.PNG')

sleep(1)

pyautogui.write('Enilda')

sleep(2)

pyautogui.click('Enilda.PNG')

sleep(1)

pyautogui.write('FAZ O L')

sleep(1)

# pyautogui.press('enter')




