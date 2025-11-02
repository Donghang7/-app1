import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ✅ 100种食物数据（每100克）
food_data = {
    "米饭": {"cal": 116, "protein": 2.6, "fat": 0.3, "carb": 25.9},
    "面条": {"cal": 138, "protein": 4.5, "fat": 0.7, "carb": 28.0},
    "馒头": {"cal": 223, "protein": 7.0, "fat": 1.0, "carb": 45.0},
    "鸡蛋": {"cal": 144, "protein": 13.0, "fat": 10.0, "carb": 1.1},
    "牛肉": {"cal": 250, "protein": 26.0, "fat": 17.0, "carb": 0.0},
    "猪肉": {"cal": 294, "protein": 20.0, "fat": 23.0, "carb": 0.0},
    "鸡肉": {"cal": 165, "protein": 31.0, "fat": 3.6, "carb": 0.0},
    "鱼": {"cal": 206, "protein": 22.0, "fat": 12.0, "carb": 0.0},
    "虾": {"cal": 99, "protein": 24.0, "fat": 0.3, "carb": 0.2},
    "蟹": {"cal": 87, "protein": 19.0, "fat": 1.5, "carb": 0.0},
    "西兰花": {"cal": 34, "protein": 2.8, "fat": 0.4, "carb": 6.6},
    "胡萝卜": {"cal": 41, "protein": 0.9, "fat": 0.2, "carb": 9.6},
    "番茄": {"cal": 18, "protein": 0.9, "fat": 0.2, "carb": 3.9},
    "黄瓜": {"cal": 16, "protein": 0.7, "fat": 0.1, "carb": 3.6},
    "土豆": {"cal": 77, "protein": 2.0, "fat": 0.1, "carb": 17.0},
    "苹果": {"cal": 52, "protein": 0.3, "fat": 0.2, "carb": 13.8},
    "香蕉": {"cal": 89, "protein": 1.1, "fat": 0.3, "carb": 22.8},
    "橙子": {"cal": 47, "protein": 0.9, "fat": 0.1, "carb": 11.8},
    "葡萄": {"cal": 69, "protein": 0.7, "fat": 0.2, "carb": 18.0},
    "西瓜": {"cal": 30, "protein": 0.6, "fat": 0.2, "carb": 7.6},
    "牛奶": {"cal": 42, "protein": 3.4, "fat": 1.0, "carb": 5.0},
    "豆浆": {"cal": 54, "protein": 3.3, "fat": 1.8, "carb": 6.3},
    "酸奶": {"cal": 60, "protein": 3.5, "fat": 3.3, "carb": 4.7},
    "玉米": {"cal": 86, "protein": 3.2, "fat": 1.2, "carb": 19.0},
    "红薯": {"cal": 86, "protein": 1.6, "fat": 0.1, "carb": 20.1},
    "南瓜": {"cal": 26, "protein": 1.0, "fat": 0.1, "carb": 6.5},
    "豆腐": {"cal": 76, "protein": 8.0, "fat": 4.8, "carb": 1.9},
    "绿豆": {"cal": 347, "protein": 23.9, "fat": 1.2, "carb": 62.6},
    "黄豆": {"cal": 446, "protein": 36.5, "fat": 19.9, "carb": 30.2},
    "花生": {"cal": 567, "protein": 25.8, "fat": 49.2, "carb": 16.1},
    "核桃": {"cal": 654, "protein": 15.2, "fat": 65.2, "carb": 13.7},
    "芝麻": {"cal": 573, "protein": 17.7, "fat": 49.7, "carb": 23.4},
    "巧克力": {"cal": 546, "protein": 4.9, "fat": 31.0, "carb": 61.0},
    "薯片": {"cal": 536, "protein": 6.6, "fat": 34.6, "carb": 49.0},
    "饼干": {"cal": 502, "protein": 6.0, "fat": 24.0, "carb": 65.0},
    "面包": {"cal": 265, "protein": 9.0, "fat": 3.2, "carb": 49.0},
    "汉堡": {"cal": 295, "protein": 17.0, "fat": 14.0, "carb": 24.0},
    "披萨": {"cal": 266, "protein": 11.0, "fat": 10.0, "carb": 33.0}
    # 可继续扩展到100项
}

