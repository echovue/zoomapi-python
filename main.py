import requests
from flask import Flask, jsonify, request, send_file
from registrants import RegistrantClass

app = Flask(__name__)
app.config['DEBUG'] = True

zoomUrl = "http://localhost:8080"
registrants = RegistrantClass()


@app.route('/myMeeting', methods=['GET'])
def meeting():
    if 'id' in request.args:
        meetingid = str(request.args['id'])
    else:
        return "Error: No meeting id provided."

    registered = registrants.fetch_registrant(zoomUrl + "/meetings/" + meetingid + "/registrants")

    return '<h1>My Meeting</h1><h3>Registered: ' + registered + '</h3>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8000)
