"""
data storage - sqllite3
contact creation, update & deletion
Search (re)
On-screen presentation

extra:
backup database (locally or to cloud)
Printing (pyPDF2)
Multiple Users
User levels
"""

# CLI tool to add, update & deletion of contacts
import sqlite3
import argparse
import sys


# add arguments for creating, update & deleting contacts
def get_arguments():
    parser = argparse.ArgumentParser(
        prog="ContactBook",
        description="Software to manage Contacts",
    )
    parser.add_argument(
        "operation",
        choices=["create", "update", "delete", "search"],
        help="Specify what kind of operation you wish to do: CRUD/SEARCH",
        required=True
    )

    parser.add_argument("-n", "--name", type=str, required=True)
    parser.add_argument("-e", "--email", type=str, required=False, default="")
    parser.add_argument("-a", "--address", type=str, required=False, default="")
    parser.add_argument("-p", "--phone", type=int, required=False, default=0)
    args = parser.parse_args()
    return args


# function for CRUD operations
def contact_book_create(dbconn, details):
    query = f"INSERT INTO CONTACT (NAME,EMAIL,ADDRESS,PHONE) \
        VALUES ('{details['name']}','{details['email']}','{details['address']}',{details['phone']})"
    dbconn.execute(query)
    dbconn.commit()
    print(dbconn.total_changes)


def contact_book_update(dbconn, details):
    # search for contact from DB
    query_output = contact_book_search(dbconn, details)
    if len(query_output) > 1:
        print("Error: More than 1 Contact returned. Need more info to update contact.")
        sys.exit(1)

    check_update = input("If you wish to update Contact, type Y/N : ")
    if check_update != "Y":
        sys.exit(0)

    print("Click Enter without typing if you wish keep previous value in the field.")
    name = input("Name: ")
    if name is None:
        name = details["name"]
    email = input("Email: ")
    if email is None:
        email = details["email"]
    phone = input("Phone: ")
    if phone is None:
        phone = details["phone"]
    else:
        try:
            phone = int(phone)
        except ValueError:
            print("Invalid integer!")
            sys.exit(1)
    address = input("Address: ")

    query = f"UPDATE CONTACT set NAME = '{name}', EMAIL = '{email}', PHONE = {phone}, ADDRESS = '{address}';"
    dbconn.execute(query)
    dbconn.commit()
    print(dbconn.total_changes)


def contact_book_delete(dbconn, details):
    query_output = contact_book_search(dbconn, details)
    print_contact(query_output)

    delete_status = input("Do you wish to delete these contacts: Y/N ? ")
    if delete_status != "Y":
        sys.exit(1)

    queries = []
    for contact in query_output:
        queries.append(f"DELETE FROM CONTACT WHERE ID = {contact[0]};")

    for query in queries:
        dbconn.execute(query)
        dbconn.commit()
        print(dbconn.total_changes)


# function for Search operations
def contact_book_search(dbconn, details):
    query = f"SELECT * FROM CONTACT WHERE NAME = '{details['name']}'"

    for key, val in details.items():
        if key != "name" and val not in ["", 0]:
            query += f" AND {key.upper()}"
            if type(val) == str:
                query += f" = '{val}'"
            else:
                query += f" = {val}"

    print(query + ";")

    cursor = dbconn.execute(query)
    return cursor.fetchall()


def print_contact(query_output):
    for contact in query_output:
        print(f"ID: {contact[0]}")
        print(f"Name: {contact[1]}")
        print(f"Email: {contact[2]}")
        print(f"Phone: {contact[3]}")
        print(f"Address: {contact[4]}")


# connect to DB
def db_connection():
    conn = sqlite3.connect("contact_book.db")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS CONTACT
        (ID     INTEGER PRIMARY KEY,
        NAME    TEXT    NOT NULL,
        EMAIL   TEXT,
        PHONE   INT,
        ADDRESS CHAR(50))
        """
    )
    conn.commit()
    return conn


def main():
    arguments = get_arguments()
    # print(f"Operation Type: {arguments}")

    details = {
        "name": arguments.name,
        "email": arguments.email,
        "address": arguments.address,
        "phone": arguments.phone,
    }

    dbconn = db_connection()

    if arguments.operation == "create":
        contact_book_create(dbconn, details)
    elif arguments.operation == "update":
        contact_book_update(dbconn, details)
    elif arguments.operation == "delete":
        contact_book_delete(dbconn, details)
    else:
        query_output = contact_book_search(dbconn, details)
        print_contact(query_output)


if __name__ == "__main__":
    main()
