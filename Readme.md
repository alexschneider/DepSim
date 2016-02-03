# Distributed Deployment Simulator

This project is developed using Python 3 using PyParsing and SimPy.

#Install and Run Instructions
To run on Unix (Linux/Mac):
```Shell
$ pip3 install virtualenv
$ python3 -m virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ python depsim.py
```

To run on Windows:

```Shell
$ py -3 -m pip install virtualenv
$ py -3 -m virtualenv venv
$ venv/Scripts/activate.bat
$ pip install -r requirements.txt
$ python depsim.py
```

# Sample Model
```

```
# EBNF for Model

```
name = all_characters;
model = {region | upgrade_domain | rollout_plan};

region = 'region', name, '{', region_spec, '}';
region_spec = {{region_attribute} | {datacenter}};
region_attribute = ('located in', all_characters);

datacenter = [number], 'datacenter' | 'datacenters', name, '{', datacenter_spec, '}';
datacenter_spec = {{datacenter_attribute} | {cluster}};

cluster = [number], 'cluster' | 'clusters', name, '{', cluster_spec '}';
cluster_spec = {{cluster_attribute} | {rack}};

rack = [number], 'rack' | 'racks', name, '{', rack_spec '}';
rack_spec = {{rack_attribute} | {server}};

server = [number], 'server' | 'servers', name, '{', server_spec, '}';
server_spec = {{server_attribute}};

upgrade_domain = (*How do I define this?*)

rollout_plan = '{', {parallelize_plan | }, '}'
```
