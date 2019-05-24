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


The lookup plugin expect a directory structure like this.
Where "li9_exam_system" is a name of the plugin's first argument

li9_exam_system/linux/
    apache
        newnametask
            description dot yml
            goss dot yaml
            pre_config dot yml
        taskone
            description dot yml
            goss dot yaml
            pre_config dot yml
        tasktwo
            description dot yml
            goss dot yaml
            pre_config dot yml
    attr
        taskone
            description dot yml
            goss dot yaml
            pre_config dot yml
        tasktwo
            description dot yml
            goss dot yaml
            pre_config dot yml
...

Example of usage:

  - name: Get files info
    set_fact:
      files_info: "{{ lookup('listtasks', 'li9_exam_system/linux/', content=False) }}"

  - debug: var=files_info

The plugin will create a structure like below. The sections 'content' on the top and
'selected_task_content' are being filled with informaion from found description.yml files.
By default this feature is enabled, but could be disabled by specifying an argument
'content=False'

{
    "content": {
        "description": "",
        "ready": false,
        "title": ""
    },
    "rootpath": "li9_exam_system/linux",
    "topics": {
        "apache": {
            "selected_task_content": {
                "description": "",
                "ready": false,
                "title": ""
            },
            "selected_task_id": 1,
            "selected_task_name": "tasktwo",
            "selected_task_path": "apache/tasktwo",
            "tasks": [
                "newnametask",
                "tasktwo",
                "taskone"
            ]
        },
        "attr": {
            "selected_task_content": {
                "description": "",
                "ready": false,
                "title": ""
            },
            "selected_task_id": 1,
            "selected_task_name": "taskone",
            "selected_task_path": "attr/taskone",
            "tasks": [
                "tasktwo",
                "taskone"
            ]
        },
  ...
}
"""



import os
import yaml
import random
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()
random.seed()


def getDescription(base_dir, include=True):
  if not include: 
    result = { "title": "", "description": "", "ready": False }
  else:
    try:
      desc_content = {}
      with open('/'.join([base_dir, 'description.yml']), 'r') as fd:
        desc_content = yaml.load( fd )
        if desc_content.get('title', None) and desc_content.get('description', None):
          result = desc_content
          result['ready'] = True
    except Exception as err:
      raise AnsibleError("Getting description error: {0}, on directory: {1}".format(err, base_dir))
  return result


class LookupModule(LookupBase):

  def run(self, paths, variables=None, **kwargs):
    results = []

    for path in paths:
      path = '/'.join([ component for component in path.split('/') if len(component.strip()) > 0 ])
      curr_data = { 'topics': {}, 'rootpath': path }
      display.vvvv("Tasks lookup path: %s" % path)

      if os.path.exists(path) and os.path.isdir(path):
        for root, dirs, files in os.walk(path):
           
          for filename in files:
            if filename == 'description.yml':
              subpath = root[len(path)+1:]
              if subpath == "": # found root directory of an exam
                curr_data['content'] = getDescription(root, kwargs.get('content', True))
              elif subpath.count('/') == 1: # found a task within a topic
                topic_name, task_name = subpath.split('/')
                topic_data = curr_data['topics'].get(topic_name, { "tasks": []})
                curr_data['topics'][topic_name] = topic_data
                topic_data['tasks'].append( task_name )
        for topic in curr_data['topics'].keys():
          topic_data = curr_data['topics'].get(topic)
          generated_id = random.randint(0, len(topic_data.get('tasks'))-1)
          topic_data['selected_task_id'] = generated_id
          topic_data['selected_task_name'] = topic_data.get('tasks')[generated_id]
          topic_data['selected_task_path'] = "/".join([ topic, topic_data.get('selected_task_name')])
          
          topic_data['selected_task_content'] = getDescription(
            '/'.join([ curr_data.get('rootpath'), topic_data.get('selected_task_path')]),
            kwargs.get('content', True)
          )

        results.append(curr_data)
      else:
        raise AnsibleError("Cound not locate directory: %s" % path)
      return results
    pass


