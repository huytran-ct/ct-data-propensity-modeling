import json
from get_model import get_model
import _pickle as pickle
import pandas as pd

_MAX_LOSSLESS = 9007199254740992

import os

from flask import Flask, request, jsonify
app = Flask(__name__)
accepted_call_model = pickle.loads(get_model("chotot_vertexai",
                                             "propensity-model/accepted-call-telesales",
                                             "accepted_call_telesales.pkl"))


@app.route("/", methods=['POST'])
def get_accepted_call_score():
    feature_name = ["no_listed_ad", "potential_region", "sum_lead", "insert_ad_recency", "order_recency"]
    try:
        request_json = request.get_json()
        calls = request_json['calls']
        behavior_user_df = pd.DataFrame(calls, columns=feature_name)
        replies = accepted_call_model.transform(behavior_user_df)[:, 1].tolist()
        return jsonify({"replies": replies})
    except Exception as inst:
        return jsonify({"errorMessage": 'something unexpected in input'}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
