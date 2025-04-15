from fastapi import APIRouter

from .endpoints import reservation_router, table_router

main_router = APIRouter()


main_router.include_router(
    table_router, prefix="/tables", tags=["Tables"]
)
main_router.include_router(
    reservation_router, prefix="/reservations", tags=["Reservations"]
)
