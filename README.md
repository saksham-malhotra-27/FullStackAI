## Project Setup Instructions
### Backend Setup

+  Navigate to the Backend Directory:
```
cd backend
```
+ Install Required Packages:
```
pip install fastapi sqlalchemy alembic uvicorn sqlalchemy psycopg2-binary pymupdf pydantic llama_index llama_index.llms.gemini
```
+ Initialize alembic (make sure you are in backend directory) using:
```
alembic init alembic 
```
+ Add database url in alembic.ini under sqlalchemy.url name and in the file named database.py, Note that add url in alembic.ini without quotes
+ Also, copy / paste the content inside backend/env.py to backend/alembic/env.py and delete thr former file
+ Add google api key with google ai studio features enabled from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
+ Run these commands (make sure in the backend dir)
```
alembic revision --autogenerate -m "Initial migration"  
alembic upgrade head
```
+ Make an upload directory in the backend directory where alembic folder lies
+ Finally run the connection through :
```
uvicorn main:app --reload 
```
Note: To change the port number you have to configure the fronted's vite config file as well as the uvicorn port number in the main file under backend directory


### Go to frontend directory :
+ Install Required Packages:
```
npm install
``` 
+ setup vite config file:
```
import { defineConfig } from 'vite'  
import react from '@vitejs/plugin-react'  
  
// [https://vitejs.dev/config/](https://vitejs.dev/config/)  
export default defineConfig({  
plugins: [react()],  
server: {  
proxy: {  
'/upload': {  
target: 'http://localhost:8000',  
changeOrigin: true,  
secure: false,  
},  
'/ask': {  
target: 'http://localhost:8000',  
changeOrigin: true,  
secure: false,  
},  
},  
},  
})
```
