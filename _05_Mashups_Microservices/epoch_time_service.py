import os
import time
from flask import Flask

app = Flask(__name__)


def epoch_time():
    return int(time.time())


@app.route('/')
def get_service():
    try:
        return str(epoch_time())
    except Exception:
        return 'There is a problem!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
