import yaml

def get_secret(name, default=''):
    result = default

    try:
        stream = open('vault.yml', 'r')
        secrets = yaml.load(stream, Loader=yaml.FullLoader)
        result = secrets[name]

    except:
        print('Error in getting secrets')

    return result
