from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.book import Book

@app.route('/book')
def index():
    all_books = Book.get_all()
    return render_template("books.html", all_books = all_books)

@app.route('/create/book', methods = ['POST'])
def create_book():
        data ={
            **request.form
        }
        Book.create(data)
        return redirect('/book')
