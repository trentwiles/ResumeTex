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
    try:
        return FileResponse("public/index.html")
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/v1/text")
async def predict(data: dict):
    try:
        resume = ResumeMaker()
        return resume.get_complete_latex(data)
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/v1/tex")
async def predict(data: dict):
    try:
        resume = ResumeMaker()
        latex_content = resume.get_complete_latex(data)
        return FileResponse(
            content=latex_content.encode(), media_type="text/plain", filename="resume.tex"
        )
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.post("/api/v1/pdf")
async def get_pdf(data: dict, background_tasks: BackgroundTasks):
    try:
        resume = ResumeMaker()
        pdf_path = resume.generate_pdf(data)
        background_tasks.add_task(cleanup)
        return FileResponse(
            path=pdf_path, media_type="application/pdf", filename="resume.pdf"
        )
    except Exception as e:
        print(e)
        return {"error": str(e)}
