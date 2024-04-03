from datetime import datetime

# Class to model Task objects
class allClass:
    def __init__(self, className, location, semester):
        self._class = className
        self._location = location
        self._semester = semester
   
    @property
    def className(self):
        return self.className
    
    @className.setter
    def className(self, new_className):
        self._className = new_className

    @property
    def location(self):
        return (self._location)
    
    @location.setter
    def location(self, new_location):
        self._location = new_location

    @property
    def semester(self):
        return self.semester
    
    @semester.setter
    def semester(self, new_semester):
        self._semester = new_semester



# Class to support reading/writing class objects with the database
class allClassDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    

    def select_all_class(self):
        select_all_query = """
            SELECT * from allClass;
        """
        self._cursor.execute(select_all_query)
        return self._cursor.fetchall()


    def select_all_class_by_className(self, className):
        select_class_by_className = """
            SELECT * from allClass WHERE className LIKE %s;
        """
        self._cursor.execute(select_class_by_className, (f"%{className}%",))
        return self._cursor.fetchall()
    

    def select_class_by_id(self, classID):
        select_class_by_id = """
                SELECT * from allClass WHERE classID = %s;
        """
        self._cursor.execute(select_class_by_id, (classID,))
        return self._cursor.fetchall()


    def insert_class(self, allClass):
        insert_query = """
            INSERT INTO allClass (className, location, semester)
            VALUES (%s, %s, %d);
        """

        self._cursor.execute(insert_query, (allClass.className, allClass.location, allClass.semester))
        self._cursor.execute("SELECT LAST_INSERT_ID() classID")
        classID = self._cursor.fetchone()
        self._db_conn.commit()
        return classID


    def update_class(self, classID, new_class):
        update_query = """
            UPDATE allCLass
            SET className=%s
            WHERE classID=%s;
        """
        self._cursor.execute(update_query, (new_class.className, classID))
        self._db_conn.commit()

    def delete_task_by_id(self, classID):
        delete_query = """
            DELETE from allClass
            WHERE classID=%s;
        """
        self._cursor.execute(delete_query, (classID,))
        self._db_conn.commit()
