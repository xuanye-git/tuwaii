from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from src.utils.logger import logger
import time

# 设置启动选项
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 全屏启动浏览器

# 初始化 WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://h5.g123.jp/game/jya")
driver.maximize_window()


def fetchCanvas():
    try:
        logger.info("等待 iframe 加载")
        iframe = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "iframe-game"))
        )
        logger.info("iframe 加载完成")


        # 切换到 iframe
        driver.switch_to.frame(iframe)
        logger.info("切换到 iframe 成功")

        # 等待并定位 Canvas 元素
        canvas = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "GameCanvas"))
        )
        logger.info("Canvas 元素已加载: %s", canvas)

        # 获取 Canvas 信息
        canvas_rect = driver.execute_script("""
            var canvas = arguments[0];
            var rect = canvas.getBoundingClientRect();
            return {x: rect.left, y: rect.top, width: rect.width, height: rect.height};
        """, canvas)
        logger.info("Canvas 信息: %s", canvas_rect)

        time.sleep(60)

        return canvas, canvas_rect

    except TimeoutException as e:
        logger.error("超时异常: %s", e)
        return None, None


def click(canvas, xoffset, yoffset):
    try:
        # 获取 Canvas 位置信息
        canvas_rect = driver.execute_script("""
            var canvas = arguments[0];
            var rect = canvas.getBoundingClientRect();
            return {x: rect.left, y: rect.top, width: rect.width, height: rect.height};
        """, canvas)

        # 计算全局屏幕坐标中的点击位置
        click_x = canvas_rect['x'] + xoffset
        click_y = canvas_rect['y'] + yoffset

        # 执行点击动作
        logger.debug("尝试点击: 偏移 (%d, %d)", xoffset, yoffset)
        action = ActionChains(driver)
        action.move_to_element_with_offset(canvas, click_x, click_y).click().perform()

    except Exception as e:
        logger.error("点击操作失败: %s", e)



if __name__ == '__main__':
    canvas, canvas_rect = fetchCanvas()
    if canvas and canvas_rect:
        width = canvas_rect["width"]
        height = canvas_rect["height"]

        logger.info("Canvas 宽度: %s", width)
        logger.info("Canvas 高度: %s", height)

        # 点击 Canvas 的不同位置
        time.sleep(2)
        click(canvas, width / 2, height / 2)  # 中心点
        time.sleep(2)
        click(canvas, width / 2, height - 50)  # 底部中间
        time.sleep(2)
        click(canvas, width / 2, height / 2) # 正中间

        time.sleep(5)
    else:
        print("Canvas 加载失败！")

    driver.quit()
