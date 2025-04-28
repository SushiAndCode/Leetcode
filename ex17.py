import pandas as pd


employee = pd.DataFrame({
        "id": [101, 102, 103, 104, 105, 106],
        "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
        "department": ["A", "A", "A", "A", "A", "B"],
        "managerId": [None, 101, 101, 101, 101, 101]
    })
    
# Creating the second DataFrame with different managerIds
df2 = pd.DataFrame({
        "id": [101, 102, 103, 104, 105, 106],
        "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
        "department": ["A", "A", "A", "A", "A", "B"],
        "managerId": [None, 101, 102, 103, 104, 105]  # Different manager IDs
    })


data = {
    "id": list(range(100)),
    "name": [
        "qnDL", "H4yq", "wWAV", "vAUb", "Hujf", "J400", "UMHO", "1gOg", "0cYl", "DtWG", "eyXo", "Honp", "Ipkr", "h23t", "CGAH", "PsOK", "SAUF", "Msms", "A3ea", "iTWd", "e64F", "SPLQ", "12GB", "8d8F", "x8D2", "daW9", "Hhzb", "Ed2J", "mbGb", "tGod", "bJkK", "I9Zp", "oREm", "dqz6", "ZfXN", "eWU3", "lirh", "3asM", "22GY", "QLcM", "VjRR", "80kO", "LLYZ", "jJ3g", "gr3s", "aY69", "NWZQ", "MjBT", "77wf", "zqlY", "VvOc", "4pWH", "IOkX", "ponb", "hUUC", "iAZA", "rMjY", "HIwL", "qOQU", "WGCl", "hZtj", "KHN3", "96Sp", "MgKR", "sdWY", "hVYY", "Q4B3", "z6lt", "BdZn", "3YHT", "WqJb", "fMkc", "wJG6", "bE1z", "kpbq", "rpJJ", "5GoX", "14aW", "w9uQ", "gujV", "BEtQ", "B9Li", "rL0o", "UytZ", "52md", "49gg", "H7q2", "SdJa", "aY00", "0zhn", "lwlK", "IrcP", "yNkE", "0RT7", "fgzl", "0Gg7", "4acG", "Oztr", "Y7O2", "0lKb"
    ],
    "department": ["A"] * 100,
    "managerId": [
        636, 251, 551, 550, 344, 947, 939, 507, 154, 822, 72, 91, 134, 916, 732, 759, 529, 197, 177, 857, 899, 480, 38, 928, 627, 57, 864, 425, 59, 882,
        351, 467, 333, 484, 265, 5, 225, 354, 177, 939, 694, 800, 773, 643, 323, 267, 332, 20, 340, 143, 604, 5, 364, 360, 117, 266, 462, 78, 323, 477, 219,
        139, 177, 243, 570, 903, 124, 239, 538, 467, 499, 832, 510, 593, 479, 343, 933, 930, 350, 428, 598, 232, 647, 95, 187, 459, 504, 834, 773, 903, 60,
        442, 907, 660, 146, 264, 13, 656, 713, 984
    ]
}

employee = pd.DataFrame(data)

count = employee.value_counts(subset = "managerId").reset_index()
managers = count[(count["managerId"].isin(employee["id"])) & (count["count"] >= 2)]
managers = employee[employee["id"].isin(managers["managerId"])]
print(pd.DataFrame(managers["name"]))