from model.train import train_model

def test_model_prediction():
    model = train_model()
    prediction = model.predict([[5]])
    assert round(prediction[0], 2) == 10
