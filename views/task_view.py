from flask import Blueprint, request, redirect
from flask import render_template, g, Blueprint
from models.task import allClass, allClassDB

allClass_list_blueprint = Blueprint('allClass_list_blueprint', __name__)

@allClass_list_blueprint.route('/', methods=["GET"])
def index():
    database = allClassDB(g.mysql_db, g.mysql_cursor)
    class_list = database.select_all_class()
    return render_template('index.html', class_list=class_list)
