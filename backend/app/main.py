from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.routers import auth, courses, exercises, code, ai, projects, users

app = FastAPI(
    title="Python Coach API",
    description="Backend API for Python learning assistant",
    version="0.1.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(courses.router, prefix="/api/v1", tags=["courses"])
app.include_router(exercises.router, prefix="/api/v1", tags=["exercises"])
app.include_router(code.router, prefix="/api/v1", tags=["code"])
app.include_router(ai.router, prefix="/api/v1", tags=["ai"])
app.include_router(projects.router, prefix="/api/v1", tags=["projects"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
