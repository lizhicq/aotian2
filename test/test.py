import os
import time
import platform
from PIL import ImageGrab
from pathlib import Path


def take_screenshot(output_dir, interval=5):
    """
    持续截图的函数
    :param output_dir: 保存截图的目录
    :param interval: 截图间隔时间（秒）
    """
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 计数器，用于命名文件
    screenshot_count = 0
    
    try:
        while True:
            # 获取当前系统时间作为文件名的一部分
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            
            # 截图
            screenshot = ImageGrab.grab()
            
            # 生成文件名
            filename = os.path.join(output_dir, f"screenshot_{timestamp}_{screenshot_count}.png")
            
            # 保存截图
            screenshot.save(filename)
            
            print(f"截图已保存：{filename}")
            
            # 增加计数器
            screenshot_count += 1
            
            # 等待指定时间
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("截图程序已停止")

def main():
    # 选择保存目录
    # output_dir = os.path.join(os.path.expanduser("~"), "Screenshots")
    base_dir = Path(__file__).resolve().parent.parent
    # 截图间隔（秒）
    interval = 5
    
    output_dir = f"{base_dir}/screenshots/"
    
    print(f"系统平台：{platform.system()}")
    print(f"截图将保存在：{output_dir}")
    print(f"截图间隔：{interval}秒")
    
    # 开始截图
    take_screenshot(output_dir, interval)

if __name__ == "__main__":
    main()