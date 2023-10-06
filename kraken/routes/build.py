from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Request

router = APIRouter(prefix="/build", tags=["build"])


@router.get("/")
async def get_info(request: Request):
    raise HTTPException(status_code=HTTPStatus.OK)
