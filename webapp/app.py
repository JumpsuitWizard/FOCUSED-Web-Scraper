from flask import Flask, request, jsonify
from database import (
    get_all_dependencies,
    get_dependency_by_company,
    get_common_dependency,
    get_list_dependencies,
)

app = Flask(__name__)


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
    bom_dict = get_list_dependencies(package_name)
    return jsonify(bom_dict)
