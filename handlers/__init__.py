from .empty_handler import empty_handler_router
from .user_start import user_start_handler_router
from .admin_handlers import admin_handler_router
from .channel_handlers import chanel_handler_router


ROUTERS_MAIN = [
    user_start_handler_router,
    admin_handler_router,
    chanel_handler_router,
]

ROUTERS = ROUTERS_MAIN + [empty_handler_router]
