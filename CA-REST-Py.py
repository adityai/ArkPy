import requests
import json

#My PVWA URI
PVWA_WS_URI = "http://127.0.0.1/PasswordVault/WebServices"
#http://127.0.0.1/PasswordVault/WebServices/auth/CyberArk/CyberArkAuthenticationService.svc/logon
LOGON_AUTHENTICATION_URI = PVWA_WS_URI + "/auth/CyberArk/CyberArkAuthenticationService.svc/logon"
#http://127.0.0.1/PasswordVault/WebServices/auth/CyberArk/CyberArkAuthenticationService.svc/logoff
LOGOFF_AUTHENTICATION_URI = PVWA_WS_URI + "/auth/CyberArk/CyberArkAuthenticationService.svc/logoff"
#http://127.0.0.1/PasswordVault/WebServices/PIMServices.svc/User
LOGGED_ON_USER_DETAILS_URI = PVWA_WS_URI + "/PIMServices.svc/User"
#http://127.0.0.1/PasswordVault/WebServices/PIMServices.svc/Users
ADD_ACCOUNT_URI = PVWA_WS_URI + "/PIMServices.svc/Users"
#http://127.0.0.1/PasswordVault/WebServices/API.svc/Users/testTheRest
DELETE_USER_USERNAME = "testTheRest"
DELETE_USER_URI = PVWA_WS_URI + "/PIMServices.svc/Users/testTheRest"

connectionString = {'username': 'Administrator', 'password': 'Cyberark1'}

#LOGON Request - POST
logon = requests.post(url=LOGON_AUTHENTICATION_URI, json=connectionString)
json_response = logon.json()

#Storing the token from the JSON response into a variable
token = json_response['CyberArkLogonResult']
#Converting JSON to String
str_token = str(token)

if logon.status_code !=200:
    print("Connection failed with error code: " + str(logon.status_code))
    print(logon.headers)
    print(logon)
else:
    print("Connection was successful! Status code: " + str(logon.status_code) + "\n")
    print("[Logon] Headers: " + str(logon.headers))
    print("[Logon] JSON Response: " + str(json_response))

print("\n")

activate_user_headers = {'Content-Type': 'application/json', 'Authorization': str_token, 'Suspended':'false'}
activate_user = requests.get(url=LOGGED_ON_USER_DETAILS_URI, headers=activate_user_headers)
print("[Activate User Headers] Server-side headers (JSON): " + str(activate_user.headers))
print("[Activate Uesr Response] Server-side response (JSON): " + str(activate_user.json()))

print("\n")

#add_user_headers = {'Content-Type': 'application/json', 'Authorization': str_token}
#add_user_parameters = {'UserName':'testTheRest', 'InitialPassword':'CyberArk123', 'ChangePasswordOnTheNextLogon':False, 'UserTypeName':'EPVUser', 'Disabled':False}
#add_user = requests.post(url=ADD_ACCOUNT_URI, headers=add_user_headers, json=add_user_parameters)
#print("[Add Account Headers] Server-side headers (JSON): " + str(add_user.headers))
#print("[Add Account Response] Server-side response (JSON): " + str(add_user.json()))

#delete_user_headers = {'Authorization': str_token}
#delete_user = requests.delete(url=DELETE_USER_URI, headers=delete_user_headers)
#print("[Delete User Headers] Server-side headers (JSON): " + str(delete_user.headers))
#print("[Delete User Response] Server-side response (JSON): " + str(delete_user.json()))
