print("=== BULK PASSWORD AUDITOR(File Mode) ===")
print("Loading Leaked passwords from file...\n")

try:
    with open('leaked_passwords.txt', 'r') as file:
        passwords = [line.strip() for line in file if line.strip()]
    print(f"Loaded {len(passwords)} passwords.\n")
except FileNotFoundError:
    print("File not found, make sure it's in the same folder as the script")
    exit()

print ("scanning multi password...\n")
weak_count = 0

for password in passwords:
    print(f"Checking: {password}")
    length = len(password)

    if length >=8 and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
        print("This is very strong password")
    else:
        print("WEAK")
        weak_count +=1
        if length <8:
            print("   Too short")
        if not any(char.isupper() for char in password):
            print("   No Uppder Case")
        if not any(char.islower() for char in password):
            print("   No Lower Case")
    print("----")
print(f"\n AUDIT COMPLETE : {weak_count} WEAK PASSWORDS FOUND")

print("\n AUDIT COMPLETE")
print(f"    Total passwords : {len(passwords)}")
print(f"    Weaked passwords : {weak_count}")
print(f"    strong passwords : {len(passwords) - weak_count}")

with open('audit_report', 'w') as report:
    report.write("AUDIT COMPLET")
    report.write(f"    Total passwords : {len(passwords)}")
    report.write(f"    Weaked passwords : {weak_count}")
    report.write(f"    strong passwords : {len(passwords) - weak_count}")
print("\n Report saved to : audit_report.txt")
