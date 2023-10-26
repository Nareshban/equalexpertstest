from flask import Flask
import requests

app = Flask(__name__)

# @app.route('/usergist/<user>')
@app.route('/')
def getuserpubgist():
    # set the API endpoint URL
    url = "https://api.github.com/users/{username}/gists"

    # set the username
    user = 'nareshban'

    # make the request
    response = requests.get(url.format(username=user))

    # print the description of each public gist
    for gist in response.json():
        if not gist["public"]:
            continue
        return (gist["description"])

if __name__ == '__main__':
   app.run()