# 导入环境
import math
import numpy as np
from scipy.stats import norm
from scipy.stats import t
from scipy.stats import f
from scipy.stats import chi2
import matplotlib.pyplot as plt
from pylab import mpl
# 显示中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 显示负号
plt.rcParams['axes.unicode_minus'] = False

# 标准正太分布
u = 0  # 均值u
sig = math.sqrt(0.2)  # 标准差sig， 开根号
x = np.linspace(u-3*sig, u+3*sig, 50)  # 均衡的生成变量
print( 'x的值: ' , x)
y_sig = np.exp(-(x-u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
plt.plot(x, y_sig, 'b-')
plt.show()

# T分布与标准正太分布
x = np.linspace(-3, 3, 100)
print(x)
plt.plot(x, t.pdf(x, df=1), label='t.pdf(x, 1)')
plt.plot(x, t.pdf(x, df=2), label='t.pdf(x, 2)')
plt.plot(x, t.pdf(x, df=100), label='t.pdf(x, 100)')
plt.plot(x[::5], norm.pdf(x[::5]), 'kx', label='norm.pdf(x[::5])')
plt.legend()
plt.title('T分布-不同自由度的概率密度函数')
plt.show()

# F分布
lst = []
cnt = 0
for i in range(46):
    cnt = round(cnt+0.1, 2)
    lst.append(cnt)
x = lst
print('x values: ', x)
plt.plot(x, f.pdf(x, 20, 20), 'k-', label='y=f(x, 20, 20)')
plt.plot(x, f.pdf(x, 10, 10), 'b--', label='y=f(x, 10, 10)')
plt.plot(x, f.pdf(x, 10, 5), 'r-', label='y=f(x, 10, 5)')
plt.plot(x, f.pdf(x, 10, 50), 'g--', label='y=f(x, 10, 50)')
plt.plot(x, f.pdf(x, 80, 80), 'y-', label='y=f(x, 80, 80)')
plt.legend()
plt.title('F分布-不同自由度的概率密度函数')
plt.show()

# 卡方分布
x = np.linspace(0, 20, 100)
print('x values: ', x)
plt.plot(x, chi2.pdf(x, df=1), 'k-', label='df1')
plt.plot(x, chi2.pdf(x, df=2), 'b--', label='df2')
plt.plot(x, chi2.pdf(x, df=3), 'r-', label='df3')
plt.plot(x, chi2.pdf(x, df=4), 'g--', label='df4')
plt.plot(x, chi2.pdf(x, df=8), 'y-', label='df8')
plt.legend()
plt.title('卡方分布-不同自由度的概率密度函数')
plt.show()