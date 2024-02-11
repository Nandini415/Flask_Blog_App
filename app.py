from flask import Flask, jsonify,render_template,redirect,request,url_for,session
from model import *

from model import db
from api import *

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Blogs.sqlite3' #database creation
api.init_app(app)
db.init_app(app) #db init
app.app_context().push() 


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/')
# def index():
#     b=Blog.query.all() #forms query in dict
#     return render_template('index.html',blogs=b)

# @app.route('/')
# def index():
#     b=Author.query.all() #forms query in dict
#     return render_template('Author.html',authors=b)

# @app.route('/get_blog/<int:blog_id>')
# def get_blog(blog_id):
#     blog=Blog.query.get(blog_id)
#     return jsonify({'id':blog_id, 'title':blog.title,'content':blog.content})

# @app.route('/submit-authorapi',methods=['POST'])
# def submit_author1():
#     data=request.get_json()
#     a=data['authorName']
#     b=data['authorEmail']
#     author=Author(name=a,email=b)
#     db.session.add(author)
#     db.session.commit()
#     return jsonify({'message': 'Author added successfully'})

# @app.route('/submit-author', methods=['POST'])
# def submit_author():
#     a = request.form['authorName']
#     b = request.form['authorEmail']
#     author = Author(name = a, email=b)
#     db.session.add(author)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/delete_author/<int:author_id>')
# def delete_author(author_id):
#     author=Author.query.get(author_id)
#     blogs=author.blog_relation
#     for blog in blogs:
#         ass=Association.query.filter_by(blog_id=blog_id).first()
#         db.session.delete(ass)
#         db.session.delete(blog)
#     db.session.delete(author)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/edit-author/<int:author_id>',methods=['POST'])
# def edit_author(author_id):
#     author=Author.query.get(author_id)
#     a = request.form['authorName']
#     b = request.form['authorEmail']
#     author.name=a
#     author.email=b
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/blogs/<int:author_id>')
# def blogs(author_id):
#     author=Author.query.get(author_id)
#     blogs=author.blog_relation
#     return render_template('Blog.html',blogs=blogs,author=author)

# @app.route('/submit-blog/<int:author_id>',methods=['POST'])
# def submit_blog(author_id):
#     a=request.form['blogTitle']
#     b=request.form['blogContent']
#     blog=Blog(title=a,content=b,author_id=author_id)
#     db.session.add(blog)
#     db.session.commit()

#     blog=Blog.query.filter_by(title=a,content=b).first()
#     bid=blog.id

#     association=Association(blog_id=bid,author_id=author_id)
#     db.session.add(association)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/delete_blog/<int:blog_id>')
# def delete_blog(blog_id):
#     blog=Blog.query.get(blog_id)
#     association=Association.query.filter_by(blog_id=blog_id).first()
#     db.session.delete(association)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for('blogs',author_id=association.author_id))

# @app.route('/edit-blog/<int:blog_id>',methods=['POST'])
# def edit_blog(blog_id):
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     Blog.query.filter_by(id=blog_id).update({'title':a,'content':b})
#     association=Association.query.filter_by(blog_id=blog_id).first()
#     db.session.commit()
#     return redirect(url_for('blogs',author_id=association.author_id))
    

if __name__=="__main__":
    app.run(debug=True)


# @app.route('/submit-blog', methods=['POST'])
# def submit_blog():
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     blog = Blog(title = a, content=b)
#     db.session.add(blog)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/delete_blog/<int:blog_id>')
# def delete_blog(blog_id):
#     blog=Blog.query.get(blog_id)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/edit-blog/<int:blog_id>',methods=['POST'])
# def edit_blog(blog_id):
#     blog=Blog.query.get(blog_id)
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     blog.title=a
#     blog.content=b
#     db.session.commit()
#     return redirect(url_for('index'))

# if __name__=="__main__":
#     app.run(debug=True)