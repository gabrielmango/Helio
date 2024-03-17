"""Package for table handling."""

from models.table_data import TableData


class TableHandler:
    """Class for handling tables."""

    def __init__(self, schema: str, name: str, comment: str) -> TableData:
        """Starts the class when instantiating."""
        self.schema_name = schema
        self.table_name = name
        self.table_comment = comment

    def get_table(self):
        """Returns the table associated."""
        return TableData(self.schema_name, self.table_name, self.table_comment)
