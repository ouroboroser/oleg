def add(result, type, token, location):

    result.append({
        'type': type,
        'token': token,
        'location': location,
    })
    return result

locations = {
    'persons': 'root -> left',
    'wishes': 'root -> right',
    'act': 'root -> right -> left -> left',
    'execution object': 'root -> right -> left -> left -> left -> left',
    'execution object optional': 'root -> right -> left -> left -> left -> left -> left',
    'articles': 'root -> right -> right -> left',
    'rooms': 'root -> right -> left -> left -> left -> left'
}