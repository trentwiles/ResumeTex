from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from resume import Resume

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

@app.post("/tex")
async def predict(data: list):
    latex = Resume() if 'font' not in data else Resume(data['font'])
    for item in data:
        match item['type']:
            case 1:
                latex.add_personal_info(item['data'])
            case 2:
                latex.add_education(item['data'])
            case 3:
                latex.add_work_experience(item['data'])
            case 4:
                latex.add_skills(item['data'])
            case 5:
                latex.add_projects(item['data'])
            case 6:
                latex.add_interests(item['data'])
    return latex.get_complete_latex()