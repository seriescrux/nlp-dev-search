# HIREWAY (NLP_DEV_SEARCH) - Natural Language Powered Search Application

This project is a demonstration of a web application that leverages Natural Language Processing (NLP) to enhance search functionality. It consists of a backend (Python) and a frontend (HTML, CSS, JavaScript) designed to provide users with more intuitive and context-aware search results.

## About

The goal of this project is to showcase how NLP techniques can be integrated into a search application to understand user queries beyond simple keyword matching. By using NLP, the application can:

* **Understand intent:** Interpret the meaning behind user queries, even if they are phrased in natural language.
* **Handle synonyms and related terms:** Return relevant results even if the exact keywords are not present.
* **Provide more contextually relevant results:** Rank results based on their semantic similarity to the query.

## Project Structure
**Key Components:**

* **Backend (`backend/`)**:
    * Implemented using Python and FastAPI.
    * Handles the search logic, NLP processing, and data retrieval.
    * Uses a virtual environment (`.venv`) for dependency management.
    * The `search.py` file contains the core NLP-powered search functionality.
    * `fake_data.py` is used to simulate data for development.
    * Environment variables (API keys, etc.) are stored in `.env` (which should **NOT** be committed).
* **Frontend (`frontend/`)**:
    * Built with HTML, CSS, and JavaScript.
    * Provides the user interface for interacting with the search application.
    * `app.js` handles the client-side logic and communication with the backend.

## Getting Started

**STEP 1 - Install Dependencies:**

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd NLP_DEV_SEARCH
    ```

2.  **Create and activate a virtual environment (backend):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file (if needed) and add your environment variables.**

**STEP 2 - Run the Backend:**

1.  **Open the `backend` folder in your terminal or IDE.**
2.  **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```

**STEP 3 - Open the Frontend:**

1.  **Open a new terminal window.**
2.  **Navigate to the `frontend` directory.**
3.  **Open `index.html` in your web browser. You can typically do this by simply double-clicking the file in your file explorer, or by dragging and dropping it into your browser window.**

## Future Enhancements

* Implement more sophisticated NLP techniques (e.g., semantic search, entity recognition).
* Integrate with a real database for persistent data storage.
* Add user authentication and authorization.
* Improve the frontend user interface and user experience.
* Implement testing for both backend and frontend.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
