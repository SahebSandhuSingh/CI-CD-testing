from model.train import train_model

def test_model_prediction():
    model = train_model()
    prediction = model.predict([[6]])
    assert round(prediction[0], 2) == 12.00
