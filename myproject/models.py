from extensions import db

# from extensions import admin
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, EmailField, SubmitField, DateField, IntegerField, SelectField
# from wtforms.validators import InputRequired, Email, Length

# class LoginForm(FlaskForm):
#     email = EmailField("Email", validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
#     password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=80)])
#     remember = BooleanField("Remember Me")
#     submit = SubmitField("Submit")
    
# class RegisterForm(FlaskForm):
   
#     fullname = StringField("Fullname", validators=[InputRequired(), Length(min=4, max=20)])
#     email = EmailField("Email", validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
#     password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=80)])
#     mobile = IntegerField("Mobile", validators=[InputRequired()])
#     birthdate = DateField("Birthdate", validators=[InputRequired(),])
#     gender = SelectField("Gender", choices=["Male","Female"], validators=[InputRequired()])
#     submit = SubmitField("Submit")


class User(db.Model):
    
    __tablename__= 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    birthdate = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    checkbox = db.Column(db.String(50), nullable=False)
   
    
    
    def __init__(self, firstname, lastname, username, mobile, address, email, password, gender, birthdate, checkbox):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.mobile = mobile
        self.address = address
        self.email = email
        self.password = password
        self.gender = gender
        self.birthdate = birthdate
        self.checkbox = checkbox
        
        

class Donate(db.Model):
    
    __tablename__ = "donate"
    
    id = db.Column(db.Integer, primary_key=True)
    donorname = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.String(100), nullable=False)
    donatedate = db.Column(db.String(100), nullable=False)
    donate_location = db.Column(db.String(250), nullable=False)
    blood_group = db.Column(db.String(100), nullable=False)
    previously_donated = db.Column(db.String(50), nullable=False)
    lasttime = db.Column(db.String(100), nullable=True)
    
    
    
    def __init__(self, donorname, phone, address, email, gender, birthdate, donatedate, donate_location, blood_group, previously_donated, lasttime):
        
        self.donorname = donorname
        self.phone = phone
        self.address = address
        self.email = email
        self.gender = gender
        self.birthdate = birthdate
        self.donatedate = donatedate
        self.donate_location = donate_location
        self.blood_group = blood_group
        self.previously_donated = previously_donated
        self.lasttime = lasttime
        
    
        