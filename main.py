import json
from zoomus import ZoomClient


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    client = ZoomClient('API_KEY', 'API_SECRET')

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)

    print(user_list_response)
    print(user_list)
