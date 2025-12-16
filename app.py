from flask import Flask
from src.routes.upload_routes import upload_bp
from src.routes.chat_routes import chat_bp
from src.routes.auth_routes import auth_bp
from dotenv import load_dotenv
from flask_cors import CORS
import os
from src.utils.jwt_manager import init_jwt
from src.utils.redis_listener import start_redis_watcher_thread

load_dotenv()
app = Flask(__name__)

CORS(app)

app.config['JWT_SECRET_KEY'] = os.getenv('FLASK_JWT_SECRET_KEY')
init_jwt(app)

app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(chat_bp)
start_redis_watcher_thread()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
