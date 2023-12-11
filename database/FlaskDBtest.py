from flask import Flask
from sneakyBackbase import db  # Import db from sneakyBackbase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\16302\\Documents\\GitHub\\SearchWebApp\\database\\your_database.db'
db.init_app(app)  # Bind the db object to the app

if __name__ == '__main__':
    
    app.run(debug=True)
