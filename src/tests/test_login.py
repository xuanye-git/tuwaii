import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 配置测试参数
URL = "https://h5.g123.jp/game/jya"

# 初始化 WebDriver
driver = webdriver.Chrome()

def test_login():
    driver.get(URL)
    # 定位登录按钮并点击
    login_button = driver.find_element(By.ID, "login-button-id")
    # 检查页面标题
    assert "Jya" in driver.title, "Page title mismatch!"
    login_button.click()
    # 验证是否成功登录
    assert "Welcome" in driver.page_source

    # 输入用户名和密码
    driver.find_element(By.ID, "username").send_keys("test_user")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "submit").click()

    # 验证是否跳转到主页
    time.sleep(2)
    assert "Dashboard" in driver.page_source, "Login failed!"
    print("Login test passed!")


