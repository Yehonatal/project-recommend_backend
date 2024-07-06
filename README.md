# Project Readmore | Backend

[Frontend Repository](https://github.com/Yehonatal/project-readmore)

Welcome to the backend repository of Readmore, a book recommendation system designed to help users discover new books based on their interests and reading history.

## Deployment

This backend is deployed on [Render](https://render.com) at [https://your-render-url.com](https://your-render-url.com).

Certainly! Here's a detailed guide on how to start a local development instance of your Flask application, manage port usage, and troubleshoot common issues:

### Starting a Local Development Instance

1. **Activate Virtual Environment**

   If you're using a virtual environment (`venv`), activate it first. Navigate to your project directory and run:

   ```bash
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate  # Windows
   ```

2. **Install Dependencies**

   Ensure you have all dependencies installed. Use `pip` to install them from your `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**

   Assuming your Flask application is structured as before (`app.py` and possibly other files):

   ```bash
   python app.py
   ```

   This command starts your Flask application locally. By default, it should run on `http://127.0.0.1:5000/`.

### Managing Ports and Processes

#### Checking Used Ports

To check which ports are currently in use, you can utilize the `lsof` command:

```bash
lsof -i :5000  # Replace 5000 with the port number you want to check
```

This command lists all processes using the specified port.

#### Killing Processes

If you need to free up a port (for example, if you encounter a "port already in use" error), follow these steps:

   ```bash
   lsof -i :5000 // Identify the Process
   ```

   ```bash
   kill -9 PID // Terminate the Process:
   ```
