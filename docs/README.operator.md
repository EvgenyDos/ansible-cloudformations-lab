# Li9 Test System. Documentation

Read further if you need to develop more exams and/or tasks.

## Workspace

Base directory for all exams is `/li9_exam_system` on the top level. Currently it has these subdirectories:


    li9_exam_system/
    ├── ansible
    ├── docker
    └── linux


These subdirectories are called **exams**. When you assign an `linux` exam to a person, the tasks from subdirectory `linux` are taken.


### Exams

As already said, currently there are three exams `linux`, `docker`, and `ansible`. Actually there is only one a fully developed exam is `linux`.

If you'd like to rename existed or create new exams (subdirectories) those changes should be reflected in __Ansible Tower__.

Let's dive into an exam structure. Each exam has to follow the structure like this.

    li9_exam_system/linux/
    ├── apache
    ├── attr
    ├── common_bootstrap.yml
    ├── description.yml
    ├── fs
    ├── lvm
    ├── nfs
    ├── script
    ├── shelltricks
    ├── ssh
    ├── texttools
    └── users


#### Special Files

There are two important files.

 - `common_bootstrap.yml` is an _Ansible_ playbook. It includes ansible tasks for bootstrapping an exam system. In most cases the steps are being repeated for every exam.
 - `description.yml` is a _YAML_ file. It has two mandatory keys:
   * `title` is a title for the exam, e.g. **Linux Basics Exam**.
   * `description` gives the exam specific information.

`description`should be written in _Markdown_ format. Title should be just a plain text. It worths to note that `description` does not exlpain everything about the exam. It includes only a part specific for the particular exam because remain text is taken from file`templates/mail-body.md.j2`. So just keep in mind that content of the both files should be connected.

Both `title` and `description` are rendered into an email that is sent to a student. Therefore be so much accurate in the content as possible.


Other files in the exam directory are ignored.


#### Subdirectories or Topics

The exam directory must include subdirectories. The `linux` exam has following subdirectories


    li9_exam_system/linux/
    ├── apache
    ├── attr
    ├── fs
    ├── lvm
    ├── nfs
    ├── script
    ├── shelltricks
    ├── ssh
    ├── texttools
    └── users

In this context the subdirectories are called **Topics**. An exam has so many tasks for a student as many topics are defined on this level.


Let's see the **users** topic.

    li9_exam_system/linux/users/
    ├── basic-attributes
    └── users-and-groups

This topic includes two subdirectories `basic-attributes` and `users-and-groups`. These subdirectories are called **tasks**.


Develop as many tasks as possible for each of topics. In that case every student gets its own set of tasks. If there is only one task, all students will get the same task. Otherwise, a task for every student will be selected randomly from the bunch of the available tasks.


#### A Task

A task a subdirectory one level below of a topic and follows the next structure.

    li9_exam_system/linux/users/basic-attributes/
    ├── description.yml
    ├── do_task.yml
    ├── goss.yaml
    ├── pre_config.yml
    └── reset_config.yml

- a _YAML_ file `description.yml` follows the same structure as on an exam level. It also includes `title` and `description` keys and should include specific for the particular task. This information is also included into email that sent to a student.
- an _Ansible_ playbook `pre_config.yml` which used to prepare an exam host for a student. For example, some package should be installed for doing the task.
- an _Ansible_ playbook `do_task.yml` is used to do the task. It would do the tasks like a student but it has to do all 100% correctly.
- an _Ansible_ playbook `reset_config.yml` is used to take reverse steps of `do_task.yml`.
- a _Goss_ configuration file `goss.yaml`.

A task has to contain mandatory files `description.yml`, `pre_config.yml`, and `goss.yaml`. Other two playbooks `do_task.yml` and `reset_config.yml` are needed for testing purposes when you write `goss.yaml` file.

Write these two optional playbooks, this helps to automate testing of `goss.yaml` configuration. Check the [developer doc](README.developer.md) how to test goss files.


*Note: The only file `goss.yaml` should be ended as `.yaml`. Other files should be ended as `.yml`.*
