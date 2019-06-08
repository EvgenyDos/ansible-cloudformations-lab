# Li9 Test System. Documentation

This document is designed to help to use the **Li9 Test System**.

Primary audience includes managers and operators.


## Components

There are two components which included in the system:
- __Ansible Tower__ a management interface.
- __AWS (Amazon Web Services__ is a platform where exams are run.


## Exam Scenario

### A company needs to test knowledge of a student. 

There is a pictured workflow ![Ordering an exam](https://github.com/EvgenyDos/ansible-cloudformations-lab/blob/master/files/ExamWorkflow.svg)

And the same description:

* __manager__
  * goes to __Ansible Tower__ and initiate an exam for the _student_:
    - selects an exam of _linux_, _docker_, _ansible_
    - specifies the student's email
* __student__
  * receives a web link on a provided mailbox
  * when he/she get ready to start doing the exam, he/she presses the link
* __Ansible Tower__
  * deployes the exam environment:
    - creates a VM in AWS
    - configures it with the exam requirements
  * sends to the student email with details:
    - credentials for connecting to the provisioned VM
    - tasks which the student should do
  * waits for a while, usually one (1) hour
* __student__
  * gets the mail, reads the tasks, rules, requirements, etc given in the mail
  * does or does not do the exam (timer is running anywway)
* __Ansible Tower__
  * wait for time runnint out
  * disables access of the student to the VM
  * reboots the VM
  * runs a scoring process to evaluate the student's knowledge
  * destroys the VM
  * mails to the manager results including details and a student's score
  * mails to the student notification like *You'll be contacted soon*.
* __manager__
  * analyze the received information and do next actions which are out of scope of the **Exam System**.


