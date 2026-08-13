from sklearn import datasets
from sklearn.model_selection import train_test_split
import sklearn.ensemble
import pickle


# 1. Load Iris dataset
iris = datasets.load_iris()

X = iris.data
y = iris.target


# 2. Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. Create the machine learning model
model = sklearn.ensemble.RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 4. Train the model
model.fit(X_train, y_train)


# 5. Check model accuracy
accuracy = model.score(X_test, y_test)

print("Model trained successfully!")
print("Accuracy:", accuracy)


# 6. Save the trained model
with open("iris_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as iris_model.pkl")
