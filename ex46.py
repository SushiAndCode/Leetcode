import pandas as pd
import statistics

data = {
    "requester_id": [1, 1, 2, 3],
    "accepter_id": [2, 3, 3, 4],
    "accept_date": ["2016/06/03", "2016/06/08", "2016/06/08", "2016/06/09"]
}

df = pd.DataFrame(data)

res = pd.concat([df["requester_id"], df["accepter_id"]]).tolist()
r = statistics.mode(res)
print(res)
#print(pd.DataFrame({"id" : [r], "num" : [res.count(r)]}))