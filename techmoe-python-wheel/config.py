import yaml

# 填充默认设置
default_config = {
}

config = {}

def load(text):
    global config
    config = yaml.load(text)

def load_file(file_path):
    with open(file_path) as f:
        load(f.read())

def get(key, fallback=False):
    keys = key.split('.')

    if fallback == True:
        target = default_config
    else:
        target = config
    
    for k in keys:
        target = target.get(k)
    
    if target == None and not fallback == True:
        target = get(key, fallback=True)
    return target
