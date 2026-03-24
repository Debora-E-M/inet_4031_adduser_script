#!/usr/bin/python3

# INET 4031
# Debora Mekonen
#
# This script reads user information from standard input and:
# 1. Creates a Linux user account
# 2. Sets the user password
# 3. Adds the user to any specified groups
#
# Expected input format:
# username:password:last:first:group1,group2

import os   # allows execution of Linux system commands
import re   # used to detect comment lines in the input file
import sys  # used to read input from stdin


def main():

    # Process each line from the input file
    for line in sys.stdin:

        # Ignore lines that begin with "#" (these are comments in the input file)
        if re.match("^#", line):
            continue

        # Remove trailing newline and split the line into fields
        fields = line.strip().split(':')

        # Ensure the line contains exactly 5 fields before processing
        # This prevents errors from malformed input lines
        if len(fields) != 5:
            continue

        # Assign variables from the input fields
        username = fields[0]
        password = fields[1]

        # Format the full name for the GECOS field (used in /etc/passwd)
        # Format: "First Last,,,"
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Groups may be separated by commas, so convert to a list
        groups = fields[4].split(',')

        # ---- Create the user account ----
        print("==> Creating account for %s..." % username)

        create_cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(create_cmd)

        # ---- Set the user password ----
        print("==> Setting the password for %s..." % username)

        passwd_cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(passwd_cmd)

        # ---- Assign user to additional groups ----
        for group in groups:

            # A "-" means no additional group should be assigned
            if group == '-':
                continue

            print("==> Assigning %s to the %s group..." % (username, group))

            group_cmd = "/usr/sbin/adduser %s %s" % (username, group)
            os.system(group_cmd)


if __name__ == '__main__':
    main()
