from fastapi import (
    APIRouter,
    status,
)
from pydantic import json

from api.api_v1.short_urls.crud import storage, ShortUrlsStorage

from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
    ShortUrlRead,
)
from .details_views import router as detail_router

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLs"],
)
router.include_router(detail_router)


@router.get(
    "/",
    response_model=list[ShortUrlRead],
)
def read_short_urls_list() -> list[ShortUrl]:
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrlRead,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url_create: ShortUrlCreate,
) -> ShortUrl:
    short_url = storage.create(short_url_create)
    return short_url
