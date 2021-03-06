from flask import Flask, render_template

app = Flask(__name__, static_url_path='/src/static/',template_folder='src/templates/')

print(app.url_map)
@app.route('/')
def index():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True, port=5050)