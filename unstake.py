from urllib.request import urlopen, Request
import json, datetime

now = datetime.datetime.now()
current_time = (now.strftime('%m-%d-%Y %I:%M:%S %p'))
outfile_name = (now.strftime('logs/MTV_SAVE_%m-%d-%Y_%I:%M:%S_%p'))
print("Loading Addresses.....")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
ids_url = "https://e.mtv.ac/stake/tops?pageNum=1&pageSize=10000"
list_req = Request(url=ids_url, headers=headers)
list_read = urlopen(list_req).read()
list_load = json.loads(list_read)

unstake_total = 0
current_id = 0
total_ids = (list_load["total"])

print("Scraping Data....")
while current_id < total_ids:
    user = (list_load["data"][current_id]["id"])
    current_id = current_id + 1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = "https://e.mtv.ac/account/get?address=" + user
    req = Request(url=reg_url, headers=headers)
    page = urlopen(req).read()
    y = json.loads(page)
    currentUnstaked = (y["stake"]["withdrawPending"])
    unstake_total = int(unstake_total) + int(currentUnstaked)
    save = open(outfile_name, 'w+')
    save_info = save.write("MTV currently being unstaked: {0} As of {1}\n".format(str(unstake_total), str(current_time)))
    print(f'{current_id}/{total_ids}-{user}:{currentUnstaked}')

if len(str(unstake_total)) == 27:
    unstake_total = str(unstake_total)[:9]
    print("\nMTV currently being unstaked: {:,}".format(int(unstake_total)))
    print(f'Data recorded at: {current_time}\n')
else:
    unstake_total = str(unstake_total)[:8]
    print("\nMTV currently being unstaked: {:,}".format(int(unstake_total)))
    print(f'Data recorded at: {current_time}\n')