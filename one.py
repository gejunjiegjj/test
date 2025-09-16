
import datetime
import time
from zoneinfo import ZoneInfo  # Python 3.9+

def display_time(timezone="Asia/Shanghai"):
    """显示带有时区的时间信息"""
    tz = ZoneInfo(timezone)
    while True:
        now = datetime.datetime.now(tz)
        print("\033c", end="")  # 清屏（适用于Windows/cmd）
        print(f"1. 标准格式: {now.isoformat()}")
        print(f"2. 中文格式: {now.strftime('%Y年%m月%d日 %H时%M分%S秒')}")
        print(f"3. 12小时制: {now.strftime('%I:%M:%S %p')}")
        print(f"4. 时区: {now.tzname()}")
        print("5. 退出")
        choice = input("选择显示模式 (1-5): ")
        
        if choice == "5":
            break
            time.sleep(1)

if __name__ == "__main__":
    try:
        display_time()
    except ImportError:
        print("需要Python 3.9+支持zoneinfo，请使用：")

        print("pip install tzdata")