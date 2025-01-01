# FastAPI CRUD Project

This repo demonstrates the task of performing crud using fastapi and mongoDB 

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MongoDB running locally at the default URI: `mongodb://localhost:27017`

### **Warning: MongoDB URI**
- Make sure that MongoDB is up and running at the following URI: `mongodb://localhost:27017`.
- If MongoDB is not running, the application will fail to connect to the database.

## Steps to Run the Project

### **1. Set Up a Virtual Environment**

First, create a virtual environment to isolate your project dependencies:

1. Open a terminal and navigate to your project directory.
2. Run the following command to create a virtual environment:

    - For **Windows**:
    ```bash
    python -m venv fastapienv
    ```

3. Activate the virtual environment:

    - For **Windows**:
    ```bash
    fastapienv\Scripts\activate.bat
    ```

    You should see the virtual environment name `(fastapienv)` in the terminal prompt.

---

### **2. Install Dependencies**

Once the virtual environment is activated, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### **3. Run the Uvicorn server at port 8000 (as the port number is hardcoded)**

```bash
uvicorn main:app --reload --port 8000
```

### **4.Access the full stack application by running the html file on any browser**

```bash
http://127.0.0.1:8000

```