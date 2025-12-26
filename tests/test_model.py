from model.train import train_model

def test_model_prediction():
    model = train_model()
    prediction = model.predict([[5]])
    assert prediction[0] == 10
