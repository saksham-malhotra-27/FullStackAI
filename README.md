## Project Setup Instructions
<img src="https://github.com/saksham-malhotra-27/FullStackAI/assets/147790402/f16784aa-5def-4902-ba6d-e00c8118c1af"  width="full" height="400"/>
<img src="https://github.com/saksham-malhotra-27/FullStackAI/assets/147790402/af5acbb7-5573-4e78-acb4-cc09727afe82" width="full" height="400"/>

### Backend Setup

+  Navigate to the Backend Directory:
```
cd backend
```
+ Install Required Packages:
```
pip install fastapi sqlalchemy alembic uvicorn sqlalchemy psycopg2-binary pymupdf pydantic llama_index.llms.gemini
```
+ Initialize alembic (make sure you are in backend directory) using:
```
alembic init alembic 
```
+ Add postgresql database url in alembic.ini under sqlalchemy.url name and in the file named database.py, Note that add url in alembic.ini without quotes
+ Also, copy / paste the content inside backend/env.py to backend/alembic/env.py and delete thr former file
+ Add google api key with google ai studio features enabled from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
+ Run these commands (make sure in the backend dir)
```
alembic revision --autogenerate -m "Initial migration"  
alembic upgrade head
```
+ Make an uploads directory in the backend directory where alembic folder lies
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
+ Run the app:
```
npm run dev
```
