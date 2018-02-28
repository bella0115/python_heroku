from flask import Flask, render_template, request


app = Flask('MyApp')

@app.route('/')
def hello():
    return "Hello world second version"

if __name__ == "__main__":
    app.run(debug=True)
