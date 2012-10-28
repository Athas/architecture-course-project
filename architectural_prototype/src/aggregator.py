from flask import Flask, request
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def recent_data():
    return 'Received truck data: ' + str(request.form)

if __name__ == '__main__':
    app.run()
