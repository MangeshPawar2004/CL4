import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# 1. Load dataset
# -----------------------------
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

print("Dataset loaded successfully")
print("Features:", iris.feature_names)
print("Target classes:", class_names)

# -----------------------------
# 2. Split into train and test
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 3. Create and train classifier
# -----------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 4. Predict on test data
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 5. Evaluate model
# -----------------------------
acc = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(acc * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# -----------------------------
# 6. Visualize confusion matrix
# -----------------------------
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# -----------------------------
# 7. Predict new sample
# -----------------------------
new_sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_sample)
print("\nNew sample prediction:", class_names[prediction[0]])