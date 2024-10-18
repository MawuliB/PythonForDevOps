import os

def update_env_file(key, value):
    try:
        with open(f'{os.getcwd()}/.env', 'r') as file:
            lines = file.readlines()

        with open(f'{os.getcwd()}/.env', 'w') as file:
            for line in lines:
                if line.startswith(key):
                    file.write(f'{key}={value}\n')
                else:
                    file.write(line)
    except Exception as e:
        print(e)

def add_key_to_env(key, value):
    try:
        with open(f'{os.getcwd()}/.env', 'a') as file:
            file.write(f'{key}={value}\n')
    except Exception as e:
        print(e)

def remove_key_from_env(key):
    try:
        with open(f'{os.getcwd()}/.env', 'r') as file:
            lines = file.readlines()

        with open(f'{os.getcwd()}/.env', 'w') as file:
            for line in lines:
                if not line.startswith(key):
                    file.write(line)
    except Exception as e:
        print(e)

def get_env_value(key):
    try:
        with open(f'{os.getcwd()}/.env', 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith(key):
                return line.split('=')[1].strip()
    except Exception as e:
        print(e)

add_key_to_env('CONFIG', 'development')
print(get_env_value('CONFIG'))
update_env_file('CONFIG', 'production')
print(get_env_value('CONFIG'))
remove_key_from_env('CONFIG')
print(get_env_value('CONFIG'))