"""
Collection of functions to help establish the database
"""
import mysql.connector


# Connect to MySQL and the database
def connect_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"],
        database=config["DATABASE"]
    )
    return conn


# Setup for the Database
#   Will erase the database if it exists
def init_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"]
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {config['DATABASE']};")
    cursor.execute(f"CREATE DATABASE {config['DATABASE']};")
    cursor.execute(f"use {config['DATABASE']};")
    # All Classes
    cursor.execute(
        f""" 
        CREATE TABLE allClass
        (
            classID SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
            className VARCHAR(50),
            location VARCHAR(50),
            semester int,
            CONSTRAINT pk_classID PRIMARY KEY (classID)
        );
        """
    )
    cursor.close()
    conn.close()
