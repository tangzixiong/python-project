
## 导入工具库
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import load_iris

## 载入 Iris 数据集，然后进行训练集和测试集的划分，80%数据作为训练集，其余20%作为测试集
print("加载数据中...")
dataset = load_iris()
(trainX, testX, trainY, testY) = train_test_split(dataset.data,
                                                  dataset.target, test_size=0.2)

## 将标签进行one-hot向量编码
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)


##搭建网络模型的结构和训练、预测代码

## 利用 Keras 定义网络模型
model = Sequential()
model.add(Dense(3, input_shape=(4,), activation="sigmoid"))
model.add(Dense(3, activation="sigmoid"))
model.add(Dense(3, activation="softmax"))


## 采用梯度下降训练模型
print('训练网络中...')
opt = SGD(lr=0.1, momentum=0.9, decay=0.1 / 250)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=["accuracy"])
H = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=250, batch_size=16)


## 预测
print('评估模型效果')
predictions = model.predict(testX, batch_size=16)
print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1), target_names=dataset.target_names))