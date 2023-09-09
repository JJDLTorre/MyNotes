import user_auth
import user_client
import configparser
import logging
import O365
from Logging import setup_logging_and_console


setup_logging_and_console(__file__, logging)


def get_config():
    try:
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        return config
    except Exception as e:
        logging.exception(e)
        exit(1)


if __name__ == '__main__':
    logging.info("Starging get_sharepoint_info()")
    config = get_config()

    # Replace these values with your SharePoint site URL, username, and password
    sharepoint_site = config['MS_INFO']['sharepoint_site_url']

    client_id = config['MS_INFO']['client_id']
    client_secrete = config['MS_INFO']['client_secrete']
    tenant_id = config['MS_INFO']['tenant_id']
    auth_flow_type = config['MS_INFO']['auth_flow_type']

    credential = user_client.ClientCredentials(
        client_id, client_secrete, tenant_id, auth_flow_type)
    token_path = config['MS_INFO']['token_path']
    token = O365.FileSystemTokenBackend(token_path)

    user = user_client.UserClient(credential, token)

    if not user.is_authenticated:
        ms_user = config['MS_INFO']['ms_user']
        ms_password = config['MS_INFO']['ms_password']
        user.authenticate(None, user_auth.headless(ms_user, ms_password))
    sharepoint = user.sharepoint()

    sharepoint_site = sharepoint.get_site(
        config['MS_INFO']['ms_site_id'])

    print(vars(sharepoint_site))

    logging.info("Ending get_sharepoint_info()")
