import requests

URL= "HTTP://127.0.0.1:5000/vehicles"

def deactivate_vehicle(id):
    url=URL+"/"+id
    response = requests.delete(url)
    if response.status_code == 204:
        print (
            "Done"
        )
    else:
        print( "Something went wrong"
        )

if __name__ == "__main__":
    deactivate_vehicle(id)