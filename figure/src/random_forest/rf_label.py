from sklearn.model_selection import train_test_split, cross_val_score, KFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                           roc_curve, auc, precision_recall_curve, confusion_matrix,
                           classification_report)
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('./data/merged_V2.csv')

encoder = LabelEncoder()
encoder.fit(data['label'])

data["label"] = encoder.transform(data["label"])
# 0 = jump, 1 = spin, 2 = step

X = data.drop(['label', 'level', 'gender', 'path', 'image_filename'], axis = 1)
y = data['label']

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)

fold = KFold(n_splits=5, shuffle=False)
cv_scores = cross_val_score(model, X_train, y_train, cv=fold, scoring='accuracy')
print("\n=== Cross-validation Scores ===")
print(f"CV Accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

# 5. 최종 모델 훈련
print("\n=== Training Final Model ===")
model.fit(X_train, y_train)
print("Model training completed!")

# 6. 훈련 세트 성능 평가
y_train_pred = model.predict(X_train)
print("\n=== Training Set Performance ===")
print(classification_report(y_train, y_train_pred))

# 7. 테스트 세트 성능 평가
y_test_pred = model.predict(X_test)
y_test_pred_proba = model.predict_proba(X_test)
print("\n=== Test Set Performance ===")
print(classification_report(y_test, y_test_pred))