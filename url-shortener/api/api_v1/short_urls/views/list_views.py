from fastapi import (
    APIRouter,
    status,
    Depends,
    HTTPException,
)

from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
    ShortUrlRead,
)

from .details_views import router as detail_router
from api.api_v1.short_urls.crud import storage
from api.api_v1.short_urls.dependacies import (
    api_token_or_url_required_for_unsafe_methods,
)


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
)
def create_short_url(
    short_url_create: ShortUrlCreate,
) -> ShortUrl:
    if not storage.get_by_slug(short_url_create.slug):
        return storage.create(short_url_create)

    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"Short URL with slug={short_url_create.slug!r} already exists.",
    )
