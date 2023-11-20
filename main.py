from flask import Flask, request

import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="gke-dja-demo", location="europe-west4")

parameters = {
    "candidate_count": 1,
    "max_output_tokens": 2048,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")

app = Flask(__name__)

@app.route("/")
def hello_world():
    country = request.args.get("country")
    response = model.predict(
        """Write a travel plan for me for 3 days in {}.""".format(country),
        **parameters
    )
    resp = f"Response from Model: {response.text}"
    return resp
    return "<h2>Welcome to {}!<h2>".format(country)

if __name__ == "__main__":
    app.run(port=8080)