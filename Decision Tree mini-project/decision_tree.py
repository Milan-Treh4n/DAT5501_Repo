from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# fetch dataset
car_evaluation = fetch_ucirepo(id=19)

# data (as pandas dataframes) 
X = car_evaluation.data.features 
y = car_evaluation.data.targets 
  
# metadata 
print(car_evaluation.metadata) 
  
# variable information 
print(car_evaluation.variables) 

# first five rows of feature data
print(X.head())

# Encode Categorical Data

print("\nEncoding categorical variables...")

label_encoder = LabelEncoder()

# Encode each column in X (they are all categorical)
X_encoded = X.apply(label_encoder.fit_transform)

# Encode target labels
y_encoded = label_encoder.fit_transform(y.values.ravel())

print("Encoding complete.")

# Split Data Into Training and Testing Sets

print("\nSplitting data into training and testing sets...")

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y_encoded,
    test_size=0.30,
    random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Train the Decision Tree Classifier

print("\nTraining the Decision Tree model...")

model = DecisionTreeClassifier(
    criterion="entropy",   # use information gain
    random_state=42
)

model.fit(X_train, y_train)

print("Model training complete.")

# Make Predictions

print("\nGenerating predictions...")

y_pred = model.predict(X_test)

print("Predictions complete.")

# Evaluate Model Performance

print("\nModel Evaluation:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["unacc", "acc", "good", "vgood"]
))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

