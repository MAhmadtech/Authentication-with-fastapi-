from fastapi import FastAPI
from config import engine


import tables.users as User_table
import routes.users as User_routes




User_table.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(User_routes.router)