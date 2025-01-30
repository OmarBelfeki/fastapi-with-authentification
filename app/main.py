from fastapi import FastAPI, status
from app.auth import routes as auth_routes
from app.users import routes as user_routes
from app.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(user_routes.router, prefix="/users")

@app.get(path="/", response_model=dict, status_code=status.HTTP_200_OK)
def home():
    return {"message": "Welcome to FastAPI Auth System"}


print("omar", flush=True)
