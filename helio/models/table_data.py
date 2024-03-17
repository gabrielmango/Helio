"""Package for table dataclass."""

from dataclasses import dataclass


@dataclass
class TableData:
    """Class for table dataclass."""

    schema_name: str
    table_name: str
    table_comment: str
