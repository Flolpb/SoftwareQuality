def password(psd=None):
    if psd is not None:
        if len(psd) >= 10 and len(psd) <= 20:
            if '?' in psd or '@' in psd or '&' in psd or '$' in psd or '%' in psd or '#' in psd:
                if any(x.isupper() for x in psd) and any(x.islower() for x in psd):
                    if any(x.isdigit() for x in psd):
                        print("Your mdp is good")
                        return True
                    else:
                        print("pls a number")
                        return False
                else:
                    print("pls a uppercase and a lowercase")
                    return False
            else:
                print("pls a special caracter")
                return False
        else:
            print("pls a password ")
            return False
    else:
        print("rentrez un mot de passe svp")
        return False

def main():
    user_password = input("Saisissez un mot de passe:")
    if user_password is not None:
        password(user_password)



if __name__ == '__main__':
    main()