from flask import Flask,render_template
app = Flask(__name__)

posts = [
{
	'author' :'Jonathan Holder',
	'title':'Day in the life...',
	'content':'Day in the life of a DevOps Engineer',
	'date_posted':'June 2020'

},

]





@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html',posts=posts)


@app.route("/About")
def about():
    return  render_template('about.html', title='About')

if __name__=='__main__':
	app.run(debug=True)








