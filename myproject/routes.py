from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Donate
import datetime


main = Blueprint("main",__name__)

@main.route("/",methods=["GET","POST"])
def home():
    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()

        if session['email']:
            donate = Donate.query.filter_by(email=session['email']).first()
    except:
        return render_template("home.html")
    else:
        return render_template("home.html", user=user)

@main.route("/register", methods=["GET","POST"])
def register():

    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()
    except:
        if request.method == "POST":

            firstname = request.form["firstname"]
            if firstname == "" or firstname == None:
                return "Invalid firstname"

            lastname = request.form["lastname"]
            if lastname == "" or lastname == None:
                return "Invalid lastname"
        
            username = request.form["username"]
            if username == "" or username == None:
                return "Invalid username"
            mobile = request.form["mobile"]
            if mobile == "" or mobile == None or int(len(mobile))>10 or int(len(mobile))<10:
                return "Invalid mobile"
            if not int(mobile):
                return("Please Enter Only Numbers.")
        
            address = request.form["address"]
            if address == "" or address == None:
                return "Invalid address"
            email = request.form["email"]
            if email == "" or email == None:
                return "Invalid lastname"
            
            password = request.form["password"]
            if password == "" or password == None:
                return "Invalid password"
            gender = request.form["gender"]
            if gender == "" or gender == None:
                return "Invalid gender"
            
            birthdate = request.form["birthdate"]
            print(birthdate)
            date_format = '%Y-%m-%d'
            birthdate = datetime.datetime.strptime(birthdate, date_format).date()
            print(birthdate)
            validation_date = datetime.datetime.now().date()
            print(validation_date)

            if birthdate == "" or birthdate == None or (validation_date-birthdate).days<18*365:
                return "Invalid birthdate"
            checkbox = request.form["checkbox"]
            if checkbox == "" or checkbox == None:
                return "Invalid checkbox"
            
            
            user = User.query.filter_by(email=email).first()
            if user:
                # return redirect(url_for("auth.login"))
                # return "This Email is already registerd."
                flash('Email address already exists.')
                return redirect(url_for('main.register'))
            
            new_user = User(firstname=firstname, lastname=lastname,username=username, mobile=mobile, address=address, email=email, password=generate_password_hash(password), gender=gender, birthdate=birthdate, checkbox=checkbox)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("main.login"))
        return render_template("register.html")
    else:
        return render_template("register.html", user=user)
    
@main.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        if email == "" or email == None:
            return "Invalid email"
        password = request.form["password"]
        if password == "" or password == None:
            return "Invalid password"
        
        user = User.query.filter_by(email=f"{email}").first()
        if user and check_password_hash(user.password,password):
            session["email"] = user.email
            
        if not user or not check_password_hash(user.password, password):
            flash("Email address NOT exists.")
            return redirect("/login")
        
        return redirect(url_for("main.dashboard",user=user))
                
    return render_template("login.html")

@main.route("/dashboard")
def dashboard():
    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()

        if session['email']:
            donate = Donate.query.filter_by(email=session['email']).first()
    except:
        return render_template("login.html")
    else:
        return render_template("dashboard.html", user=user, donate=donate)
    

    
@main.route("/search", methods=["GET","POST"])
def search():
    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()
    except:
        search = request.form["search"].capitalize()
        if search == "" or search == None:
                return "Invalid Search."
        all_donor = Donate.query.filter_by(donate_location=search).all()
        print(all_donor)

        return render_template("home.html",all_donor=all_donor, search=search)
    else:
       
        if request.method == "POST":
            search = request.form["search"].capitalize()
            if search == "" or search == None:
                return "Invalid Search."

            all_donor = Donate.query.filter_by(donate_location=search).all()
            print(all_donor)
        
            return render_template("home.html",all_donor=all_donor, search=search, user=user)

@main.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')


@main.route("/donate", methods=["GET","POST"])
def donate():
    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()
    except:
        return render_template("donate.html")
    else:
        if request.method == "POST":
            donorname = request.form["name"]
            if donorname == "" or donorname == None:
                return "Invalid donorname"
            
            phone = request.form["phone"]
            if phone == "" or phone == None:
                return "Invalid phone"
            
            address = request.form["address"]
            if address == "" or address == None:
                return "Invalid address"
            
            email = request.form["email"]
            if email == "" or email == None:
                return "Invalid email"
            user = User.query.filter_by(email=f"{email}").first()
            if user:
                flash("Can not donate.")
                return redirect("/donate")
            
            gender = request.form["gender"]
            if gender == "" or gender == None:
                return "Invalid gender"
            
            birthdate = request.form["birthdate"]
            date_format = '%Y-%m-%d'
            birthdate = datetime.datetime.strptime(birthdate, date_format).date()
            validation_date = datetime.datetime.now().date()
            if birthdate == "" or birthdate == None or (validation_date-birthdate).days<18*365:
                return "Invalid birthdate"
            
            donatedate = request.form["donatedate"]
            if donatedate == "" or donatedate == None:
                return "Invalid donatedate"
            date_format = '%Y-%m-%d'
            donatedate = datetime.datetime.strptime(donatedate, date_format).date()
            validation_date = datetime.datetime.now().date()
            if donatedate < validation_date:
                return "Invalid donatedate."

            # district = request.form["district"]
            # taluka = request.form["taluka"]
            # place = request.form["place"]
            donate_location = request.form["location"]
            blood_group = request.form["bloodgroup"]
            previously_donated = request.form["previouslydonated"]
            if previously_donated == "No":
                lasttime = "Null"
            else:
                lasttime = request.form["lasttime"]
            
            
            new_user = Donate(donorname=donorname, phone=phone, address=address, email=email, gender=gender, birthdate=birthdate, donatedate=donatedate, donate_location=donate_location, blood_group=blood_group, previously_donated=previously_donated, lasttime=lasttime)
            db.session.add(new_user)
            db.session.commit()
            
            all_donor = Donate.query.all()
            
            return render_template("require.html",all_donor=all_donor, user=user)
            
        return render_template("donate.html",user=user)
        
@main.route("/require")
def require():
    try:
        if session['email']:
            user = User.query.filter_by(email=session['email']).first()
            all_donor = Donate.query.all()
    except:
        all_donor = Donate.query.all()
        return render_template("require.html", all_donor=all_donor)
    else:
        return render_template("require.html",user=user, all_donor=all_donor)

