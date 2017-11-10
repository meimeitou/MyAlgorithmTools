 循环神经网络参数
=========================
---
>RNN 计算参数个数：
> $$outputsdim^2+（inputdim + 1） * outputsdim$$
>LSTM计算参数个数计算公式：
> $$4*\{(inputdim+1) * outputsdim + outputsdim^2\}$$
> LSTM 的参数个数是普通全连接RNN的四倍
```python
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
# prepare sequence
length = 5
seq = array([i/float(length) for i in range(length)])
X = seq.reshape(len(seq), 1, 1)
y = seq.reshape(len(seq), 1)
# define LSTM configuration
n_neurons = length
n_batch = length
n_epoch = 1000
# create LSTM
model = Sequential()
model.add(LSTM(n_neurons, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
print(model.summary())
# train LSTM
model.fit(X, y, epochs=n_epoch, batch_size=n_batch, verbose=2)
# evaluate
result = model.predict(X, batch_size=n_batch, verbose=0)
for value in result:
	print('%.1f' % value)
```
>运行此代码可打印网络的结构，LSTM层有140个参数，这个可以参考如下计算方式得到：
>
> `n = 4 * ((inputs + 1) * outputs + outputs^2)`
>
>`n = 4 * ((1 + 1) * 5 + 5^2)`
>
>`n = 4 * 35`
>
>`n = 140`
>
> 其中inputs为输入维长度，otput为输出维长度，timeStep时间步长仅仅表示每一次训练序列个数
---
以rnn对mnist数据集分类为例
===
[id]:../image/rnnshow.jpg 'Optional rnn'
![alt txt][id]
>将28*28的图片分解成28个长度为28的序列，28为timestep长度(图中行数)，表示一次训练输入的长度，，每一行28（图中每行的长度），表示inputdim 每次输入的序列长度，和实际网络参数个数密切相关，而timestep跟网络参数个数没有关系
