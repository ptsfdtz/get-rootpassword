import hashlib
import argparse

salt = "d44fb0960aa0-a5e6-4a30-250f-6d2df50a"

def get_salt():
    return '-'.join(reversed(salt.split("-")))

def generate_md5(sn):
    passwd = sn + get_salt()
    m = hashlib.md5(passwd.encode())
    return m.hexdigest()[:8]

def main():
    parser = argparse.ArgumentParser(description='Generate MD5 hash from SN code.')
    parser.add_argument('sn', nargs='?', type=str, help='The SN code to hash.')
    args = parser.parse_args()

    if args.sn:
        result = generate_md5(args.sn)
        print(f"MD5 hash for SN '{args.sn}': {result}")
    else:
        sn = input("请输入SN码: ")
        result = generate_md5(sn)
        print(f"{result}")

if __name__ == '__main__':
    main()
