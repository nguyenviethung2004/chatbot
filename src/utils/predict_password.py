from gradio_client import Client

_client = Client("hung102004/Demo-SecurePass")


def predict_password_strength(password: str) -> str:
    result = _client.predict(
        password=password,
        api_name="/predict_ui"
    )
    return result["label"]
