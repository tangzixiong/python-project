# iris结构化数据建模

## 导入需要的库
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC                             #支持向量分类
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier        #多层感知机
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report       #metrics 度量  检验机器学习模型效果的定量指标模块
from sklearn.datasets import load_iris
import argparse                                         #命令项选项与参数解析模块


## 设置参数
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, default="knn", help="type of python machine learning model to use")
args = vars(ap.parse_args())

## 定义一个保存模型的字典，根据 key 来选择加载哪个模型
models = {
    "knn": KNeighborsClassifier(n_neighbors=1),
    "naive_bayes": GaussianNB(),
    "logit": LogisticRegression(solver="lbfgs", multi_class="auto"),        # 求解器的选择，由参数"solver"控制，共有五种选择，libliner: 坐标下降法，二分类  lbfgs: 拟牛顿法的一种,  newton-cg: 牛顿法-共轭梯度法,   sag: 随机平均梯度下降,  saga
    "svm": SVC(kernel="rbf", gamma="auto"),               #常用核函数， 线性核函数kernel='linear'，多项式核函数kernel='poly'，径向基核函数kernel='rbf'，sigmod核函数kernel='sigmod'       高斯核中的gamma
    "decision_tree": DecisionTreeClassifier(),
    "random_forest": RandomForestClassifier(n_estimators=100),
    "mlp": MLPClassifier()
}


##载入数据
print("加载数据中...")
dataset = load_iris()
#scikit-learn中的数据通常用大写的x表示， 标签用小写的y表示
trainX, testX, trainY, testY = train_test_split(dataset.data, dataset.target,
                                                 random_state=3, test_size=0.2)


## 训练模型
print("应用 '{}' 模型建模...".format(args["model"]))
model = models[args["model"]]
model.fit(trainX, trainY)
## 预测并输出一份分类结果报告
print("评估模型效果...")
predictions = model.predict(testX)
print(classification_report(testY, predictions, target_names=dataset.target_names))
