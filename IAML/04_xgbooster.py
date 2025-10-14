import xgboost as xgb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_openml

# Carica dataset Adult (UCI)
adult = fetch_openml("adult", version=2, as_frame=True)
df = adult.frame
df.head()

df.info()

# One-hot encoding (drop_first=True per evitare collinearità)
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop('class_>50K', axis=1)
y = df_encoded['class_>50K']  # 1 se >50K, 0 altrimenti

# Converti in tipo category
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].astype('category')

X = df.drop('class', axis=1)
y = df['class'].apply(lambda x: 1 if x == '>50K' else 0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = xgb.XGBClassifier(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    enable_categorical=True
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.3f}")

xgb.plot_importance(model, importance_type='gain', max_num_features=10)
plt.title("Top 10 Feature Importance (Gain)")
plt.show()

importances = model.feature_importances_
features = X.columns

imp_df = pd.DataFrame({'Feature': features, 'Importance': importances})
imp_df = imp_df.sort_values('Importance', ascending=False).head(15)

plt.figure(figsize=(8,6))
sns.barplot(data=imp_df, x='Importance', y='Feature')
plt.title("Feature Importance (XGBoost)")
plt.tight_layout()
plt.show()

print(model.get_booster().feature_types)
print