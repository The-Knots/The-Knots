import os
import geocoder
import requests
from werkzeug.utils import redirect, validate_arguments
from pipeline import process
from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'
app.secret_key = "super secret key"

def validate_file(name):
    return name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png')

@app.route('/', methods = ['GET'])
def dashboard():
    resp = geocoder.ip('me')
    state = resp.state
    country = resp.country
    weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={state}&appid=02b5ad2898ca71d51c4a7c03a4381186').json()
    return render_template('dashboard.html', weather = weather, state = state, country = country)

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about_us.html')

@app.route('/speed', methods = ['GET','POST'])
def speed_pred():
    if request.method == 'POST':
        f = request.files['file']
        
        if f.filename == '':
            flash('Please upload a file!')
            return redirect(url_for('speed_pred'))

        elif not validate_file(f.filename):
            flash('Please upload an image file!')
            return redirect(url_for('speed_pred'))

        else:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(file_path)
            
            result = process(file_path)
            category = ''

            if result < 33:
                category = 'Tropical Depression'
            elif result >= 33 and result < 64:
                category = 'Tropical Storm'
            elif result >= 64 and result < 82:
                category = 'Category 1 Hurricane'
            elif result >= 82 and result < 95:
                category = 'Category 2 Hurricane'
            elif result >= 95 and result < 112:
                category = 'Category 3 Hurricane'
            elif result >= 112 and result < 136:
                category = 'Category 4 Hurricane'
            else:
                category = 'Category 5 Hurricane'
            
            data = {
                'speed' : round(result,2),
                'name' : 'uploads/' + f.filename,
                'type' : category
            }
            return render_template('results.html', data = data)
    return render_template('speed.html')

if __name__ == '__main__':
    app.run(debug = True)