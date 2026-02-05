from fastapi import (
    APIRouter,
    Depends,
    status,
)

from api.api_v1.short_urls.crud import storage
from api.api_v1.short_urls.dependacies import (
    api_token_or_url_required_for_unsafe_methods,
)
from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
    ShortUrlRead,
)

from .details_views import router as detail_router

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLs"],
    dependencies=[
        Depends(api_token_or_url_required_for_unsafe_methods),
    ],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthenticated. Only for unsafe methods.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid API token",
                    },
                },
            },
        },
    },
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
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "A short url with such by slug already exists.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Short URL with slug='name' already exists.",
                    },
                },
            },
        },
    },
)
def create_short_url(
    short_url_create: ShortUrlCreate,
) -> ShortUrl:
    return storage.create_or_raise_if_exists(short_url_create)
