import requests

URL= "HTTP://127.0.0.1:5001/users"

def deactivate_user(id):
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
    id = input ("Type in the user's ID: ")
    deactivate_user(id)