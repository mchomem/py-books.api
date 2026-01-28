# Books API

A simple RESTful API, built with Flask, to manage a collection of books. This project was created to aid in the study of using Python for RESTful APIs, and offers basic CRUD operations (Create, Read, Update, Delete) for books, using a list of dictionaries as a repository.

## Features

- Get all books
- Get a specific book by ID
- Add a new book
- Update an existing book
- Delete a book

## Technologies

- Python 3.x
- Flask 3.1.2
- JSON for data exchange

## Prerequisites

- Python 3.x installed
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd py-books.api
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. The API will be available at `http://localhost:5000`

## API Endpoints

### Get All Books
```
GET /books
```
Returns a list of all books.

**Response:**
```json
[
    {
        "id": 1,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien"
    },
    ...
]
```

### Get Book by ID
```
GET /books/<id>
```
Returns a specific book by its ID.

**Response:**
```json
{
    "id": 1,
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien"
}
```

### Create a New Book
```
POST /books
```
Creates a new book entry.

**Request Body:**
```json
{
    "id": 4,
    "title": "Book Title",
    "author": "Author Name"
}
```

**Response:**
Returns the updated list of all books.

### Update a Book
```
PUT /books/<id>
```
Updates an existing book by its ID.

**Request Body:**
```json
{
    "title": "Updated Title",
    "author": "Updated Author"
}
```

**Response:**
Returns the updated book.

### Delete a Book
```
DELETE /books/<id>
```
Deletes a book by its ID.

**Response:**
Returns the updated list of all books.

## Project Structure

```
py-books.api/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Dependencies

- **Flask**: Web framework for Python
- **Werkzeug**: WSGI utility library
- **Jinja2**: Template engine
- **Click**: Command-line interface creation kit
- **MarkupSafe**: String handling library
- **itsdangerous**: Data signing library
- **blinker**: Signal/event library
- **colorama**: Cross-platform colored terminal text

## Development

The application runs in debug mode by default, which enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

**Note:** Disable debug mode in production environments.

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Based on the tutorial: https://www.youtube.com/watch?v=FBLAV1SbJFk

## Author

mchomem

## Support

For support, please open an issue in the repository.
