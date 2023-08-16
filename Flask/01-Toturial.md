
-------------------auto loader----------------debugger--------------------------------------

flask --app main.py --debug run


-----------------dunder-------------------------------------------------------------










--------------------Flask Define simple view-------------------------------------------
from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    name = 'Ara'
    return '<h1>your name is {}</h1>'


@app.route('/about')
def about():
    return 'This is about page'

------------------------------------------------------------------------------

@app.route('/')
def index():
    name = 'Araz'
    return f"Your name is {name}"
    

---------------------------routes---and use values in url------------------------------------------

from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
           return "<h1>Index</h1>"

@app.route('/about')
def about():
    return "This is about page."

@app.route('/hello/<string:name>')
# <string:name>
# <int:name>
# <float:name>
# <path:name>
def hello_name(name):
    return f"Hello {name}"



--------------------------templates-----01------------------------------------------------------

from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>My Flask App</title>
        </head>
        </body>
            <h1>Hello World</h1>
        </body>
    </html>
    """

-----------------------------------------template engine (jinja)---------------------------------

# creat at root path <templates> folder
# create an index.html file 

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


--------------- template_folder='your folder'-----------------
if you want change templates folder name

app = Flask(__name__, template_folder='themes')

--------------------------------------------------------------

01----------------Heads or Tails-------------------------------

import random
from flask import Flask, render_template

app = Flask(__name__) #template_folder='templates'

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result/')
def result():
    heads_or_tails = random.randint(1, 2)
    if heads_or_tails == 1:
        result_text = 'Heads'
    else:
        result_text = 'Tails'

    return render_template('result.html', result_text=result_text)



01-------------------------------index.html---------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Heads or Tails - Homepage App</title>
</head>
<body>

    <a href="{{url_for('result')}}">Heads or Tails</a>

</body>
</html>

01-------------------------------result.html--------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Heads or Tails - Result</title>
</head>
<body>
    Result page : {{ result_text }}
    <br>
    <a href="{{ url_for('result')}}">Heads or Tails</a>

</body>
</html>


------------------------------------------------------------------------------
------------------------------------------------------------------------------

02------------------Loops in templates-----------------------------------------


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    students = ['Araz', 'Arezou', 'Rosa']
    numbers = [i for i in range(20)]
    return render_template('index.html', students=students, numbers=numbers)


02-------------------index.html-----------------------------------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Loops in Templates</title>
</head>
<body>
    <h1>Loops in Templates</h1>
    <br>
    <br>
    {{ students }}
    <br><br>
    <ul>
    {% for student in students %}
        <li>{{ student }}</li>
    {% endfor %}
    </ul>

    <h2>Numbers</h2>
    {% for number in numbers %}
        {% if number % 2 ==0 %}
            <li>{{ number }}</li>
        {% endif%}
    {% endfor %}

</body>
</html>
-------------------------------------------------------------------------------------



























































