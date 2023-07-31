from ldap3 import Server, Connection, MODIFY_ADD, MODIFY_DELETE
from configparser import ConfigParser
import csv


def get_emails(remove_st) -> list:
    # Read the email list from the CSV file
    csv_file = 'emails.csv'
    emails = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                emails.append(row[0].replace(remove_st, ''))
    return emails


def get_members(group_dn, conn):
    # Retrieve all members of the AD group
    conn.search(group_dn, '(objectClass=*)', attributes=['member'])
    members = [member_dn.split(',')[0].split(
        '=')[1] for member_dn in conn.entries[0].member]

    return members


def bulk_modify_members(operation, to_remove, conn, group_dn, organization_unit, domain_component):
    if not to_remove:
        return

    remove_result = conn.modify(
        group_dn, {'member': [(operation, f'CN={dn},{organization_unit},{domain_component}') for dn in to_remove]})

    if remove_result:
        print(f"{operation} {len(to_remove)}")
    else:
        # This user failed to be modified
        if len(to_remove) == 1:
            return

        # Divide the remaining list by half
        half_index = len(to_remove) // 2
        first_half = to_remove[:half_index]
        second_helf = to_remove[half_index:]

        # Recursive call for each half
        bulk_modify_members(operation, first_half, conn,
                            group_dn, organization_unit, domain_component)
        bulk_modify_members(operation, second_helf, conn,
                            group_dn, organization_unit, domain_component)


def main():

    print("Starting AD group add/remove process")

    # Read the AD properties from the properties file
    config = ConfigParser()
    config.read('ad_properties.ini')
    ad_server = config.get('AD', 'ad_server')
    username = config.get('AD', 'username')
    password = config.get('AD', 'password')
    group_dn = config.get('AD', 'group_dn')
    domain_component = config.get('AD', 'domain_component')
    organization_unit = config.get('AD', 'organization_unit')
    email_relace_str = config.get('AD', 'email_relace_str')
    
    emails = get_emails(email_relace_str)

    server = Server(ad_server)

    with Connection(server, user=username, password=password) as conn:

        current_members = get_members(group_dn, conn)
        print(f"Current member: {len(current_members)} group: {group_dn}")

        # Compare the group members with the email list and identify additions and removals
        to_add = [email for email in emails if email not in current_members]
        bulk_modify_members(MODIFY_ADD, to_add, conn,
                            group_dn, organization_unit, domain_component)

        # Compare the group members with the email list to remove
        to_remove = [email for email in current_members if email not in emails]
        bulk_modify_members(MODIFY_DELETE, to_remove, conn,
                            group_dn, organization_unit, domain_component)

        print("=== Status Report ===")
        status_members = get_members(group_dn, conn)
        added_users = [email for email in to_add if email in status_members]
        failed_to_add_users = [
            email for email in to_add if email not in status_members]
        removed_users = [
            email for email in to_remove if email not in status_members]
        print(f"Added {len(added_users)}")
        if failed_to_add_users:
            print(f"Failed to add {failed_to_add_users}")
        print(f"Removed {len(removed_users)}")
        print(f"Status member: {len(status_members)} group: {group_dn}")
        print("=====================")

    print("Ending AD group add/remove process")


if __name__ == "__main__":
    main()
