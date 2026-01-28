# Video class https://www.youtube.com/watch?v=FBLAV1SbJFk

# Endpoints
# ----------------------------
#   - localhost/books (GET)
#   - localhost/books/id (GET)
#   - localhost/books (POST)
#   - localhost/books/id (PUT)
#   - localhost/books/id (DELETE)

# install/uninstall Flask:
#   pip install flask
#   pip uninstall flask

from flask import Flask, jsonify, request

app = Flask(__name__) # criação da aplicação flask com o nome do arquivo atual.

# dictionaries list
books = [
    {
        'id': 1,
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling'
    },
    {
        'id': 3,
        'title': 'Atomic Habits',
        'author': 'James Clear'
    }
] 

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id: # or using book['id'] == id
            return jsonify(book)
        
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:id>', methods=['PUT'])
def put_book_by_id(id):    
    updated_book = request.get_json() # get the data sent in the request body as JSON
        
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(updated_book)

            return jsonify(books[index])

@app.route('/books', methods=['POST'])
def post_book():
    new_book = request.get_json() # get the data sent in the request body as JSON
    books.append(new_book)

    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]  # or using: books.pop(index)

            return jsonify(books)

app.run(port = 5000, host = 'localhost', debug = True)
