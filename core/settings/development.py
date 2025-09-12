from core.configs.libs.cors import CorsConfig

from .base import BaseSettings

CORS_CONFIG = CorsConfig().for_development()


class DevelopmentSettings(BaseSettings):
    """
    Configurações de desenvolvimento.
    """

    DATABASE_ALIAS = "development"
    ENVIRONMENT_NAME = "Development"
    DEBUG = True

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    INSTALLED_APPS = [
        *BaseSettings.INSTALLED_APPS,
        "django_extensions",
        "debug_toolbar",
    ]

    MIDDLEWARE = [
        *BaseSettings.MIDDLEWARE,
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    # Debug Toolbar
    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost",
    ]

    ALLOW_ALL_ORIGINS = CORS_CONFIG["CORS_ALLOW_ALL_ORIGINS"]
