import argparse, clipboard, hashlib
from passlib.hash import lmhash


def calculateLM(text):
    try:
        hashed = lmhash.hash("hello").upper()
        print("[+] The LM hash of '{0}' is: \n{1}\n".format(text, hashed))
        try:
            clipboard.copy(hashed)
            print("[+] Hash successfully copied to the clipboard")
        except:
            print("[!] Warning: Cannot access the clipboard")
    except:
        print("[-] Error: LM hash calculating is not supported")

def calculateNT(text):
    try:
        hashed = hashlib.new("md4", text.encode("utf-16le")).hexdigest().upper()
        print("[+] The NTLM hash of '{0}' is: \n{1}\n".format(text, hashed))
        try:
            clipboard.copy(hashed)
            print("[+] Hash successfully copied to the clipboard")
        except:
            print("[!] Warning: Cannot access the clipboard")
    except:
        print("[-] Error: NTLM hash calculating is not supported")
    
def main():
    parser = argparse.ArgumentParser("Simple Hash Calculator")
    parser.add_argument("-n", "--ntlm", help="Calculate NTLM hash", action="store_true")
    parser.add_argument("-l", "--lm", help="Calculate LM hash", action="store_true")
    parser.add_argument("-t", "--text", type=str, help="String to hash")
    
    args = parser.parse_args()

    if args.ntlm and args.lm:
        print("[-] Error: More than one algorithm specified")
        exit(0)
    
    if args.ntlm:
        if args.text:
            calculateNT(args.text)
        else:
            print("[-] Error: No text specified")
    elif args.lm:
        if args.text:
            calculateLM(args.text)
        else:
            print("[-] Error: No text specified")
    else:
        print("[-] Error: No algorithm specified")
    
if __name__ == "__main__":
    main()
