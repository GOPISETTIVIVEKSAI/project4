from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return 'you are in home page'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

#to open login form
@app.route('/index2',methods=['GET'])
def login():
    return render_template('index2.html')
#to receive the form data
@app.route('/login-form',methods=['POST'])
def login_form_data():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return {'response':[num1,num2]}

@app.route('/BBQ',methods=['GET'])
def bbq():
    return render_template('BBQ.html')


#Maths-------------------------------------
'''Addition'''
@app.route('/add',methods=['GET'])
def adding():
    return render_template('add.html')
@app.route('/addition',methods=['POST'])
def adding_data():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [int(num1)+int(num2)]
#-----------------------------------------------
'''subtraction'''
@app.route('/sub',methods=['GET'])
def subtract():
    return render_template('sub.html')

@app.route('/subtract',methods=['POST'])
def subtracting_data():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [int(num1)-int(num2)]
#--------------------------------------------------
'''multiplication'''
@app.route('/mul',methods=['GET'])
def multiplication():
    return render_template('mul.html')

@app.route('/multiply',methods=['POST'])
def multiplying_data():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [int(num1)*int(num2)]
#---------------------------------------------------
'''division'''
@app.route('/div',methods=['GET'])
def division():
    return render_template('div.html')

@app.route('/division',methods=['POST'])
def dividing_data():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [int(num1)//int(num2)]

app.run()