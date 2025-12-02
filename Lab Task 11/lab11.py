import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import warnings

fp = 'ObesityDataSet.csv'
dt = pd.read_csv(fp)

# Data Cleaning
num_c = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'SCC', 'SMOKE', 'CH2O', 'FAF', 'TUE']
for c in num_c:
    if c in dt.columns:
        dt[c] = dt[c].fillna(dt[c].median())
if 'CALC' in dt.columns:
    dt['CALC'] = dt['CALC'].fillna(dt['CALC'].mode()[0])

X = dt.drop('NObeyesdad', axis=1)
Y = dt['NObeyesdad']
for c in X.select_dtypes(['object']).columns:
    X[c], _ = pd.factorize(X[c])
Y_e, uc = pd.factorize(Y)
Y_e = pd.Series(Y_e)

# 1. Splitting Data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y_e, test_size=0.3, shuffle=True, random_state=42
)

print('X_train shape:', X_train.shape)

# 2. Applying Different Classifiers
cls = {
    'Bernoulli': BernoulliNB(),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gaussian': GaussianNB(),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Multinomial': MultinomialNB(),
    'KNeighbors': KNeighborsClassifier()
}

scr = []
print('\nClassifier Scores:')

for name, clf in cls.items():
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    
    lbl = np.unique(Y_pred)
    
    acc = metrics.accuracy_score(Y_test, Y_pred)
    prc = metrics.precision_score(Y_test, Y_pred, average='weighted', labels=lbl)
    rcl = metrics.recall_score(Y_test, Y_pred, average='weighted', labels=lbl)
    f1 = metrics.f1_score(Y_test, Y_pred, average='weighted', labels=lbl)
    
    scr.append({
        'Classifier': name,
        'Accuracy': acc,
        'Precision': prc,
        'Recall': rcl,
        'F1 Score': f1
    })
    
    print(f'{name} Accuracy: {acc:.4f}')

res_dt = pd.DataFrame(scr)
print('\nSummary of All Classifiers:')
print(res_dt)

# 3. Plotting Bar Graph
met_l = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
cls_l = res_dt['Classifier'].tolist()
x = np.arange(len(cls_l))
w = 0.2

fig, ax = plt.subplots(figsize=(14, 8))

for i, metric in enumerate(met_l):
    offset = w * (i - 1.5)
    ax.bar(x + offset, res_dt[metric], w, label=metric)

ax.set_ylabel('Score')
ax.set_title('Performance Scores of Applied Classifiers')
ax.set_xticks(x)
ax.set_xticklabels(cls_l, rotation=45, ha="right")
ax.legend(loc='lower right')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 1.05)
plt.tight_layout()
plt.show()
