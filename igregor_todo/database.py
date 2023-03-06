"""Database"""

import configparser
import json
from pathlib import Path
from typing import Any, Dict, List, NamedTuple

from igregor_todo import DB_WRITE_ERROR, SUCCESS, DB_READ_ERROR, JSON_ERROR

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

class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int

class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self.__db_path__ = db_path

    def read_todos(self) -> DBResponse:
        try:
            with self.__db_path__.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError: # Catch wrong JSON format
                    return DBResponse([], JSON_ERROR)
        except OSError: # Catch file IO problems
            return DBResponse([], DB_READ_ERROR)
    
    def write_todos(self, todo_list: List[Dict[str, Any]]) -> DBResponse:
        try: 
            with self.__db_path__.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
        except OSError: # Catch file IO problems
            return DBResponse([], DB_WRITE_ERROR)