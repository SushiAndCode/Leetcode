import pandas as pd

# Creating the Trips DataFrame
trips_data = [
    {'id': 1, 'client_id': 1, 'driver_id': 10, 'city_id': 1, 'status': 'completed', 'request_at': '2013-10-01'},
    {'id': 2, 'client_id': 2, 'driver_id': 11, 'city_id': 1, 'status': 'cancelled_by_driver', 'request_at': '2013-10-01'},
    {'id': 3, 'client_id': 3, 'driver_id': 12, 'city_id': 6, 'status': 'completed', 'request_at': '2013-10-01'},
    {'id': 4, 'client_id': 4, 'driver_id': 13, 'city_id': 6, 'status': 'cancelled_by_client', 'request_at': '2013-10-01'},
    {'id': 5, 'client_id': 1, 'driver_id': 10, 'city_id': 1, 'status': 'completed', 'request_at': '2013-10-02'},
    {'id': 6, 'client_id': 2, 'driver_id': 11, 'city_id': 6, 'status': 'completed', 'request_at': '2013-10-02'},
    {'id': 7, 'client_id': 3, 'driver_id': 12, 'city_id': 6, 'status': 'completed', 'request_at': '2013-10-02'},
    {'id': 8, 'client_id': 2, 'driver_id': 12, 'city_id': 12, 'status': 'completed', 'request_at': '2013-10-03'},
    {'id': 9, 'client_id': 3, 'driver_id': 10, 'city_id': 12, 'status': 'completed', 'request_at': '2013-10-03'},
    {'id': 10, 'client_id': 4, 'driver_id': 13, 'city_id': 12, 'status': 'cancelled_by_driver', 'request_at': '2013-10-03'}
]

trips = pd.DataFrame(trips_data)# Creating the Users DataFrame
users_data = [
    {'users_id': 1, 'banned': 'No', 'role': 'client'},
    {'users_id': 2, 'banned': 'Yes', 'role': 'client'},
    {'users_id': 3, 'banned': 'No', 'role': 'client'},
    {'users_id': 4, 'banned': 'No', 'role': 'client'},
    {'users_id': 10, 'banned': 'No', 'role': 'driver'},
    {'users_id': 11, 'banned': 'No', 'role': 'driver'},
    {'users_id': 12, 'banned': 'No', 'role': 'driver'},
    {'users_id': 13, 'banned': 'No', 'role': 'driver'}
]
users = pd.DataFrame(users_data)

users = users[users["banned"] == "No"]

trips = trips[(trips["client_id"].isin(users["users_id"])) & (trips["driver_id"].isin(users["users_id"]))]

trips["num_canc"] = trips.apply(lambda x: 1 if "cancelled" in x["status"] else 0, axis = 1)

trips["num_canc"] = trips.groupby(by = "request_at")["num_canc"].cumsum()

trips["tot_num"] = trips.groupby(by = "request_at").cumcount() + 1

result =trips.groupby("request_at")[["num_canc", "tot_num"]].apply(lambda x: x["num_canc"].max() / x["tot_num"].max()).reset_index(name = "Cancellation Rate")
print(result.rename(columns = {"request_at":"Day"}))
