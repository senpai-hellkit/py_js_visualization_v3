import pandas as pd
from flask import Flask, jsonify, render_template
from typing import Dict, Union, List

from settings import get_data_to_json


app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    data: pd.DataFrame = get_data_to_json()
    api_data: Dict[str, List[Union[str, int]]] = {'date': data['date'].to_list(),
                                                  'course': data['close'].to_list()}
    return jsonify(api_data)


if __name__ == '__main__':
    app.run(debug=True)
