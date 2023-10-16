from flask import Flask, render_template
from extensions import db
from routes import main
from extensions import admin
from flask_admin.contrib.sqla import ModelView
from models import User,Donate


app = Flask(__name__)
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="pradip",url="localhost:5432",db="blood")
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config["SECRET_KEY"] = "SK"

db.init_app(app)
admin.init_app(app)

app.register_blueprint(main)


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Donate, db.session))

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)