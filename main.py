import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code)

# instead of writing exception for every status code its good to insatll requests module from pypi.org and raise exception.
# if response.status_code == 404:
#     raise Exception('That resource does not exists.')
# elif response.status_code == 401:
#     raise Exception('You are not allowed to access the status code.')


response.raise_for_status()
data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
ISS_position = (longitude, latitude)
print(ISS_position)