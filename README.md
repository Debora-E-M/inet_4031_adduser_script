Program Description

This program automates the process of creating Linux user accounts and assigning them to groups using a Python script. Instead of manually running commands for each user, the script reads from an input file and performs all steps automatically. This saves time and reduces errors when creating multiple users.

Program Operation

The script reads from a file called create-users.input, where each line represents a user. For each valid line, the script:

Creates the user account
Sets the password
Assigns the user to groups

The program can run in two modes:

Dry-run mode → prints what would happen without making changes
Normal mode → actually creates users and assigns groups
Input File Format

Each line in the input file must follow this format:

username:password:last:first:groups
Lines starting with # are ignored
Use - if no groups are needed
Invalid lines are skipped
Running the Program

First make the script executable:

chmod +x create-users2.py

Then run:

sudo ./create-users2.py < create-users.input

The < symbol passes the input file into the script.

Dry-Run Mode

When running the script, you will be prompted to choose dry-run mode.

Y → shows commands without executing them
N → runs commands and creates users

Dry-run mode is useful for testing before making real changes.
