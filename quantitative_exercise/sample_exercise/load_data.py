import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

import seaborn as sns


path = "../data/lung_cancer_survey.csv"
data = pd.read_csv(path)


print(data.info())

print(data.sample())

print(data.isnull().sum())

data["GENDER"] = data["GENDER"].map({"F": 0, "M": 1})
data["LUNG_CANCER"] = data["LUNG_CANCER"].map({"NO": 0, "YES": 1})


corr = data.corr()
print(corr)

plt.figure(figsize=(10, 10))
plt.matshow(corr, fignum=1)
plt.xticks(range(len(corr.columns)), corr.columns, fontsize="small", rotation=90)
plt.yticks(
    range(len(corr.columns)),
    corr.columns,
)

fig = plt.gcf()
fig.savefig("figures/correlation_matrix.png")

plt.hist(data["AGE"])
plt.xlabel("Count")
plt.ylabel("Age")
plt.savefig("figures/age_distribution.png")

plt.clf()

X = data.drop("LUNG_CANCER", axis=1)
y = data["LUNG_CANCER"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


cm = confusion_matrix(y_test, y_pred)


sns.heatmap(cm, annot=True, fmt="g", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("figures/confusion_matrix.png")


plt.clf()
coefficients = pd.Series(model.coef_[0], index=X.columns)

# Sort coefficients by magnitude
coefficients = coefficients.sort_values()

# Plot coefficients
plt.figure(figsize=(10, 10))
coefficients.plot(kind="barh")

plt.title("Logistic Regression Coefficients")
plt.xlabel("Coefficient Value")
plt.savefig("figures/logistic_regression_coefficients.png")
