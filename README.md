## Project Setup Instructions
### Backend Setup

+  Navigate to the Backend Directory:
```
cd backend
```
+ Install Required Packages:
```
pip install fastapi sqlalchemy alembic uvicorn sqlalchemy psycopg2-binary pymupdf pydantic llama_index
```
+ Add database url in alembic.ini under sqlalchemy.url name and in the file named database.py, Note that add url in alembic without quotes  
+ Add google api key with google ai studio features enabled from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
+ cut/paste this to alembic/envpy:
```
from logging.config import fileConfig  
from sqlalchemy import engine_from_config  
from sqlalchemy import pool  
from database import Base  
from models import *  
from alembic import context  
config = context.config  
if config.config_file_name is not None:  
fileConfig(config.config_file_name)  
  
target_metadata = Base.metadata  
  
def run_migrations_offline() -> None:  
url = config.get_main_option("sqlalchemy.url")  
context.configure(  
url=url,  
target_metadata=target_metadata,  
literal_binds=True,  
dialect_opts={"paramstyle": "named"},  
)  
  
with context.begin_transaction():  
context.run_migrations()  
  
  
def run_migrations_online() -> None:  
connectable = engine_from_config(  
config.get_section(config.config_ini_section, {}),  
prefix="sqlalchemy.",  
poolclass=pool.NullPool,  
)  
  
with connectable.connect() as connection:  
context.configure(  
connection=connection, target_metadata=target_metadata  
)  
  
with context.begin_transaction():  
context.run_migrations()  
  
  
if context.is_offline_mode():  
run_migrations_offline()  
else:  
run_migrations_online()
```

+ alembic revision --autogenerate -m "Initial migration"  
+ alembic upgrade head  
+ make an upload directory in the backend directory where alembic folder lies


### Go to frontend directory :
+ `npm create vite@latest  
+ setup tailwind from [https://tailwindcss.com/docs/guides/vite](https://tailwindcss.com/docs/guides/vite)
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
