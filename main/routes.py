from flask_login import login_user, login_required
from main import app, db
from flask import jsonify, render_template, url_for, request, redirect, Response
from main.models import Mentorship,AdminUser, Career
from werkzeug.utils import secure_filename


# Create the database on run
with app.app_context():
    db.create_all()

# Home page route 
@app.route('/')
def home():
    return render_template("home.html")


# This route takes the name of the images based on the id of the career and render the image
@app.route('/<filename>')
def see(filename):
	img = Career.query.filter_by(img_name=filename).first()
	if not img:
		return "Image not found ", 404

	return Response(img.img, mimetype=img.mimetype)


# This route query all the available careers in the database and render it to the careers page
@app.route('/careers', methods=["GET","POST"])
def careers():
    careers = Career.query.all()
    return render_template("career.html", careers=careers)


#This route views in detail a selected career form the careers page
@app.route('/careers/<int:id>')
def career(id):
    career = Career.query.get_or_404(id)
    return render_template('careers.html', career=career)



# this route provides a form for mentorship application 
@app.route('/mentor', methods=["POST", "GET"])
def mentor():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone')
        reason = request.form.get('reason')
        career_choice = request.form.get('career_choice')

        mentee = Mentorship(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, reason=reason, career_choice=career_choice)
        
        db.session.add(mentee)
        db.session.commit()

        return redirect(url_for('careers'))
    
    return render_template("mentor.html")


# About page route 
@app.route('/about')
def about():
    return render_template("about.html")


#admin home page
@app.route('/admin', methods=["GET","POST"])
@login_required
def admin():
    careers = Career.query.all()
    return render_template("admin_home.html", careers=careers)

#a Admin login route 
@app.route('/admin/login', methods=["GET","POST"])
def admin_login():
   
    if request.method == "POST":
        attempted_user = AdminUser.query.filter_by(username=request.form.get('username')).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=request.form.get('password')):
            login_user(attempted_user)
            return redirect(url_for('admin'))
            # return redirect(url_for('admin'))
    return render_template("admin_login.html")


# the admin adds new career path sto the database through this route 
@app.route('/admin/upload', methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        # Get datails from the add career form 
        career_name = request.form.get("career_name")
        description = request.form.get("description")
        content = request.form.get('content')
        pic = request.files['file']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype

        # Saving to database 
        career = Career(career_name=career_name, description=description, content=content, img=pic.read(),mimetype=mimetype, img_name=filename)
        # adding items to the database
        db.session.add(career)
        db.session.commit()

        # if items are added successfully, the admin will be redirected
        #  to the admin home to see all the available careers
        # for verification  
        return redirect(url_for('admin'))

    return render_template("fileUpload.html")



# this route is responsible for deleting a career path from the database base on selected ID
@app.route('/admin/delete/<int:id>')
@login_required
def delete_career(id):
    career_to_delete = Career.query.get_or_404(id)
    try:
        db.session.delete(career_to_delete)
        db.session.commit()
        careers = Career.query.all()
        return render_template('admin_home.html', careers=careers)

    except ValueError:
        careers = Career.query.all()
        return render_template('admin_home.html')



# this route controls editing of an existing career and updating changes in the database 
@app.route('/admin/edit/<int:id>', methods=["POST", "GET"])
@login_required
def edit_career(id):
    # career = Career.query.get_or_404(id)
    # try:
    #     career.career_name = request.form.get('career_name')
    #     career.description = request.form.get('description')
    #     career.content = request.form.get('content')
    #     pic = request.files['file']
    #     filename = pic.filename
    #     mimetype = pic.mimetype
    # except Exception as e:
    #     return f"An error {e} occurred! "
    
    # request.form.values('career_name') = career.career_name
    # request.form.values('description') = career.description
    # request.form.get('content') = career.content
    # request.files('file') = pic
    # pic.img = career.img
    # pic.filename = career.img_name
    # pic.mimetype = career.mimetype    
    
    return render_template("admin_edit.html", )


@app.route('/admin/applicants')
@login_required
def applicants():
    return "Applicants will be listed here soon"