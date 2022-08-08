import requests

URL= "HTTP://127.0.0.1:5001/vehicles"


def create_vehicle(vehicle_model, vehicle_type, vehicle_year, vehicle_brand, vehicle_transmission, id_user):
    vehicle = {
        "vehicle_model": vehicle_model,
        "vehicle_type": vehicle_type,
        "vehicle_year": vehicle_year,
        "vehicle_brand": vehicle_brand,
        "vehicle_transmission": vehicle_transmission,
        "id_user": id_user
    }
    response = requests.post(URL, json=vehicle)
    if response.status_code == 201:
        print(
            "Successfully created new record, Got: %s"
            % response.json().get("message")
        )
    else:
        print(
            "Something went wrong while trying to register a new vehicle."
        )

if __name__ == "__main__":
    vmodel = input("Type in the model of the vehicle: ")
    vtype = input ("Type in the type of vehicle: ")
    vyear = input ("Type in the vehicle's year of release: ")
    vbrand = input ("Type in the brand of the vehicle: ")
    vtransmission = input ("Type in the transmission mode: ")
    uid = input ("And finally, type in the owner's ID number: ")
    create_vehicle(vmodel, vtype, vyear, vbrand, vtransmission, uid)