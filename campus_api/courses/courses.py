from fastapi import APIRouter
 
router = APIRouter(prefix="/courses", tags=["courses"])
 
courses = ["Python", "SQL", "FastAPI"]
 
@router.get("")
def list_courses():
    return courses
 
@router.get("/count")
def count_courses():
    return len(courses)
 
@router.get("/search")
def search_courses(text: str = ""):
    return [c for c in courses if text.lower() in c.lower()]
