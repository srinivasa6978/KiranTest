from flask import Flask
app = Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name
if __name__ == '__main__':
    app.run(debug=True)
# I got the env , how to push my code in the github
