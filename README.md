# nlp-dev-search (HIREWAY)

**Explanation:**

* **`NLP_DEV_SEARCH/`**: The root directory of the project.
* **`.venv/`**: A virtual environment for Python dependencies, ensuring project isolation.
* **`backend/`**: Contains the server-side code, likely written in Python.
    * **`app/`**: Holds the core application logic.
        * **`__pycache__/`**: Automatically generated directory for compiled Python files.
        * **`__init__.py`**: Makes the `app` directory a Python package.
        * **`fake_data.py`**: Used for generating dummy data during development.
        * **`main.py`**: The main entry point for the backend application.
        * **`search.py`**: Implements the search functionality.
* **`.env`**: Stores environment variables (API keys, etc.). **Crucially, this file should not be committed to version control.**
* **`frontend/`**: Contains the client-side code (HTML, CSS, JavaScript).
    * **`app.js`**: JavaScript code for interactive elements and logic.
    * **`index.html`**: The main HTML file that defines the webpage structure.
    * **`styles.css`**: CSS stylesheets for styling the webpage.
* **`README.md`**: This file, providing project documentation.
* **`requirements.txt`**: Lists the Python dependencies required for the backend.

**Key Points:**

* Clear separation of backend and frontend.
* Use of a virtual environment for dependency management.
* Emphasis on not committing the `.env` file.
* Standard web development structure for the frontend.