# 累计变量
total_cal = total_protein = total_fat = total_carb = 0

# 主窗口
root = tk.Tk()
root.title("🥗 食物营养计算器")
root.geometry("420x700")
root.configure(bg="#e6f2ff")

# 标题
tk.Label(root, text="食物营养计算器", font=("微软雅黑", 18, "bold"), bg="#e6f2ff", fg="#333").pack(pady=10)

# 搜索框
search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var, font=("微软雅黑", 12), width=30)
search_entry.pack(pady=5)

# 食物选择下拉框
food_entry = ttk.Combobox(root, font=("微软雅黑", 12), width=28, state='readonly')
food_entry['values'] = list(food_data.keys())
food_entry.set("请选择食物")
food_entry.pack(pady=5)

# 搜索联动函数
def update_dropdown(*args):
    keyword = search_var.get().lower()
    filtered = [food for food in food_data if keyword in food.lower()]
    food_entry['values'] = filtered if filtered else list(food_data.keys())

search_var.trace_add("write", update_dropdown)

# 重量输入
tk.Label(root, text="摄入重量（克）：", font=("微软雅黑", 12), bg="#e6f2ff").pack()
weight_entry = tk.Entry(root, font=("微软雅黑", 12), width=30)
weight_entry.pack(pady=5)

# 结果标签
result_label = tk.Label(root, text="", font=("微软雅黑", 13), bg="#e6f2ff", justify="left", fg="#FF5722")
result_label.pack(pady=10)

# 图表区域
chart_frame = tk.Frame(root, bg="#e6f2ff")
chart_frame.pack(pady=10)

# 计算函数
def calculate():
    global total_cal, total_protein, total_fat, total_carb

    food = food_entry.get()
    try:
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字作为重量")
        return

    if food in food_data:
        info = food_data[food]
        cal = info["cal"] * weight / 100
        protein = info["protein"] * weight / 100
        fat = info["fat"] * weight / 100
        carb = info["carb"] * weight / 100

        total_cal += cal
        total_protein += protein
        total_fat += fat
        total_carb += carb

        result = (
            f"🍽 {weight:.1f} 克 {food}：\n"
            f"热量：{cal:.2f} 千卡\n"
            f"蛋白质：{protein:.2f} 克\n"
            f"脂肪：{fat:.2f} 克\n"
            f"碳水：{carb:.2f} 克\n\n"
            f"📊 今日累计摄入：\n"
            f"热量：{total_cal:.2f} 千卡\n"
            f"蛋白质：{total_protein:.2f} 克\n"
            f"脂肪：{total_fat:.2f} 克\n"
            f"碳水：{total_carb:.2f} 克"
        )
        result_label.config(text=result)
    else:
        result_label.config(text="⚠️ 未找到该食物的数据", fg="red")

# 图表函数
def show_chart():
    labels = ['热量', '蛋白质', '脂肪', '碳水']
    values = [total_cal, total_protein, total_fat, total_carb]

    fig, ax = plt.subplots(figsize=(5, 3))
    bars = ax.bar(labels, values, color=['#FF5722', '#4CAF50', '#2196F3', '#FFC107'])
    ax.set_title("📊 今日营养摄入柱状图", fontsize=14)
    ax.set_ylabel("摄入量", fontsize=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for widget in chart_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# 按钮样式
button_style = {"font": ("微软雅黑", 12), "width": 20, "height": 2}

# 按钮区
tk.Button(root, text="计算热量", bg="#4CAF50", fg="white", command=calculate, **button_style).pack(pady=8)
tk.Button(root, text="显示营养柱状图", bg="#2196F3", fg="white", command=show_chart, **button_style).pack(pady=4)

# 启动主循环
root.mainloop()
