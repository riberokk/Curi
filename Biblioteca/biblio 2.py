import pyautogui, time

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://sp.senai.br/unidade/jundiai/")
pyautogui.press("enter")
time.sleep(1.5)
cursos = pyautogui.locateOnScreen('cursos.png')
posi_cursos = pyautogui.center(cursos)
pyautogui.click(posi_cursos.x, posi_cursos.y)
