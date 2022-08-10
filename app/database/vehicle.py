from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        vehicle = {
            "id": result[0],
            "vehicle_model": result[1],
            "vehicle_type": result[2],
            "vehicle_year": result[3],
            "vehicle_transmission": result[4],
            "id_user": result[5]
        }
        out.append(vehicle)
    return out

def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle", ()
    )
    results=cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?",
        (pk, )
    )
    results=cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def insert (vehicle_dict):
    value_tuple = (
        vehicle_dict.get("vehicle_model"),
        vehicle_dict.get("vehicle_type"),
        vehicle_dict.get("vehicle_year"),
        vehicle_dict.get("vehicle_brand"),
        vehicle_dict.get("vehicle_transmission"),
        vehicle_dict.get("id_user")
    )
    statement = """
            INSERT INTO vehicle (
                vehicle_model,
                vehicle_type,
                vehicle_year,
                vehicle_brand,
                vehicle_transmission,
                id_user
            ) VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor = get_db()
    cursor.execute (statement, value_tuple)
    cursor.commit()
    cursor.close()

def update (pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("vehicle_model"),
        vehicle_data.get("vehicle_type"),
        vehicle_data.get("vehicle_year"),
        vehicle_data.get("vehicle_type"),
        vehicle_data.get("vehicle_brand"),
        vehicle_data.get("vehicle_transmission"),
        vehicle_data.get("id_user"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET vehicle_model=?,
        vehicle_type=?,
        vehicle_year=?,
        vehicle_brand=?,
        vehicle_transmission=?,
        id_user=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute (statement, value_tuple)
    cursor.commit()
    cursor.close()

def deactivate_vehicle(pk):
    cursor = get_db()
    cursor.execute ("DELETE FROM vehicle WHERE id_vehicle=? ", (pk, ))
    cursor.commit()
    cursor.close()
