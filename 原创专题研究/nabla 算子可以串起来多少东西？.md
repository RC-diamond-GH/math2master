# nabla 算子可以串起来多少东西？

## 一、nabla 算子的定义

二维 nabla 算子的定义如下所示：
$$
\nabla=(\frac{\part }{\part x},\frac{\part }{\part y})
$$


三维 nabla 算子的定义如下所示：
$$
\nabla=(\frac{\part }{\part x},\frac{\part }{\part y},\frac{\part }{\part z})
$$
$\nabla$ 算子是一个**偏微分算子组成的向量**



## 二、多元函数微分学及几何

### 0x00 标量场的梯度

设有标量场 $f(x,y,z)$，则其梯度为：
$$
\nabla f(x,y,z)=\left(\frac{\part f}{\part x},\frac{\part f}{\part y},\frac{\part f}{\part z}\right)
$$


### 0x01 方向导数

给定方向向量 $\vec v$，那么标量场 $f(x,y,z)$ 沿该方向的方向导数为：
$$
\frac{\vec v}{|\vec v|}\cdot\nabla f(x,y,z)
$$

### 0x02 二元泰勒公式

如果使用 $P_0=(x_0,y_0)$ 来表示给定点，$\Delta P=(\Delta x,\Delta y)$ 来表示增量，那么二元泰勒公式可以写为：
$$
f(P_0+\Delta P)=\sum_{i=0}^n\frac{(\Delta P\cdot\nabla)^i f(P_0)}{i!}+\frac{(\Delta P\cdot\nabla)^{n+1}f(P_0+\theta\Delta P)}{(n+1)!},\theta\in(0,1)
$$

### 0x03 空间曲面的法向量

如果空间曲面的方程为：
$$
F(x,y,z)=0
$$
则它一点上的法向量为：
$$
\nabla\cdot F(x_0,y_0,z_0)
$$

### 0x04 空间曲线的切向量

如果空间曲面的方程为：
$$
\begin{cases}
F(x,y,z)=0\\
G(x,y,z)=0
\end{cases}
$$
则它一点上的切向量为：
$$
\nabla F(x_0,y_0,z_0)\times \nabla G(x_0,y_0,z_0)
$$

## 三、多元函数积分学

### 0x00 散度与高斯公式

向量场 $\mathbf F$ 的散度可以表示为：
$$
\nabla\cdot\mathbf F
$$
因此高斯公式可以简洁的表示为：
$$
\iint_{\part\Omega}\mathbf F\cdot\mathrm d\mathbf S=\iiint_{\Omega}\nabla\cdot\mathbf F\mathrm dV
$$

### 0x01 旋度与斯托克斯公式

向量场 $F$ 的旋度可以表示为：
$$
\nabla\times\mathbf F
$$
因此斯托克斯公式可以简洁的表示为：
$$
\int_{\part\Sigma}\mathbf F\cdot\mathrm d\mathbf r=\iint_{\Sigma}\nabla\times\mathbf F\cdot\mathrm d\mathbf S
$$


