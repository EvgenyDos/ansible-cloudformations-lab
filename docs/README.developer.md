# Li9 Exam System

You are at a right place if you are a developer. Check the diagram [here](README.manager.md) to understand the workflow. 

There is too much to say about developing. Are you an Ansible, Ansible Tower guru, yes? You'll figure out what to do ;).



## How to test your task

1. Create a virtual machine running *CentOS 7*.
2. Use playbook `tests/test-task.yaml`:
   - Format: 
            
         ansible-playbook tests/test-task.yaml -e task_path=<path/to/task> -e target=myhost -t <action>
         
     where:
     - *path/to/task* is path to the task directory with files 
       (`description.yml`, `pre_config.yml`, `reset_config.yml`, `goss.yaml`)
     - *action* is a tag for Ansible, can be: `pre-config`, `do-task`, `do-goss` or `validate`, and `reset-config`.
     - *target* is a variable you can use to pass a host group or host from your inventory. 
       By default, the playbook expects *[target]* host group is being defined.
       
   - Example of configuring a target system:
   
         ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t pre-config
   
   - Example of configuring a target system:
   
         ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t do-task
         
   - Example of resetting a target system to the task's before do-task state:
   
         ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t reset-config
   
   - Example of run goss tests:
   
         ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t do-goss
         ansible-playbook tests/test-task.yaml -e task_path=../li9_exam_system/linux/attr/modify-file -t validate

## How to test rendering of an Exam

  To make testing easier, there is a playbook which helps to check what the system can see when an Exam is being prepared.

  Call this command to check what a message a candidate receives for a particular exam:

      ansible-playbook test-doc.yaml <-e exam=name>

  where:

  - `exam` tells which exam (subdirectory) located in the directory `/li9_exam_system` to test. Default value is **linux**.

  You can find a message which a candidate receives in subdirectory `~/tmp/final-mailbody.html"` on ansible controller. Look for a file `mail.html`.

