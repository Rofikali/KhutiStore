import requests

url = "http://127.0.0.1:8000/api/porducts/"
params = {"limit": 3}
all_results = []

r = requests.get(url, params=params, auth=("admin", "admin"))
# data = r.json()['results'][0]['name']
one_data = r.json()[0]["product_detail_url"]
# print(requests.get(url=one_data))
# print(one_data)
# all_results

q = requests.get(one_data)
# print(type(q))
a = q.json()
# print(a)
for i in a.items():
    print(i('0'))
    if i == "id":
        print("id is there")
    # else:
    #     print('id is not there ')


# print(a["brand"]["name"], a["category"]["name"])

# while url:
#     r = requests.get(url, params=params)
#     data = r.json()
#     print(data)
#     # all_results.extend(data.get("results", []))

# # Get the next page URL
# url = data.get("next")
# params = {}  # Clear params since 'next' already contains them

# Print or process all results
# for item in all_results:
#     print(item)
