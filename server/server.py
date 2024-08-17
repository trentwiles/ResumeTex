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

@app.post("/predict")
async def predict(data: dict):
    print(data.keys())
    latex = Resume() if 'font' not in data else Resume(data['font'])
    for key, value in data.items(): 
        match key:
            case "personal_info": latex.add_personal_info(value)
            case "education" : latex.add_education(value)
            case "experience" : latex.add_work_experience(value)
            case "skills" : latex.add_skills(value)
            # case "projects" : latex.add_projects(value)
            # case "interests" : latex.add_interests(value)
    return latex.get_complete_latex()