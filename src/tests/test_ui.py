import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


def test_game_start():
    driver = webdriver.Chrome()
    driver.get("https://g123.jp/game/jya")

    # 点击“开始游戏”按钮
    play_button = driver.find_element(By.ID, "play-button")
    play_button.click()

    # 验证游戏启动成功
    time.sleep(5)  # 等待游戏加载
    assert "Game Started" in driver.page_source, "Game did not start!"
    print("Game start test passed!")

    driver.quit()