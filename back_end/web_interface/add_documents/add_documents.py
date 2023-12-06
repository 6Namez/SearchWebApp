# add_documents.py

# Imports
    # Web framework import
from flask import render_template


# render add document page
def addDocumentPage():
    return render_template('add_documents.html')