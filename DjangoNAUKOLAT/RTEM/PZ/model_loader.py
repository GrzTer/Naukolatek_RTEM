from tf_keras.models import load_model


def get_model():
    model_path = "PZ/model_checkpoint.h5"
    model = load_model(model_path)
    return model
