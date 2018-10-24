import requests

def get_location_info():
    return requests.get("http://api.ipstack.com/194.186.207.248?access_key=6bfdb21f3fc70bde8a4cfa2c83ebfd77").json()

if __name__=="__main__":
    print(get_location_info())