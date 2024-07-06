from flask import Flask, render_template, request
from download import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = int(request.form['start'])
        count = int(request.form['count'])
        urls = main(count=count,start=start)
        return render_template('index.html',urls=urls)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
