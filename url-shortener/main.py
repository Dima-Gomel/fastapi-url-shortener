from typing import Annotated
from fastapi import (
    FastAPI,
    Request,
    status,
    HTTPException,
    Depends,
)
from fastapi.responses import (
    RedirectResponse,
)
from schemas.short_url import ShortUrl
from schemas.film_library import Movie


app = FastAPI(
    title="URL Shortener",
)


@app.get("/")
def read_root(
    request: Request,
    name: str = "World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello {name}",
        "docs": str(docs_url),
    }


SHORT_URLS = [
    ShortUrl(
        target_url="https://www.example.com",
        slug="example",
    ),
    ShortUrl(
        target_url="https://www.google.com",
        slug="search",
    ),
]


@app.get(
    "/short-urls/",
    response_model=list[ShortUrl],
)
def read_short_url_list():
    return SHORT_URLS


def prefetch_short_url(
    slug: str,
) -> ShortUrl:
    url: ShortUrl | None = next(
        (url for url in SHORT_URLS if url.slug == slug),
        None,
    )
    if url:
        return url
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"URL {slug!r} not found",
    )


@app.get("/r/{slug}")
@app.get("/r/{slug}/")
def redirect_short_url(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
):
    return RedirectResponse(
        url=url.target_url,
    )


@app.get(
    "/short_urls/{slug}/",
    response_model=ShortUrl,
)
def read_short_url_details(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
) -> ShortUrl:
    return url


MOVIES = [
    Movie(
        id=1,
        title="Москва слезам не верит",
        year=1979,
        description="Москва, 1950-е годы. Три молодые провинциалки приезжают в Москву в поисках того,"
        "что ищут люди во всех столицах мира — любви, счастья и достатка. Антонина выходит замуж,"
        "растит детей, любит мужа. Людмиле Москва представляется лотереей,"
        "в которой она должна выиграть свое особенное счастье. Катерина же отчаянно влюбляется,"
        "но избранник ее оставляет. Однако она не опускает руки, в одиночку растит дочь и к тому же"
        "успевает делать блестящую карьеру. В 40 лет судьба дарит ей неожиданную встречу.",
        genre="драма, комедия",
    ),
    Movie(
        id=2,
        title="Живая сталь",
        year=2011,
        description="События фильма происходят в будущем, где бокс запрещен за негуманностью и заменен боями"
        "2000-фунтовых роботов, управляемых людьми. Бывший боксер, а теперь промоутер,"
        "переметнувшийся в Робобокс, решает, что наконец нашел своего чемпиона, когда ему попадается"
        "выбракованный, но очень способный робот. Одновременно на жизненном пути героя возникает"
        "11-летний парень, оказывающийся его сыном. И по мере того, как машина пробивает свой путь"
        "к вершине, обретшие друг друга отец и сын учатся дружить.",
        genre="научно-фантастическая семейная драма",
    ),
    Movie(
        id=3,
        title="Великий уравнитель",
        year=2014,
        description="Бывший агент ЦРУ, пожилой афроамериканец Роберт Макколл, решил начать жизнь заново,"
        "оставить непростое прошлое и смотреть в будущее, как и обещал покойной жене. Он уже нашёл обычную"
        "работу продавца в магазине. Однажды Макколл вступается за юную проститутку Тери,"
        "с которой болтал в местной закусочной и которая находится под контролем русской мафии."
        "Макколл прекращает свою добровольную отставку и начинает самостоятельные поиски правосудия. Все,"
        "кто страдает от криминальных авторитетов, коррумпированных чиновников и не может найти помощи "
        "у государства, находят помощь в лице Макколла. Он поможет. Потому что он — великий уравнитель.",
        genre="боевик-триллер",
    ),
]
