from main import db, login_manager, bcrypt
from flask_login import UserMixin


# Login manager for admin login
@login_manager.user_loader
def load_user(user_id):
    return AdminUser.query.get(int(user_id))

# this model records the details of mentorship applicants 
class Mentorship(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name= db.Column(db.String(length=25), nullable=False)
    last_name= db.Column(db.String(length=25), nullable=False)
    email= db.Column(db.String(), nullable=False)
    phone_number= db.Column(db.String(length=15), nullable=False)
    reason = db.Column(db.String(), nullable=False)
    career_choice = db.Column(db.String(), nullable=False)

    def user_name(self):
        return f"{self.last_name} {self.first_name}"


# this model holds the details of a career path 
class Career(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    career_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    img = db.Column(db.Text(), nullable=False)
    img_name = db.Column(db.Text(), nullable=False)
    mimetype = db.Column(db.Text(), nullable=False)


# this model keeps the details required of an admin to login successfully
class AdminUser(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password 
    
    # decrypting password hash to compare with the password entered at login 
    @password.setter
    def password(self, plain_text):
        self.password_hash = bcrypt.generate_password_hash(plain_text).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


