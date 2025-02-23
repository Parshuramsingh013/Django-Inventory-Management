# Django Inventory Management System

This is a Django-based Inventory Management System that allows users to manage product categories, track stock levels, and maintain inventory records efficiently.

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/Parshuramsingh013/Django-Inventory-Management.git
cd Django-Inventory-Management
```

### 2. Set Up Virtual Environment

```sh
python -m venv venv
```

#### Activate the Virtual Environment

- **On Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure the Database

Create a new PostgreSQL database named **Inventory\_Management**. Then, update the `DATABASES` settings in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "your_database_name",  # Replace with your database name
        "USER": "your_username",       # Replace with your database username
        "PASSWORD": "your_password",   # Replace with your database password
        "HOST": "your_host",           # Replace with your host
        "PORT": "your_port",           # Replace with your port
    }
}
```

### 5. Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Initial Categories (Optional)

```sh
python manage.py shell
```

Then, run the following commands inside the Django shell:

```python
from inventory.models import Category
Category.objects.create(name="Electronics")
Category.objects.create(name="Furniture")  # Add more categories as needed
exit()
```

### 7. Run the Server

```sh
python manage.py runserver
```

Your Django Inventory Management System should now be running at `http://127.0.0.1:8000/`.

---

## Features

- Add, edit, and delete product categories
- Track stock levels
- Manage inventory efficiently
- PostgreSQL integration

## Contributing

Feel free to fork the repository and contribute! Open an issue if you find any bugs or need improvements.

## License

This project is open-source and available under the [MIT License](LICENSE).

Happy coding! 🚀

