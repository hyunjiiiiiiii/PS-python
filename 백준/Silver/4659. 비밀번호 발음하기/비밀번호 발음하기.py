# 비밀번호 발음하기

while True:
    password = list(input())

    if ''.join(password) == "end":
        break

    mo = ["a", "e", "i", "o", "u"]

    jamo = []
    for i in password:
        if i in mo:
            jamo.append("mo")
        else:
            jamo.append("ja")


    if not any (v in password for v in mo):
        print(f"<{''.join(password)}> is not acceptable.")
    else:
        idx = 1
        while idx < len(password):

            # 2번 모음 3개 연속, 자음 3개 연속
            if idx > 1 and (jamo[idx] == jamo[idx-1] == jamo[idx-2]):
                print(f"<{''.join(password)}> is not acceptable.")
                break
            else:
                if password[idx] == password[idx-1] and (password[idx] != "e" and password[idx] != "o"):
                    print(f"<{''.join(password)}> is not acceptable.")
                    break
            idx += 1
        
        if idx == len(password):
            print(f"<{''.join((password))}> is acceptable.")
