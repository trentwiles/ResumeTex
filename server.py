from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resume.resume_maker import ResumeMaker
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def cleanup():
    ResumeMaker.clean_up_temp_files()


@app.get("/")
async def root():
    return FileResponse("public/index.html")


@app.get("/api/v1/text")
async def predict(data: dict):
    resume = ResumeMaker()
    return resume.get_complete_latex(data)


@app.get("/api/v1/tex")
async def predict(data: dict):
    resume = ResumeMaker()
    latex_content = resume.get_complete_latex(data)
    return FileResponse(
        content=latex_content.encode(), media_type="text/plain", filename="resume.tex"
    )


@app.get("/api/v1/pdf")
async def get_pdf(data: dict, background_tasks: BackgroundTasks):
    resume = ResumeMaker()
    try:
        pdf_path = resume.generate_pdf(data)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate PDF: {str(e)}")

    background_tasks.add_task(cleanup)
    response = FileResponse(
        path=pdf_path, media_type="application/pdf", filename="resume.pdf"
    )

    return response
