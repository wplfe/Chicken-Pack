from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
   return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
   return render_template(page_name)

def write_to_file(data):
   with open('database.txt', mode='a') as database:
      email = data["email"]
      file = database.write(f'\n{email}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
      data = request.form.to_dict()
      write_to_file(data)
      return redirect('/thanks.html')
   else:
      return 'try again' 