from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<center><font size="6">loves contributing to ScoreLab.</font></center>'


app.run(debug=True, host='0.0.0.0', port=8080)
