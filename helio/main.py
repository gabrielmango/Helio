"""Package for main function."""

from tasks.table_handler import TableHandler


def main():
    """Main function that runs the project."""
    print('HELIO: Lets start!')
    print('----------------------------------------------------------------')
    print('HELIO: What is the name of the schema ?')
    schema = input('YOU: ')
    print('----------------------------------------------------------------')
    print('HELIO: What is the name of the table?')
    table = input('YOU: ')
    print('----------------------------------------------------------------')
    print('HELIO: What is the comment of the table?')
    comment = input('YOU: ')
    print('----------------------------------------------------------------')
    table_handler = TableHandler(schema, table, comment).get_table()

    print(table_handler)


if __name__ == '__main__':
    main()
