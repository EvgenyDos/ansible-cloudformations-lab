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

"""

import os
import yaml
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
      path = '/'.join([ component for component in path.split('/') if len(component.strip()) > 0 ])
      curr_data = { 'topics': {}, 'rootpath': path }
      display.debug("Tasks lookup path: %s" % path)
      if os.path.exists(path) and os.path.isdir(path):
        for root, dirs, files in os.walk(path):

          if path == root[0:len(path)]:
            root = root[len(path):]
          else: continue

          if root.count('/') != 2: continue

          rootdir, topic, task_name = root.split('/')

          display.vvvv("Current Rootdir is {0}".format(topic))
    
          topic_data = { 'tasks': []}

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
          task_dir = '/'.join([ curr_data.get('rootpath'), topic_data.get('selected_task_path')])

          if kwargs.get('content', True):
            try:
              desc_content = {}
              with open('/'.join([ task_dir, 'description.yml' ])) as fd:
                desc_content = yaml.load( fd )
                if desc_content.get('title', None) and desc_content.get('description', None):
                  topic_data['selected_task_content'] = desc_content
            except:
              topic_data['selected_task_content'] = { 'title': '', 'description': '' }


        results.append( curr_data )
      else:
        raise AnsibleError("Cound not locate directory: %s" % path)
    return results

