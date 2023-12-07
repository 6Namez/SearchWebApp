# app.py 

# Imports
    # Web framework import
from flask import Flask

    # Back End imports
from back_end.web_interface.index.index import indexPage
from back_end.web_interface.search.search import searchPage
from back_end.web_interface.add_documents.add_documents import addDocumentPage



# Create an instance of the Flask class
app = Flask(__name__)




# Page Route Calls

# app route for index page
@app.route('/')
def index_route():
    return indexPage()

# index page function rotes
# none


# app route for search page
@app.route('/search')
def search_route():
    return searchPage()

# index page function rotes
# none


# app rote for add document page
@app.route('/add_documents')
def add_documents_route():
    return addDocumentPage()

# index page function rotes
# none





# Run app
if __name__ == '__main__':
    app.run(debug=True)