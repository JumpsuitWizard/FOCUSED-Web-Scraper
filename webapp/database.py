import psycopg2
import os
import json
from bom import Bom


def get_connection():
    try:
        connection = psycopg2.connect(
            host="postgres",
            user="postgres",
            password="admin",
            database="dependencies",
            port="5432"
        )
        print('Connected to database')
        return connection

    except (psycopg2.Error, Exception) as error:
        print("Error connecting to the PostgreSQL database:", error)
        return None


def get_all_dependencies():
    connection = get_connection()

    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM all_dependencies")
            rows = cursor.fetchall()

            # Create a BOM object
            bom = Bom()

            for row in rows:
                dependency_id = row[0]
                company_name = row[1]
                package_name = row[2]
                package_version = row[3]

                # Add each dependency as a component to the BOM
                bom.add_component("library", package_name,
                                  package_version, company_name)

            # Convert the BOM to a dictionary
            bom_dict = bom.to_dict()

    return bom_dict


def get_dependency_by_company(company_name):
    connection = get_connection()

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT package_name, package_version FROM all_dependencies WHERE company_name = %s",
                (company_name,)
            )
            rows = cursor.fetchall()

            bom = Bom()

            for row in rows:
                package_name = row[0]
                package_version = row[1]
                cursor.execute(
                    "SELECT company_name FROM all_dependencies WHERE LOWER(package_name) = LOWER(%s)",
                    (package_name,)
                )
                common_authors_set = set()  # Store unique authors for each package

                for author in cursor.fetchall():
                    author_name = author[0]
                    if author_name != company_name:
                        common_authors_set.add(author_name)

                # Convert the set of common authors to a list
                common_authors = list(common_authors_set)

                # Add each dependency as a component to the BOM
                bom.add_component_with_shared_authors(
                    "library", package_name, package_version, company_name, common_authors
                )

            # Convert the BOM to dictionary
            bom_dict = bom.to_dict()

    return bom_dict


def get_common_dependency(company, package_name):
    connection = get_connection()

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT company_name, package_version FROM all_dependencies WHERE package_name = %s",
                (package_name,)
            )
            rows = cursor.fetchall()

            # Create a Bom instance
            bom = Bom()

            for row in rows:
                company_name = row[0]
                package_version = row[1]
                if company_name == company:
                    continue

                # Add the component to the Bom
                bom.add_component("library", package_name,
                                  package_version, company_name)

            # Convert the Bom to a dictionary
            bom_dict = bom.to_dict()

    return bom_dict


def get_list_dependencies(package_name):
    connection = get_connection()

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT company_name, package_version FROM all_dependencies WHERE package_name = %s",
                (package_name,)
            )
            rows = cursor.fetchall()

            bom = Bom()

            response_data = []
            for row in rows:
                company_name = row[0]
                package_version = row[1]
                # Add the component to the Bom
                bom.add_component("library", package_name,
                                  package_version, company_name)
            # Convert the Bom to a dictionary
            bom_dict = bom.to_dict()

    return bom_dict
