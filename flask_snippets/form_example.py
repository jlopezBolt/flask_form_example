from flask import Flask, render_template, session, redirect, request, url_for
from flask_bootstrap import Bootstrap
import json
# create flask app object
app = Flask(__name__)

# create a secret key. this is needed to pass data from the forms back to python
app.secret_key = 'testsecret'

# need this to do wtf.quickform
Bootstrap(app)

# import the TestForm class from forms.py found in the same directory
from forms import TestForm


@app.route('/', methods=['POST', 'GET'])
def index():
    # create a TestForm instance and store it in form
    form = TestForm()

    # render the template and pass the form to the template
    return render_template('formtest.html', form=form)


if __name__ == '__main__':
    app.run(debug = True,
        port=5000)


