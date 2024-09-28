from fastapi import APIRouter

router = APIRouter()

@router.get("/resumes/")
def get_resumes():
    return [{"resume_id": 1, "name": "John's Resume"}, {"resume_id": 2, "name": "Jane's Resume"}]

@router.post("/resumes/")
def create_resume(resume: dict):
    return {"message": f"Resume {resume['name']} created successfully!"}
