import json
import requests

def main():
    url = "https://testapp1030.herokuapp.com"
    query = {
        'method': 'POST',
        'id': "sununu",
        'pass': 'aaa'
        }
    print("--------- sign up ------------")
    print(url+"/signup")
    r = requests.post(url+"/signup",query)
    print(r.json())
    #print(json.dumps(r.json(),indent=2,))
    print("done")
    print("--------------user information ---------")
    user_id = "kaito"
    password = "kaikaipoteto"
    header = {
        'method': 'GET',
        "Authorization":"kaito:kaikaipoteto-"
        }

    r = requests.get(url+"/users/"+user_id,headers=header)
    print(r)
    print(json.dumps(r.json(),indent=2)) 
    
if __name__ == "__main__":
    main()