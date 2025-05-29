"""
Elasticsearch Client Example - Demonstrating connection to Elasticsearch

This example shows how to connect to an Elasticsearch instance and list all indices.
"""
from elasticsearch import Elasticsearch


def list_elasticsearch_indices(host, username, password):
    """
    Connect to Elasticsearch and list all indices.
    
    Args:
        host (str): Elasticsearch host URL
        username (str): Username for authentication
        password (str): Password for authentication
        
    Returns:
        list: List of index names
    """
    # Create Elasticsearch client
    es = Elasticsearch(
        [host],
        basic_auth=(username, password),
        verify_certs=False,  # Note: In production, verify_certs should be True
    )
    
    # Get all indices
    indices = es.indices.get_alias(index="*")
    return list(indices.keys())


if __name__ == "__main__":
    # Replace with your actual credentials
    host = "https://elasticsearch.example.com:443"
    username = "elastic"
    password = "<your_password>"  # In production, use environment variables or a secure vault
    
    try:
        indices = list_elasticsearch_indices(host, username, password)
        print(f"Found {len(indices)} indices:")
        for index_name in indices:
            print(f"- {index_name}")
    except Exception as e:
        print(f"Error connecting to Elasticsearch: {e}")
