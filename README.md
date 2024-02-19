# ToDo App Backend
This is a brief description of the project.

## Prerequisites

Before you begin, make sure you have the following requirements installed:

- Python (version 3.11.X)
- pip (Python package manager)
- Git (optional)

## Getting Started

To get started with this project, follow these steps:

### Clone the Repository

You can clone this repository using Git by running the following command:

```bash
git clone https://github.com/malek-bt/ToDo_app_back.git
```

### Installation

1. Navigate to the project directory:

   ```bash
   cd ToDo_app_back
   ```

2. Create a virtual environment (optional but recommended):

   On Unix/macOS:

   ```bash
   python -m venv venv
   ```

   On Windows:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   On Unix/macOS:

   ```bash
   source venv/bin/activate
   ```

   On Windows (Command Prompt):

   ```bash
   venv\Scripts\activate
   ```

   On Windows (PowerShell):

   ```bash
   .\venv\Scripts\Activate.ps1
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Perform database migrations:

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

### Running the Application

Now you can run the application:

```bash
python manage.py runserver
```

The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

To access specific parts of the application, navigate to the corresponding URLs (e.g., `/todo/createToDo`, `/todo/getToDos`, `/todo/updateToDo/<int:id>` , `/todo/deleteToDo`).

