from fastapi import (
    APIRouter,
    status,
    Depends,
)


from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
    ShortUrlRead,
)
from .details_views import router as detail_router
from ..crud import storage
from ..dependacies import save_storage_state

router = APIRouter(
    prefix="/short-urls",
    tags=["Short URLs"],
    dependencies=[Depends(save_storage_state)],
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
    return storage.create(short_url_create)
