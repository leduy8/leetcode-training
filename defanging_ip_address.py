
# * https://leetcode.com/problems/defanging-an-ip-address/

def defang_ip_addr(address: str) -> str:
    return address.replace('.', '[.]')

print(defang_ip_addr('1.1.1.1'))