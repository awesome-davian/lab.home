import re
import json
from datetime import datetime

from fabric import Connection


def load_config(file):
    config = json.load(open(file, "rt"))

    user_id = config['USER_INFO']['id']
    user_pw = config['USER_INFO']['password']

    server_list = config['SERVER_LIST']

    return user_id, user_pw, server_list


class ServerInfo(object):
    command = "nvidia-smi --query-gpu=timestamp,name,driver_version,temperature.gpu,memory.total,memory.free,memory.used,utilization.gpu --format=csv"

    def __init__(self, host, user_id, user_pw):
        self.connection = Connection(host, user_id)
        self.connection.connect_kwargs.password = user_pw
        self.host = host
        self.info = []

        self.update()

    def update(self):
        output = self.connection.run(self.command)

        # TODO: exit code exception or no gpu exception
        self._parse(output.stdout)

    def _parse(self, gpu_stats: str):
        self.info = []
        for line in gpu_stats.split("\n"):
            if line.startswith("20"):
                stat_list = line.split(", ")
                timestamp = stat_list[0]
                name = stat_list[1]
                driver_version = stat_list[2]
                temperature = int(re.findall(r"([\d]+)", stat_list[3])[0])
                total_memory = int(re.findall(r"([\d]+)", stat_list[4])[0])
                free_memory = int(re.findall(r"([\d]+)", stat_list[5])[0])
                used_memory = int(re.findall(r"([\d]+)", stat_list[6])[0])
                utilization = int(re.findall(r"([\d]+)", stat_list[7])[0])

                memory_percentage = int(used_memory / total_memory * 100)
                color_class = {
                    'success': False,
                    'normal': False,
                    'warning': False,
                    'danger': False
                }
                if memory_percentage < 30:
                    color_class['success'] = True
                elif memory_percentage < 50:
                    color_class['normal'] = True
                elif memory_percentage < 70:
                    color_class['warning'] = True
                else:
                    color_class['danger'] = True

                self.info.append({
                    'timestamp': timestamp,
                    'name': name,
                    'driver_version': driver_version,
                    'temperature': temperature,
                    'total_memory': total_memory,
                    'free_memory': free_memory,
                    'used_memory': used_memory,
                    'memory_percentage': memory_percentage,
                    'color_class': color_class,
                    'utilization': utilization
                })

    @property
    def json(self):
        return {"host": self.host, "info": self.info}

    def __str__(self):
        return self.host, str(self.info)


if __name__ == '__main__':
    user_id, user_pw, server_list = load_config("server_info.json")
    servers = [ServerInfo(host, user_id, user_pw) for host in server_list]

    for server in servers:
        print(server.host)
        print(server.info)
        print("=======================")
