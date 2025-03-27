# resources/secrets_manager.py
import pandas as pd

def get_raw_data(session, region):
    sm_client = session.client('secretsmanager', region_name=region)
    # Secrets Manager는 list_secrets() 호출
    response = sm_client.list_secrets()
    return response

def get_filtered_data(raw_data):
    rows = []
    for secret in raw_data.get('SecretList', []):
        row = {
            'Name': secret.get('Name'),
            'ARN': secret.get('ARN'),
            'Description': secret.get('Description'),
            'LastChangedDate': str(secret.get('LastChangedDate'))
        }
        rows.append(row)
    return pd.DataFrame(rows)
