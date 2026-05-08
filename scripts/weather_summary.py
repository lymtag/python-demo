# 导入 Python 内置的 json 模块，用来把 JSON 字符串转换成 Python 数据。
import json

# 从 pathlib 模块导入 Path，用更现代的方式处理文件路径。
from pathlib import Path


# __file__ 表示当前这个 Python 文件的路径。
# resolve() 会把路径转换成绝对路径。
# parents[1] 表示当前文件所在目录的上一级目录，也就是项目根目录。
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 用项目根目录拼接出 test.json 的完整路径。
WEATHER_FILE = PROJECT_ROOT / "test.json"


# 定义 main 函数，作为这个脚本的主要执行入口。
def main():
    # 读取 test.json 文件中的所有文本内容，encoding="utf-8" 用来正确读取中文。
    weather_text = WEATHER_FILE.read_text(encoding="utf-8")

    # 把 JSON 文本转换成 Python 字典 dict。
    weather = json.loads(weather_text)

    # 从字典里取出“城市”字段。
    city = weather["城市"]

    # 从字典里取出“温度”字段。
    temperature = weather["温度"]

    # 从字典里取出“天气”字段。
    condition = weather["天气"]

    # 从字典里取出“预报”字段，它是一个列表 list。
    forecast = weather["预报"]

    # 从字典里取出“湿度”字段。
    humidity = weather["湿度"]

    # 从字典里取出“风”字段，它本身也是一个字典。
    wind = weather["风"]

    # 使用 f-string 格式化字符串，打印城市、温度和天气。
    print(f"{city}: {temperature}°C, {condition}")

    # 使用 join 把 forecast 列表拼接成一个字符串，中间用逗号和空格分隔。
    print(f"未来预报: {', '.join(forecast)}")

    # 打印湿度，后面手动加上百分号。
    print(f"湿度: {humidity}%")

    # wind 是字典，所以继续用 ["方向"] 和 ["速度"] 取出里面的值。
    print(f"风向: {wind['方向']}, 风速: {wind['速度']}")


# 只有直接运行这个文件时，下面的代码才会执行。
# 如果这个文件被其他 Python 文件 import，main() 不会自动运行。
if __name__ == "__main__":
    # 调用 main 函数，开始执行脚本。
    main()
