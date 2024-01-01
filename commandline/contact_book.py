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
from datetime import datetime


class ContactBook():

    # add arguments for creating, update & deleting contacts
    def get_arguments(self):
        parser = argparse.ArgumentParser(
            prog="ContactBook",
            description="Software to manage Contacts",
        )
        parser.add_argument(
            "operation",
            choices=["create", "update", "delete", "search", "backup"],
            help="Specify what kind of operation you wish to do: CRUD/SEARCH/BACKUP"
        )

        parser.add_argument("-n", "--name", type=str, required=False)
        parser.add_argument("-e", "--email", type=str, required=False, default="")
        parser.add_argument("-a", "--address", type=str, required=False, default="")
        parser.add_argument("-p", "--phone", type=int, required=False, default=0)
        args = parser.parse_args()
        return args


    # function for CRUD operations
    def contact_book_create(self):
        query = f"INSERT INTO CONTACT (NAME,EMAIL,ADDRESS,PHONE) \
            VALUES ('{self.details['name']}','{self.details['email']}','{self.details['address']}',{self.details['phone']})"
        self.conn.execute(query)
        self.conn.commit()
        print(self.conn.total_changes)


    def contact_book_update(self):
        # search for contact from DB
        query_output = self.contact_book_search()
        if len(query_output) > 1:
            print("Error: More than 1 Contact returned. Need more info to update contact.")
            sys.exit(1)

        check_update = input("If you wish to update Contact, type Y/N : ")
        if check_update != "Y":
            sys.exit(0)

        print("Click Enter without typing if you wish keep previous value in the field.")
        name = input("Name: ")
        if name is None:
            name = self.details["name"]
        email = input("Email: ")
        if email is None:
            email = self.details["email"]
        phone = input("Phone: ")
        if phone is None:
            phone = self.details["phone"]
        else:
            try:
                phone = int(phone)
            except ValueError:
                print("Invalid integer!")
                sys.exit(1)
        address = input("Address: ")

        query = f"UPDATE CONTACT set NAME = '{name}', EMAIL = '{email}', PHONE = {phone}, ADDRESS = '{address}';"
        self.conn.execute(query)
        self.conn.commit()
        print(self.conn.total_changes)


    def contact_book_delete(self):
        query_output = self.contact_book_search()
        print_contact(query_output)

        delete_status = input("Do you wish to delete these contacts: Y/N ? ")
        if delete_status != "Y":
            sys.exit(1)

        queries = []
        for contact in query_output:
            queries.append(f"DELETE FROM CONTACT WHERE ID = {contact[0]};")

        for query in queries:
            self.conn.execute(query)
            self.conn.commit()
            print(self.conn.total_changes)


    # function for Search operations
    def contact_book_search(self):
        query = f"SELECT * FROM CONTACT WHERE NAME = '{self.details['name']}'"

        for key, val in self.details.items():
            if key != "name" and val not in ["", 0]:
                query += f" AND {key.upper()}"
                if type(val) == str:
                    query += f" = '{val}'"
                else:
                    query += f" = {val}"

        print(query + ";")

        cursor = self.conn.execute(query)
        return cursor.fetchall()


    def print_contact(self, query_output):
        for contact in query_output:
            print(f"ID: {contact[0]}")
            print(f"Name: {contact[1]}")
            print(f"Email: {contact[2]}")
            print(f"Phone: {contact[3]}")
            print(f"Address: {contact[4]}")


    # connect to DB
    def db_connection(self):
        self.conn = sqlite3.connect("contact_book.db")
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS CONTACT
            (ID     INTEGER PRIMARY KEY,
            NAME    TEXT    NOT NULL,
            EMAIL   TEXT,
            PHONE   INT,
            ADDRESS CHAR(50))
            """
        )
        self.conn.commit()

    def progress(self, status, remaining, total):
        print(f'Copied {total-remaining} of {total} pages...')


    def take_db_back(self):
        time_now = datetime.now().strftime("%Y-%m-%d")
        backup_name = f"./backup_book_{time_now}.db"
        print(backup_name)
        dest = sqlite3.connect(backup_name)
        with dest:
            self.conn.backup(dest, progress=self.progress)
        dest.close()


    def main(self):
        arguments = self.get_arguments()
        # print(f"Operation Type: {arguments}")

        self.details = {
            "name": arguments.name,
            "email": arguments.email,
            "address": arguments.address,
            "phone": arguments.phone,
        }

        self.db_connection()

        if arguments.operation == "create":
            self.contact_book_create()
        elif arguments.operation == "update":
            self.contact_book_update()
        elif arguments.operation == "delete":
            self.contact_book_delete()
        elif arguments.operation == "backup":
            self.take_db_back()
        else:
            query_output = self.contact_book_search()
            self.print_contact(query_output)


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.main()
