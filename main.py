import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  return render_template("home.html", projects=projects.setup())

#connects /hello path of server to render hello.html
@app.route('/hello/')
def hello_rooute():
  return render_template("hello.html", projects=projects.setup())

#connects /flask path of server to render flask.html
@app.route('/flask/')
def flask_route():
  return render_template("flask.html", projects=projects.setup())

@app.route('/pokedex/')
def pokedex():
  return render_template("pokedex.html", projects=projects.setup())
	
@app.route('/pokedexv/')
def pokedexv():
  return render_template("pokedexv.html", projects=projects.setup())

@app.route('/bulbasaur/')
def bulbasaur():
  return render_template("bulbasaur.html", projects=projects.setup())

@app.route('/squirtle/')
def squirtle():
  return render_template("squirtle.html", projects=projects.setup())

@app.route('/charmander/')
def charmander():
  return render_template("charmander.html", projects=projects.setup())

if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(port='3000', host='0.0.0.0')


