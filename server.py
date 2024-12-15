from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resume.resume_maker import ResumeMaker
from fastapi import HTTPException
from fastapi.responses import FileResponse

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
    return FileResponse("public/index.html")


@app.get("/api/v1/tex")
async def predict(data: dict):
    resume = ResumeMaker()
    return resume.get_complete_latex(data)

@app.post("/api/v1/pdf")
async def get_pdf(data: dict):
    resume = ResumeMaker()
    try:
        pdf_path = resume.generate_pdf(data)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate PDF: {str(e)}")
    
    response = FileResponse(
        path=pdf_path,
        media_type='application/pdf',
        filename='resume.pdf'
    )
    
    @response.call_on_close
    def cleanup():
        ResumeMaker.clean_up_temp_files()
    
    return response