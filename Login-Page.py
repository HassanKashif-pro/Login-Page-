from flask import Flask, request

app = Flask(__name__)

login = {}
login['david'] = {"email" : "apm@example.com", "password" : "1234", "usesrname" : "david33"}
login['admin'] = {"email" : "k8@example.com", "password" : "K8T", "username" : "katie34"}

@app.route('/login', methods=['POST'])
def login_user():
  form = request.form
  isThere = False
  details = {}
  try:
    details = login[form["username"]]
    isThere = True
  except:
    return "username, password or email is in correct."
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "you are logged In"
  else:
    return "username, password or email is in correct."
    

@app.route('/')
def index():
  page = """<form method = "post" action="/process">
    
  <p>Username : <input type="text" name="username"</p>
  <p>  Email  : <input type="Email" name="email"> </p>
  <p>Password : <input type="password" name="password"</p><br><br>
  <button type="Login">Login</button>
</body>
  </form>
    """
  return page
  
app.run(host='0.0.0.0', port=81)