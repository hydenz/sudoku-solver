from selenium import webdriver
from time import sleep
import pyautogui

driver = webdriver.Firefox()
driver.get("https://www.geniol.com.br/logica/sudoku/")
driver.execute_script("window.scrollTo(0, 500)")
sleep(1)
driver.find_element_by_xpath("//a[@data-level='veryhard']").click()
sleep(1)
pyautogui.press("enter")
valor = [[], [], [], [], [], [], [], [], []]
sleep(2)
c = 0
for lista in valor:
    for j in range(9):
        num = driver.find_element_by_xpath(f"//td[@id='c{c}']").text
        lista.append(int(num)) if num != '' else lista.append(None)
        c += 1
sleep(1)
print("Valores do Sudoku:\n", valor)
sec_driver = webdriver.Firefox()
sec_driver.get("https://www.sudoku-solutions.com/")
sleep(1)
sec_driver.find_element_by_xpath("//div[@id='EVENT_CLEAR']").click()
sleep(3)
sec_driver.find_element_by_xpath("//div[@id='C1']").click()
for i in valor:
    for j in range(9):
        pyautogui.press(
            f"{i[j]}") if i[j] is not None else pyautogui.press('right')

sleep(3)
sec_driver.find_element_by_xpath("//div[@id='EVENT_SOLVE']").click()
sleep(3)
sec_driver.find_element_by_xpath(
    "//button[@class='ui-button ui-corner-all ui-widget']").click()
valor_sol = valor.copy()
c = 1
for lista in valor_sol:
    for j in range(9):
        if lista[j] is None:
            lista[j] = int(sec_driver.find_element_by_xpath(
                f"//div[@id = 'C{c}_INPUT_CONTAINER']").text)
        else:
            lista[j] = None
        c += 1
c = 0
for lista in valor_sol:
    for j in range(9):
        if lista[j] is not None:
            driver.find_element_by_xpath(f"//td[@id='c{c}']").click()
            driver.find_element_by_xpath(
                f"//td[@data-value='{lista[j]}']").click()
        else:
            c += 1
            continue
        c += 1
print("Valores faltantes:\n", valor_sol)
