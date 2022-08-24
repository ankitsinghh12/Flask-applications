from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_function():
    return render_template('index.html')

@app.route('/contact_us')
def contact_function():
    return render_template('contact_us.html')

@app.route('/thankyou', methods = ['POST'])
def thankyou_function():
    name = request.form['var_1']
    age = int(request.form['var_2'])
    return render_template('thankyou.html', n = name, a= age)

@app.route('/about_us')
def about_function():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)