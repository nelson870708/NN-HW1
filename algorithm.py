import numpy as np


# a為學習率, it為iteration, lim為收斂條件
def perceptron_train(x, y, anskey, lr=0.8, it=100, es=1):
    row = len(x)
    col = len(x[0])
    w = np.random.uniform(low=-1, high=1, size=col)
    for i in range(it):
        for n in range(row):  # 先調整
            r = np.dot(w, x[n].transpose())  # X,w與講義表示方法不同，為了call library之方便
            if r < 0 and y[n] == anskey[0]:
                w = w + lr * x[n]
            elif r >= 0 and y[n] == anskey[1]:
                w = w - lr * x[n]
        correct = 0
        for n in range(row):  # 再算準確率
            r = np.dot(w, x[n].transpose())
            if (r >= 0 and y[n] == anskey[0]) or r < 0 and y[n] == anskey[1]:
                correct = correct + 1
        print('The accuracy of ' + str(i + 1) + ' epoch is ' + str(correct / row))
        if correct / row >= es:
            print('Early stop at ' + str(i + 1) + ' epoch' + '\n')
            break
    print()
    return w, correct/row


def perceptron_test(x, y, anskey, weight):
    row = len(x)
    correct = 0
    for n in range(row):
        r = np.dot(weight, x[n].transpose())  # X,w與講義表示方法不同，為了call library
        if r >= 0 and y[n] == anskey[0]:
            correct = correct + 1
        elif r < 0 and y[n] == anskey[1]:
            correct = correct + 1
    return correct / row
