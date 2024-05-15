import boto3

def extract_text_from_document(file):
    # Initialize Textract client
    textract_client = boto3.client('textract')

    # Read file as bytes
    file_bytes = file.read()

    # Call Textract API
    response = textract_client.detect_document_text(
        Document={'Bytes': file_bytes}
    )

    # Extract text
    extracted_text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + '\n'

    return extracted_text
