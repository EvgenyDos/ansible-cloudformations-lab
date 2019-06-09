# Li9 Exam System

You are at a right place if you are a developer. Check the diagram [here](README.manager.md) to understand the workflow. 

It is too much to say about developing. Are you an Ansible, Ansible Tower guru, yes? You'll figure out what to do ;).



## How to test your task

1. Create a virtual machine running *CentOS 7*.
2. Use playbook `tests/test-task.yaml:
     be redefining by using a variable *target*.
   - Format: `ansible-playbook tests/test-task.yaml -e task_path=<path/to/task> -e target=myhost -t <action>
     where:
     - *path/to/task* is path to the task directory with files 
       (`description.yml`, `pre_config.yml`, `reset_config.yml`, `goss.yaml`)
     - *action* is a tag for Ansible, can be: `pre-config`, `do-task`, `do-goss` or `validate`, and `reset-config`.
     - *target* is a variable you can use to pass a host group from your inventory. 
       By default, the playbook expects *[target]* host group is being defined.
   - Example of configuring a target system:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t pre-config`.
   - Example of configuring a target system:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t do-task`.
   - Example of resetting a target system to the initial state:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t reset-config`.
   - Example of run goss tests:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t do-goss`.
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t validate`.

