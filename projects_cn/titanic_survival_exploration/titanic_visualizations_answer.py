%cd D:\develop\pythonproject\machine-learning-master\projects_cn\titanic_survival_exploration
import numpy as np
import pandas as pd
from titanic_visualizations import survival_stats
from IPython.display import display
#%matplotlib inline
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)
display(full_data.head())


# 从数据集中移除 'Survived' 这个特征，并将它存储在一个新的变量中。
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)
display(data.head())


def accuracy_score(truth, pred):
    if len(truth) == len(pred): 
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"
    

# Test the 'accuracy_score' function
# 测试 'accuracy_score' 函数
predictions = pd.Series(np.ones(5, dtype = int))

print accuracy_score(outcomes[:5], predictions)


# 预测全死
def predictions_0(data):
    predictions = []
    for _, passenger in data.iterrows():
        predictions.append(0)
    
    return pd.Series(predictions)

predictions = predictions_0(data)
print accuracy_score(outcomes, predictions)

#对比性别，预测死亡情况
#survival_stats(data, outcomes, 'Sex')
def predictions_1(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger.Sex == 'female':
            predictions.append(1)
        else:
            predictions.append(0)
        
    
    return pd.Series(predictions)


predictions = predictions_1(data)
print accuracy_score(outcomes, predictions)

#survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])

def predictions_2(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger.Sex == 'female':
            predictions.append(1)
        elif passenger.Age < 10:
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)

# Make the predictions
# 进行预测
predictions = predictions_2(data)
print accuracy_score(outcomes, predictions)
#survival_stats(data, outcomes, 'Age', ["Sex == 'male'", "Age < 18"])





#survival_stats(data, outcomes, 'SibSp', ["Sex == 'female'",  "Parch == 2", "Fare < 47", "Pclass == 3", "Age >= 0", "Age < 39"])
#( Age >= 10 and Age <= 60 ) 
def predictions_3(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger.Sex=='female':
            # 女性
            if passenger.SibSp == 8 or passenger.SibSp == 5 :
                predictions.append(0)
            else:
                if passenger.Fare >= 152:
                    predictions.append(1)
                elif passenger.Fare >= 151 :
                    if passenger.SibSp == 0:
                        predictions.append(1)
                    else:
                        predictions.append(0)
                elif passenger.Fare >= 47:
                    predictions.append(1)
                else:
                    if passenger.Parch==4 or passenger.Parch == 6:
                        predictions.append(0)
                    else :
                        if passenger.Pclass == 3:
                           if passenger.Age >= 60:
                               predictions.append(1)
                           elif passenger.Age >= 39:
                               predictions.append(0)
                           else :
                               if passenger.Parch == 3 or passenger.Parch == 5:
                                   predictions.append(1)
                               elif passenger.Parch == 0 :
                                   if passenger.SibSp == 3:
                                       predictions.append(1)
                                   elif passenger.SibSp == 2:
                                       predictions.append(0)
                                   else:
                                       predictions.append(1)
                               elif passenger.Parch == 1:
                                   if passenger.Embarked == "Q":
                                       predictions.append(0)
                                   elif passenger.Embarked == "C":
                                       predictions.append(1)
                                   else:
                                       if passenger.SibSp == 3: 
                                           predictions.append(0)
                                       else:
                                           predictions.append(1)
                               else :
                                   if passenger.SibSp == 0: 
                                       predictions.append(1)
                                   else :
                                       predictions.append(0)
                        else:
                           predictions.append(1) 
        else:
            # 男性
            if passenger.Age < 10:
                # 10岁以下 男性
                predictions.append(1)
            else:
                # 10岁以上 男性
                if passenger.Pclass == 2:
                    predictions.append(0)
                else:
                    # 10岁以上 非中产阶级 男性
                    if passenger.Embarked == 'C':
                        if passenger.Age > 70:
                            predictions.append(0)
                        elif passenger.Age > 60:
                            predictions.append(1)
                        else:
                            if passenger.Fare > 300:
                                predictions.append(1)
                            elif passenger.Fare > 106:
                                predictions.append(0)
                            elif passenger.Fare >= 15:
                                predictions.append(1)
                            else:
                                if passenger.Age >= 30:
                                    predictions.append(0)
                                else: 
                                    if passenger.Parch == 1:
                                        predictions.append(0)
                                    else :
                                        if passenger.Age <= 23:
                                            predictions.append(1)
                                        else:
                                            predictions.append(0)

                    else:
                        # 10岁以上 非中产阶级 非C上船 男性
                        if passenger.Age >= 70:
                            if passenger.Fare > 20 and passenger.Fare < 40:
                                predictions.append(1)
                            else:
                                predictions.append(0)
                        elif passenger.Age > 60:
                            predictions.append(0)
                        else:
                            # 10岁以上 60岁以下（含） 非中产阶级 非C上船 男性
                            if passenger.Fare > 134:
                                predictions.append(0)
                            elif passenger.Fare >= 85:
                                predictions.append(1)
                            elif passenger.Fare >= 60:
                                predictions.append(0)
                            else:
                                # 10岁以上 60岁以下（含）票价60以下 非中产阶级 非C上船 男性
                                if passenger.Parch == 0:
                                    # 10岁以上 60岁以下（含）票价60以下 非中产阶级 非C上船 无孩子 男性
                                    if passenger.Fare < 19:
                                        # 10岁以上 60岁以下（含）票价19以下 非中产阶级 非C上船 无孩子 男性
                                        if passenger.Age > 45:
                                           predictions.append(0)
                                        else:
                                            if passenger.Pclass==1:
                                                predictions.append(0)
                                            else:
                                                # 10岁以上 45岁以下（含）票价19以下 底层阶级 非C上船 无孩子 男性
                                                #if passenger.SibSp==2:
                                                    predictions.append(0)
                                                #else:
                                                    # 10岁以上 45岁以下（含）票价19以下 底层阶级 非C上船 无孩子 2个兄弟姐妹 男性
                                    elif passenger.Fare <= 47:
                                        predictions.append(1)
                                    else:
                                        if passenger.Age >=20 and passenger.Age < 50 :
                                            predictions.append(1)
                                        else :
                                            predictions.append(0)
                                else:
                                    predictions.append(0)#TODO 1人

    return pd.Series(predictions)

predictions = predictions_3(data)
print accuracy_score(outcomes, predictions)

