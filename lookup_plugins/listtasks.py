# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type



DOCUMENTATION = """
    listtasks: file
      author: Dmitrii Mostovshchikov <dmadm2008@gmail.com>
      version_added: "0.1"
      short_description: Gets list of tasks in a directory
      description:
        - Reads the specified directory and returns a random task from this directory
      options:
        path: 
          description: path to the directories to read
          required: true


The plugin designed to read the directory structure like this

li9_exam_system/
├── apache
│   ├── task0
│   │   ├── goss.yaml
│   │   └── pre_config.yml
│   ├── task1
│   │   ├── goss.yaml
│   │   └── pre_config.yml
│   └── task2
│       ├── goss.yaml
│       └── pre_config.yml
├── attr
│   ├── task0
│   │   ├── goss.yaml
│   │   └── pre_config.yml
│   ├── task1
│   │   ├── goss.yaml
│   │   └── pre_config.yml
│   └── task2
│       ├── goss.yaml
│       └── pre_config.yml

and produce output like this
{
        "rootpath": "li9_exam_system/",
        "topics": {
            "apache": {
                "selected_task_id": 1,
                "selected_task_name": "task1",
                "selected_task_path": "apache/task1",
                "tasks": [
                    "task0",
                    "task1",
                    "task2"
                ]
            },
            "attr": {
                "selected_task_id": 2,
                "selected_task_name": "task2",
                "selected_task_path": "attr/task2",
                "tasks": [
                    "task0",
                    "task1",
                    "task2"
                ]
            },
  ...
}
"""

import os
import random
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()
random.seed()


class LookupModule(LookupBase):

  def run(self, paths, variables=None, **kwargs):
    results = []
    for path in paths:
      curr_data = { 'topics': {}, 'rootpath': path }
      display.debug("Tasks lookup path: %s" % path)
      if os.path.exists(path) and os.path.isdir(path):
        for root, dirs, files in os.walk(path):
          while root.startswith('/'): root = root[1:]
          while root.endswith('/'): root = root[:-1]
          if root.count('/') != 2: continue
          local_path = root[len(path)+1:] # removing also trailing slash "/"
         
          rootdir, topic, task_name = root.split('/')

          topic_data = { 'tasks': [ ]}
          if topic in curr_data['topics'].keys():
            curr_data['topics'][topic]['tasks'].append(task_name)
          else:
            curr_data['topics'][topic] = { "tasks": [ task_name ]}


        for topic in curr_data['topics'].keys():
          topic_data = curr_data['topics'][topic]
          generated_id = random.randint(0, len(topic_data['tasks'])-1)
          topic_data['selected_task_id'] = generated_id
          topic_data['selected_task_name'] = topic_data['tasks'][generated_id]
          topic_data['selected_task_path'] = "/".join([ topic, topic_data['selected_task_name'] ])

        results.append( curr_data )
      else:
        raise AnsibleError("Cound not locate directory: %s" % path)
    return results

