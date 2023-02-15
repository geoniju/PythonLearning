from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html', num = 20, op_name = "nothing")

# @app.route('/<name>')
# def guess(name):
#     return render_template('index.html', num = 20, op_name = name)
# A decorator used to tell the application
# which URL is associated function
# @app.route('/', methods =["GET", "POST"])
# def gfg():
#     if request.method == "POST":
#        # getting input with name = fname in HTML form
#        first_name = request.form.get("fname")
#        # getting input with name = lname in HTML form
#        last_name = request.form.get("lname")
#        return "Your name is "+first_name + last_name
#     return render_template("form.html")
@app.route('/')
def student():
   return render_template('student.html')
  
@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('result.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)