import subprocess

# these file uses selenium
#  'meta_ray_ban.py', 'panapto.py', 'spaceti.py', 'giphy.py'

python_files = ['meta_ray_ban.py', 'panapto.py', 'spaceti.py', 'giphy.py',
                'slack.py', 'spotify.py', 'cisco.py', 'samsung_developers.py', 'porsche.py', 'discord.py', 'broadcom.py', 'confluent.py', 'adlock.py', 'apple_maps.py', 'bocada.py', 'bosch.py',
                'smartsheet.py', 'sparktrader.py', 'camunda.py', 'oracle_fusion.py', 'box.py', 'parasoft.py', 'clue_io.py', 'cognition.py', 'nvidia.py', 'shoott.py', 'genesis.py', 'veertu.py', 'parsec.py', 'flexera.py']


def execute_python_file(file_name):
    try:
        subprocess.run(["python3", file_name], check=True)
        print(f"{file_name} executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {file_name}: {e}")


if __name__ == "__main__":
    for file_name in python_files:
        execute_python_file(file_name)
    print("All the dependencies have been added successfully")
