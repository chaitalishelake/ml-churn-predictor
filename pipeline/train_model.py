from sklearn.linear_model import LogisticRegression
import joblib
def run_training(X, y):
clf = LogisticRegression()
clf.fit(X, y
joblib.dump(clf, "models/churn_model.joblib")
return clf
