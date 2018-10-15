from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Lets see what we can do right now! If you want to see the other pages i recommend doing the following on copying and pasting, future links to click and go over will be done soon. https://it231-kvillalobos421855861.codeanyapp.com/projects or try https://it231-kvillalobos421855861.codeanyapp.com/about"
  
@app.route('/projects')
def projects():
    return 'The project page! This is where were going to talk about the project planning for the future project, hahah, well were going to make a webpage server where you can create an account and just have a small blog about yourself, that or either a chatting service.'

@app.route('/about')
def about():
    return 'The about page! Well were going to try to get more info on the project, but currently more on the about is were going to do a lot of coding and getting help from the professor, keep working hard and dont give up.'