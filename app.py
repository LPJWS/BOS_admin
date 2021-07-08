from flask import Flask, render_template, request
import json
import wifi_change


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/w_change_pass', methods=['POST'])
def w_change_pass():
    # return json.dumps({'status': 'ok', 'response': {'password': 'Sanya_hui_sosi'}})
    if request.method == 'POST':
        return json.dumps({'status': 'ok', 'response': {'password': wifi_change.change_pass()}})
    else:
        return json.dumps({'status': 'error', 'error': 'Bad method'})


@app.route('/w_get_pass', methods=['GET'])
def w_get_pass():
    if request.method == 'GET':
        return json.dumps({'status': 'ok', 'response': {'password': wifi_change.get_pass()}})
    else:
        return json.dumps({'status': 'error', 'error': 'Bad method'})


if __name__ == '__main__':
    app.run(debug=True)
