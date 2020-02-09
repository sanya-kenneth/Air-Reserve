from typing import List


def find_missing_fields(request, required_fields: List[str]):
    """
    Validates request to ensure that required fields are included
    """
    for key in required_fields:
        if key not in request.keys():
            return {'error': f'{key} field is required'}
    return {'error': 'None'}
