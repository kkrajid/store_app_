

![E-commerce Server Flowchart](chart1.png)

# E-commerce Backend

This project is a simple e-commerce backend system built with Python. It provides basic functionality for managing products through a RESTful API.

## Features

- HTTP server handling GET, POST, PUT, and DELETE requests
- SQLite database for storing product information
- RESTful API endpoints for product management
- Simple routing system

## Project Structure

```
ecommerce-backend/
│
├── main.py              # HTTP server and request handler
├── router.py            # URL routing logic
├── views.py             # View functions for handling requests
├── models.py            # Database models and operations
└── README.md            # This file
```

## Prerequisites

- Python 3.6 or higher
- SQLite3

## Setup and Installation

1. Clone the repository:
   ```
   git clone [https://github.com/yourusername/ecommerce-backend.git](https://github.com/kkrajid/store_app_.git)
   cd ecommerce-backend
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install sqlite3
   ```

## Running the Server

To start the server, run:

```
python main.py
```

The server will start running on `http://localhost:8000`.

## API Endpoints

- `GET /products`: Retrieve all products
- `GET /product/{id}`: Retrieve a specific product by ID
- `POST /product/add`: Add a new product

### Adding a Product

To add a product, send a POST request to `/product/add` with a JSON body:

```json
{
  "name": "Product Name",
  "price": 19.99,
  "description": "Product description"
}
```

## Database

The project uses SQLite as its database. The database file (`ecommerce.db`) will be created automatically when you run the server for the first time.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
