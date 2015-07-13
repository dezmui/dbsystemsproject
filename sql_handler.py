#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements and committing them to the database server
#######################################################################################################

import MySQLdb

#######################################################################################################

#Run sql queries and return result

def run_sql(sqlstatement):
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g13", "info20003g13_2014", "info20003g13", 3306)
    cursor = db.cursor()
    try:
        cursor.execute(sqlstatement)
        result = cursor.fetchall()
        db.close()
        return result
    except:
        return None

#######################################################################################################

#Run sql updates and commit, otherwise, rollback if error

def run_update(updateStatement):
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g13", "info20003g13_2014", "info20003g13", 3306)
    cursor = db.cursor()
    try:
        cursor.execute(updateStatement)
        db.commit()
    except:
        db.rollback()
    db.close()
    return

#######################################################################################################

#Run sql inserts and commit, otherwise, rollback if error

def run_insert(insertStatement):
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g13", "info20003g13_2014", "info20003g13", 3306)
    cursor = db.cursor()
    try:
        cursor.execute(insertStatement)
        cur_val = db.insert_id()
        db.commit()
        db.close()
        return cur_val
    except:
        db.rollback()
        return None

#######################################################################################################
    
#Run sql removes and commit, otherwise, rollback if error

def run_remove(removeStatement):
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g13", "info20003g13_2014", "info20003g13", 3306)
    cursor = db.cursor()
    try:
        cursor.execute(removeStatement)
        db.commit()
    except:
        db.rollback()
    db.close()
    return

#######################################################################################################

