from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User,Blogs
from flask_login import login_required, current_user
from .forms import UpdateProfile,BlogsForm
from .. import db, photos
from .. requests import getQuotes

@main.route('/')
def index():
    blog = Blogs.get_blogs()
    isoko = getQuotes()

    return render_template('index.html',  blog = blog, isoko = isoko)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    
@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/add/blogers', methods=['GET','POST'])
@login_required
def inyandiko():
    
    form = BlogsForm()

    if form.validate_on_submit():
        title = form.title.data
        texto = form.texto.data
        inyandiko = Blogs(texto=texto, title=title)
        inyandiko.ububiko()

        return redirect(url_for('.index'))

    title = 'Blogs'
    return render_template('new_blog.html', blog_form = form,title=title)

@main.route('/blogers/<int:id>')
def bloger(id):
    bloge = Blogs.query.get(id)

    return render_template('index.html', bloge=bloge) 

@main.route('/comment/<int:id>',methods=['POST','GET'])
def comment(id):
    form=CommentForm()
    bloga = Blogs.query.get(id)
    commento = Comment.query.filter_by(id = id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blogerss = blogerss
        user = user
        newcomment = Comment(comment = comment,user = user,bloga = bloga)
        newcomment.save_comme()

    title = 'Comments'
    return redirect(url_for('.comment',blog_id = blog_id))
    return render_template('comment.html',form=form, title = title,bloga = bloga,commento=commento)     

@main.route('/deletecomment/<int:id>', methods = ['GET','POST'])
@login_required
def deletecomment(id):

    current_post = Comment.query.filter_by(id = id).first()

    if current_post.writer != current_user:
        abort(404)

    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.index'))
    return render_template('comment.html',current_post = current_post)

@main.route('/update/<int:id>',methods= ['GET','POST'])
@login_required
def updateblog(id):

    blogs = Blog.query.filter_by(id = id).first()
    if blogs is None:
        abort(404)

    form = UpdateBlogForm()

    if form.validate_on_submit():

        blogs.title = form.title.data
        blogs.content = form.content.data

        db.session.add(blogs)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('update_blog.html',form = form)