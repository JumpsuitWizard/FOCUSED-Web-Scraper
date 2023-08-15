from flask import Flask, request, jsonify
from flask_cors import CORS
from database import (
    get_all_dependencies,
    get_dependency_by_company,
    get_common_dependency,
    get_list_dependencies,
    get_package_count,
    get_all_packages,
    get_unique_package_count, 
    get_package_percentage_count
)
from urllib.parse import unquote


app = Flask(__name__)
CORS(app)


@app.get("/")
def get_main():
    return "Welcome to FOCUSED"


@app.get("/dependencies")
def get_all_dependencies_route():
    bom_dict = get_all_dependencies()
    return jsonify(bom_dict)


@app.route("/dependencies/company/<company_name>", methods=["GET"])
def get_dependency_by_company_route(company_name):
    bom_dict = get_dependency_by_company(company_name)
    return jsonify(bom_dict)


@app.route("/dependencies/<company>/<package_name>", methods=["GET"])
def get_common_dependency_route(company, package_name):
    bom_dict = get_common_dependency(company, package_name)
    return jsonify(bom_dict)


@app.route("/dependencies/package/<package_name>", methods=["GET"])
def get_list_dependencies_route(package_name):
    decoded_package_name = unquote(package_name)
    bom_dict = get_list_dependencies(decoded_package_name)
    return jsonify(bom_dict)

@app.route("/dependencies/packages", methods=["GET"])
def get_all_package_dependencies_route():
    bom_dict = get_all_packages()
    return jsonify(bom_dict)


@app.route("/dependencies/package/count", methods=["GET"])
def get_package_count_route():
    bom_dict = get_package_count()
    return jsonify(bom_dict)

@app.route("/dependencies/package/companies_with_max_unique_counts", methods=["GET"])
def get_unique_package_count_route():
    bom_dict = get_unique_package_count()
    return jsonify(bom_dict)

@app.route("/dependencies/package/package_percentage", methods=["GET"])
def get_package_percentage_route():
    bom_dict = get_package_percentage_count()
    return jsonify(bom_dict)