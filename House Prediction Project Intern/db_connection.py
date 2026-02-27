from sqlalchemy import create_engine
from urllib.parse import quote_plus
import config


def get_engine():
    """
    Creates reusable MySQL connection engine
    """

    # encode special characters like @ #
    password = quote_plus(config.DB_PASSWORD)

    engine = create_engine(
        f"mysql+mysqlconnector://"
        f"{config.DB_USER}:{password}"
        f"@{config.DB_HOST}/{config.DB_NAME}"
    )

    return engine