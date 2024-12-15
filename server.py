from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resume.resume_maker import ResumeMaker
from fastapi import HTTPException
from fastapi.responses import FileResponse

import os


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/tex")
async def predict(data: dict):
    resume = ResumeMaker(data)
    return resume.get_complete_latex()

@app.post("/pdf")
async def get_pdf(data: dict):
    resume = ResumeMaker(data)
    try:
        pdf_path = resume.generate_pdf()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    response = FileResponse(
        path=pdf_path,
        media_type='application/pdf',
        filename='resume.pdf'
    )
    
    @response.call_on_close
    def cleanup():
        ResumeMaker.clean_up_temp_files()
    
    return response