from sklearn.metrics import classification_report
def print_metrics(y_true, y_pred):
report = classification_report(y_true, y_pred)
print(report)
