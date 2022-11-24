import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt

# ՄՈՒՏՔԱՅԻՆ ՏՎՅԱԼՆԵՐԻ ՖԱՅԼԸ, ՈՐՏԵՂ ՏՐՎԱԾ Է X և Y ԱՌԱՆՑՔՆԵՐԻ ԿՈՐԴԻՆԱՏՆԵՐԸ
input_file = 'data_singlevar_regr.txt'

# ՏՎՅԱԼՆԵՐԻ ՆԵՐՄՈՒԾՈՒՄ ԵՐԿՉԱՓ ԶԱՆԳՎԱԾԻ ՏԵՍՔՈՎ
data = np.loadtxt(input_file, delimiter=",")
"""
[[-0.86  4.38]
 [ 2.58  6.97]
 [ 4.17  7.01]
 [ 2.6   5.44]
 .............
"""
# ԱՌԱՆՁՆԱՑՆԵՆՔ X-Ի(ՏՈՂԵՐԻ 1-ԻՆ ՏԱՐՐԵՐԸ) և Y-Ի(ՏՈՂԵՐԻ 2-ՐԴ ՏԱՐՐԵՐԸ) ԿՈՐԴԻՆԱՏՆԵՐԸ
x, y = data[:, :-1], data[:, -1]
"""
X` 
[[-0.86]
 [ 2.58]
 [ 4.17]
 [ 2.6 ]
 [ 5.13]
 [ 3.23]
 .......]
 
Y` [4.38,  6.97,  7.01,  5.44, ... ]
"""

# ԲԱԺԱՆԵՆՔ ՏՎՅԱԼՆԵՐԸ ՈՒՍՈՒՑՄԱՆ և ԹԵՍՏԱՎՈՐՄԱՆ ՄԱՍԵՐԻ
num_training = int(0.8 * len(x))  # 80%
num_test = len(x) - num_training

# ՈՒՍՈՒՑՄԱՆ ՏՎՅԱԼՆԵՐԸ
x_train, y_train = x[:num_training], y[:num_training]

# ԹԵՍՏԱՎՈՐՄԱՆ ՏՎՅԱԼՆԵՐ
x_test, y_test = x[:num_test], y[:num_test]

# ՍՏԵՂԾՈՒՄ ԵՆՔ ԳԾԱՅԻՆ ՌԵԳՐԵՍԻԱՅԻ ՄՈԴԵԼ
regressor = linear_model.LinearRegression()

# ՄՈԴԵԼԻ ՈՒՍՈՒՑՈՒՄԸ fit ՖՈՒՆԿՑԻԱՅԻ ՄԻՋՈՑՈՎ
regressor.fit(x_train, y_train)

# ԿԱՆԽԱՏԵՍՈՒՄ X-Ի ԹԵՍՏԱՅԻՆ ՏՎՅԼԱՆԵՐԻ ՀԻՄԱՆ ՎՐԱ
y_test_pred = regressor.predict(x_test)

# ԳՐԱՖԻԿԻ ԿԱՌՈՒՑՈՒՄ
plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, y_test_pred, color='red')
plt.xticks(())
plt.yticks(())
plt.show()

print(f"""<<Linear   regressor   performance>>
\tMean absolute error = {round(sm.mean_absolute_error(y_test,y_test_pred), 2)}")
\tMean squared error = {round(sm.mean_squared_error(y_test, y_test_pred), 2)}")
\tMedian absolute error = {round(sm.median_absolute_error(y_test, y_test_pred), 2)}")
\tExplain variance score = {round(sm.explained_variance_score(y_test, y_test_pred), 2)})
\tR2 score = {round(sm.r2_score(y_test, y_test_pred), 2)})""")
