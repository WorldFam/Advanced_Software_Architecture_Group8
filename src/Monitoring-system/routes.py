from fastapi import APIRouter, Request, HTTPException, status
from typing import List
from bson import ObjectId
from models import LogIn, LogOut

router = APIRouter()

@router.post("/", response_description="Create a new log", status_code=status.HTTP_201_CREATED, response_model=LogOut)
def create_log(request: Request, log: LogIn):
   
    log_data = log.dict()
    log_data.pop("id", None)
    new_log = request.app.database["logs"].insert_one(log_data)
    created_log = LogOut(id=str(new_log.inserted_id), **log_data)
    return created_log

@router.get("/", response_description="List all logs", response_model=List[LogOut])
def list_logs(request: Request):
    logs_cursor = request.app.database["logs"].find(limit=100)
    logs = []

    for log in logs_cursor:
        logs.append(LogOut(
            id=str(log["_id"]),
            programName=log["programName"],
            log=log["log"]
        ))
    
    return logs

@router.get("/{id}", response_description="Get a single log by id", response_model=LogOut)
def find_log(id: str, request: Request):
    log = request.app.database["logs"].find_one({"_id": ObjectId(id)})
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return LogOut(
        id=str(log["_id"]),
        programName=log["programName"],
        log=log["log"]
    )
