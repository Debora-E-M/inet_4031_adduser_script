#!/usr/bin/python3

# INET 4031 - Lab 8 Part 2 (Dry-Run Version)
# Debora Mekonen
#
# This version allows interactive dry-run mode.
# User can choose whether to execute system commands
# or only print what would have executed.

import os
import re
import sys


def main():

    # Ask user if they want dry-run mode
    mode = input("Run in dry-run mode? (Y/N): ").strip().upper()

    dry_run = (mode == "Y")

    if dry_run:
        print("\n*** Running in DRY-RUN mode ***\n")
    else:
        print("\n*** Running in NORMAL mode ***\n")

    for line in sys.stdin:

        # Skip comment lines
        if re.match("^#", line):
            if dry_run:
                print("Skipping comment line.")
            continue

        fields = line.strip().split(':')

        # Check for proper format
        if len(fields) != 5:
            if dry_run:
                print("Error: Invalid line format (expected 5 fields).")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # ---- Create user ----
        create_cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        print("==> Creating account for %s..." % username)

        if dry_run:
            print("Would run:", create_cmd)
        else:
            os.system(create_cmd)

        # ---- Set password ----
        passwd_cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        print("==> Setting password for %s..." % username)

        if dry_run:
            print("Would run:", passwd_cmd)
        else:
            os.system(passwd_cmd)

        # ---- Assign groups ----
        for group in groups:

            if group == '-':
                if dry_run:
                    print("Skipping group assignment ('-' found).")
                continue

            group_cmd = "/usr/sbin/adduser %s %s" % (username, group)

            print("==> Assigning %s to group %s..." % (username, group))

            if dry_run:
                print("Would run:", group_cmd)
            else:
                os.system(group_cmd)


if __name__ == '__main__':
    main()
