from flask import Flask,render_template,redirect,request,url_for,session
from model import *
app=Flask(__name__)
from model import db
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Blogs.sqlite3'

db.init_app(app)
app.app_context().push()

@app.route('/')
def index():
    b=Blog.query.all()
    return render_template('index.html',blogs=b)

@app.route('/submit-blog', methods=['POST'])
def submit_blog():
    a = request.form['blogTitle']
    b = request.form['blogContent']
    blog = Blog(title = a, content=b)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_blog/<int:blog_id>')
def delete_blog(blog_id):
    blog=Blog.query.get(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)