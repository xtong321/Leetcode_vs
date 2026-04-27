import pandas as pd
import matplotlib.pyplot as plt

# 第一步读取数据: 使用read_csv()函数读取csv文件中的数据
df = pd.read_csv(r"D:\study\python\data\percent-bachelors-degrees-women-usa.csv")
# 第二步利用pandas的plot方法绘制折线图
df.plot(x = "Year", y = "Agriculture")
# 第三步: 通过plt的show()方法展示所绘制图形
plt.show()