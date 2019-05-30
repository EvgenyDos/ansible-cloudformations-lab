
## An exam task's structure

A task is a directory with set of predefined files that should exist. There are the files:
- file `description.yml`:
  - text content should be written using **Markdown** structured language
  - is a YAML file which has following keys:
    - *title (mandatory)* - name of the task (one line text). This name is sent to a participant. 
      Don't use here *Markdown* tags
    - *description (mandatory)* - text of the task. Provide here all details needed to solve the task. 
      This description is sent to a participant
    - *explanation (optional)*  - technical details that exlains how the task works (only for managers). 
      Can be written in any form but using *Markdown* is prefferable
- file `pre_config.yml`:
  - is an Ansible playbook which deploys the task on an exam machine
- file `reset_config.yml`:
  - is an Ansible playbook which resets the task on an exam machine to an initial state.
    Saying other words, it rollbacks the changes made by `pre_config.yml` playbook
- file `do_task.yml`:
  - is an Ansible playbook which completes the task 100%
  - it is needed to automate testing other playbooks and `goss.yaml` configuration
- file `goss.yaml`:
  - is a configuration file for **Goss**, which checks how good the task is completed by a participant


### How to test your task

1. Create a virtual machine running *CentOS 7*.
2. Use playbook `tests/test-task.yaml`:
     be redefining by using a variable *target*.
   - Format: `ansible-playbook tests/test-task.yaml -e task_path=<path/to/task> -e target=myhost -t <action>
     where:
     - *path/to/task* is path to the task directory with files 
       (`description.yml`, `pre_config.yml`, `reset_config.yml`, `goss.yaml`)
     - *action* is a tag for Ansible, can be: `pre-config`, `do-task`, and `reset-config`.
     - *target* is a variable you can use to pass a host group from your inventory. 
       By default, the playbook expects *[target]* host group is being defined.
   - Example of configuring a target system:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t pre-config`.
   - Example of configuring a target system:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t do-task`.
   - Example of resetting a target system to the initial state:
     `ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t reset-config`.



