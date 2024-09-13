### Vue 3 & FastAPI Starter Project
This project combines a Vue.js front-end with a FastAPI back-end to create a full-stack application. Below are the steps to set up both parts of the project.

### Front-End Setup (Vue 3 with Vuetify & Pinia)
1. Create a new Vue project with Vuetify and Pinia
To start, create the Vue 3 project using the following command:
npm create vuetify@latest

Select NPM when prompted.
Select Pinia as your state management library when asked.

2. Clean up the initial project files
Once the project is created:

Navigate to the layouts folder and delete the default HelloWorld.vue file.
Create your own layout component or structure.

3. Remove unused imports
Open the router/index.js or router/index.ts file (depending on your setup) and remove the imports for any components that you deleted, such as HelloWorld.vue.
Make sure to remove corresponding routes as well if they point to these deleted components.

### Back-End Setup (FastAPI with Uvicorn)
1. Create a Python virtual environment
For Windows, run the following commands to create and activate a Python virtual environment:

python -m venv venv
.\venv\Scripts\Activate

2. Install dependencies
After activating the virtual environment, install FastAPI and Uvicorn:
pip install fastapi uvicorn

3. Create the backend folder and app.py file
Create a folder called backend.
Inside that folder, create a file called app.py and add the following code:

# backend/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

4. Run the FastAPI application
To run the FastAPI server, execute the following command:
uvicorn backend.app:app --reload

The server will start, and you can now access the FastAPI endpoint by visiting the following URL in your browser:


http://127.0.0.1:8000/
Here, you'll see the default JSON response from the FastAPI back-end: {"Hello": "World"}.

5. Configure the Vite Proxy for FastAPI
To enable communication between your Vue front-end and FastAPI back-end, you need to configure the Vite development server to proxy requests. Open the vite.config.mjs file located at:

### vite.config.mjs
Add the following proxy configuration under server:

server: {
  proxy: {
    '/': {
      target: 'http://localhost:8000',
      changeOrigin: true,
      secure: false,
    }
  }
}
This configuration tells Vite to forward any requests from the Vue front-end to the FastAPI back-end running on http://localhost:8000.

Now you have a working full-stack application with a Vue.js front-end and FastAPI back-end!