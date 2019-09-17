import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, \
    precision_score, recall_score


y_true = [0, 1, 0, 1, 1]
# y_pred = np.ones_like(y_true)
y_pred = np.zeros_like(y_true)

# print(confusion_matrix(y_true, y_pred))
print(confusion_matrix(y_pred, y_true))
