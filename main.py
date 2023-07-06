import subprocess

# these file uses selenium
#  'meta_ray_ban.py', 'panapto.py',

python_files = [
    'slack.py', 'spotify.py', 'cisco.py', 'samsung_developers.py', 'porsche.py', 'discord.py', 'broadcom.py', 'confluent.py', 'adlock.py', 'apple_maps.py', 'bocada.py', 'bosch.py',
    'smartsheet.py', 'sparktrader.py', 'camunda.py', 'oracle_fusion.py', 'box.py', 'parasoft.py', 'clue_io.py', 'cognition.py', 'nvidia.py', 'shoott.py', 'genesis.py', 'veertu.py']


def execute_python_file(file_name):
    subprocess.run(["python3", file_name])


if __name__ == "__main__":
    for file_name in python_files:
        execute_python_file(file_name)
        print(f"{file_name} executed successfully")
    print("All the dependencies have been added successfully")
