from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from typing import List
import fitz  
from database import SessionLocal, engine 
from sqlalchemy.orm import Session
from models import Base
from models import File as FilesUpload
from datetime import datetime
from pydantic import BaseModel
import os
from llama_index.llms.gemini import Gemini
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request


GOOGLE_API_KEY = "AIzaSyD_e5Bk00mK1a9l8kNBwXnsPV26VwcrkMU"  # add your GOOGLE API key here
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY




Base.metadata.create_all(bind=engine)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow all  origin (just for development phase)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


class QuestionRequest(BaseModel):
    question: str
    id: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
       
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Invalid file type")
        
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        document = FilesUpload(filename=file_location,  uploadDate=upload_date)
        db.add(document)
        db.commit()
        db.refresh(document)
        return {"success": True, "id": document.id}, 200
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        document = fitz.open(pdf_path)
        text = ""
        for page in document:
            text += page.get_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# here we can change this to get request if we don't have to save anything in the future.
@app.post("/ask")
async def ask_question(request: Request, db: Session = Depends(get_db)):
   
    try:
        reqData = await request.json()
        question = reqData["question"]
        id = reqData["id"]
        ID = int(id)
        file = db.query(FilesUpload).filter(FilesUpload.id == ID).first()
        if not file:
            raise HTTPException(status_code=404, detail="Document not found")
        
        file_location = f"{file.filename}"
        
        content = extract_text_from_pdf(file_location)

        answer = generate_answer(question, content)
        
        return {"success": True, "answer": answer}, 200
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def generate_answer(question: str, context: str) -> str:
     
    #APIKEY = os.getenv("OAPI_KEY")

    answer = Gemini(model='models/gemini-pro').complete(f"based on following content: {context}, ; give me answer of Question : {question}")
    return answer


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
