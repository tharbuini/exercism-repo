def transform(legacy_data):
    
    data = dict()
    for key, value in legacy_data.items():
        for item in value:
            data.update({item.lower():key})

    return data
