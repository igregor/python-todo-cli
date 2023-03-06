"""Database"""

import configparser
from pathlib import Path

from igregor_todo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path:
    """Return the current path to the todo database"""

    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)

    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    "Create todo db"
    try:
        db_path.write_text("[]") # Empty todo list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR