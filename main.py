import uuid
import pexpect


def fuck():
    phone = '18260168335'
    uid = str(uuid.uuid4()).replace('-', '')
    check = 0
    for i in range(3):
        check = check + ord(phone[i]) + ord(uid[i])
    str_check = (check * 177 + 5166) % 10000
    account = uid + str(str_check) + "01" + phone
    print(account)
    return account


def main():
    pppd = pexpect.spawn("pppd call pppoe")
    i = pppd.expect(["username"])
    pppd.sendline
    return


if __name__ == '__main__':
    fuck()
