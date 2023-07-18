import configparser
from suds.client import Client

config = configparser.ConfigParser()
config.read('./application.ini')
wsdl = config.get('classclimate', 'soap.wsdl')
print(wsdl)

client = Client(url=wsdl)
endpoint = config.get('classclimate', 'soap.url')
client.options.location = endpoint
print(client)

username = config.get('classclimate', 'soap.user')
password = config.get('classclimate', 'soap.pass')
ticket = client.service.RequestTicket(Login=username, Password=password)
auth = client.factory.create('Header')
auth.Ticket = ticket
client.set_options(soapheaders=auth)

# Call the SOAP methods
try:

    # Call the GetAllPeriods method
    periods = client.service.GetAllPeriods()

    # Print the result
    print(periods)

except Exception as e:
    print('An error occurred:', e)
