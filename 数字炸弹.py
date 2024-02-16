import random
from tkinter import *
from tkinter import ttk
import sys
import pickle
from tkinter import messagebox
import json

window = Tk()
window.title("登录")

window.geometry('400x100')

l1 = ttk.Label(window,text="用户:")
e1 = ttk.Entry(window)

l2 = ttk.Label(window,text="密码:")
e2 = ttk.Entry(window,show="*")

l1.grid(row=0,column=0,padx=15)
e1.grid(row=0,column=1)

l2.grid(row=1,column=0,padx=15)
e2.grid(row=1,column=1)


def usr_log_in():
    # 输入框获取用户名密码
    usr_name = e1.get()
    usr_pwd = e2.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(title='welcome',
                                   message='欢迎您：' + usr_name)
            window.destroy()

            class NumberBombGame:
                def __init__(self, master):
                    self.master = master
                    self.master.title("数字炸弹游戏")

                    # 游戏参数
                    self.min_value = 1
                    self.max_value = 100
                    self.bomb = None
                    self.attempts = 0

                    # 排行榜数据结构
                    self.leaderboard = self.load_leaderboard()

                    # 创建游戏界面
                    self.create_widgets()

                def create_widgets(self):
                    # 标签和输入框
                    Label(self.master, text="猜一个数字（1-100）:").grid(row=0, column=0, sticky="e")
                    self.guess_entry = Entry(self.master)
                    self.guess_entry.grid(row=0, column=1, padx=5, pady=5)

                    # 开始游戏按钮
                    self.start_button = Button(self.master, text="开始游戏", command=self.start_game)
                    self.start_button.grid(row=1, column=0, padx=5, pady=5)

                    # 提交按钮
                    self.submit_button = Button(self.master, text="提交", command=self.check_guess)
                    self.submit_button.grid(row=1, column=1, padx=5, pady=5)

                    # 排行榜显示区域
                    self.leaderboard_label = Label(self.master, text="排行榜：")
                    self.leaderboard_label.grid(row=2, column=0, sticky="w")
                    self.leaderboard_listbox = Listbox(self.master, height=5, width=30)
                    self.leaderboard_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
                    self.update_leaderboard_display()

                def start_game(self):
                    # 重置游戏
                    self.attempts = 0
                    self.bomb = self.min_value + random.randint(0, self.max_value - self.min_value)
                    self.start_button.config(state="disabled")
                    self.submit_button.config(state="normal")
                    self.guess_entry.delete(0, END)
                    self.guess_entry.focus()

                def check_guess(self):
                    try:
                        guess = int(self.guess_entry.get())
                        self.attempts += 1




                        if guess < self.min_value or guess > self.max_value:
                            messagebox.showerror("错误", "数字必须在1到100之间。")
                        elif guess < self.bomb:
                            messagebox.showinfo("提示", "太低了，请再试一次。")
                        elif guess > self.bomb:
                            messagebox.showinfo("提示", "太高了，请再试一次。")
                        else:
                            # 猜到了炸弹数字
                            messagebox.showinfo("恭喜", f"你踩到了炸弹！你用了{self.attempts}次。")
                            self.add_to_leaderboard(self.attempts)
                            self.start_button.config(state="normal")
                            self.submit_button.config(state="disabled")
                    except ValueError:
                        messagebox.showerror("错误", "请输入一个有效的整数。")

                def add_to_leaderboard(self, attempts):
                    # 添加到排行榜
                    self.leaderboard.append((attempts,))
                    self.leaderboard.sort(key=lambda x: x[0])  # 按次数排序
                    self.update_leaderboard_display()
                    self.save_leaderboard()

                def update_leaderboard_display(self):
                    # 更新排行榜显示
                    self.leaderboard_listbox.delete(0, END)
                    for entry in self.leaderboard:
                        self.leaderboard_listbox.insert(END, f"{entry[0]}次")

                def load_leaderboard(self):
                    # 从文件加载排行榜数据
                    try:
                        with open("leaderboard.json", "r") as file:
                            return json.load(file)
                    except FileNotFoundError:
                        return []

                def save_leaderboard(self):
                    # 保存排行榜数据到文件
                    with open("leaderboard.json", "w") as file:
                        json.dump(self.leaderboard, file)

            # 创建Tkinter窗口
            root = Tk()
            game = NumberBombGame(root)

            # 运行游戏循环
            root.mainloop()

        else:
            messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
        if is_signup:
            enroll()
def end():
    sys.exit()

def enroll():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()
    window_sign_up = Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = StringVar()
    Label(window_sign_up, text='用户名：').place(x=10, y=10)
    Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = StringVar()
    Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = StringVar()
    Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = Button(window_sign_up, text='确认注册',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)

b1 = ttk.Button(window,text="登录",command=usr_log_in)
b2 = ttk.Button(window,text="退出",command=end)
b3 = ttk.Button(window, text='注册',command=enroll)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

window.mainloop()
