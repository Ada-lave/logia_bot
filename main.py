from dadata import Dadata
token = "1b42dfdd178348cc680ec9cd4f8413232a912eb1"
secret = "7ce9c45fb9b297b2241386e6fdac525896dbe8a7"
dadata = Dadata(token, secret)
result = dadata.clean("address", "москва сухонская 11")
# print(result)