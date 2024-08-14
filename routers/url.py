from fastapi import APIRouter, status
from schemas.url import CreateUrlModel
from controller.url import create_url_object
from controller.crud.url import UrlCrud
from controller.validators.url import UrlValidator
from database.session import session
from starlette.responses import RedirectResponse

router = APIRouter()
url_crud = UrlCrud()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_url_alias(url_data: CreateUrlModel):
    url_data = dict(url_data)
    UrlValidator(url_data)
    url = create_url_object(url_data)
    return await url_crud.create_url(session, url)

@router.get('/{url_alias}', status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirect_url(url_alias: str):
    url = await url_crud.get_url_by_alias(session, url_alias)
    url = url.url
    return RedirectResponse(url)