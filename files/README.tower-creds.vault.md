# Structure of tower-creds.vault

tower_host: "<tower hostname/dns/ip>"
tower_username: "username"
tower_password: "username's password

job_templates:
  deploy_exam:
    name: "job_template_name"
    id: "1"
    endpoint: "https://hostname/api/v2/job_templates/1/launch/"
  postconfig:
    name: "job_template_name"
    id: "2"
    endpoint: "https://hostname/api/v2/job_templates/2/launch/"
  waittime:
    name: "job_template_name"
    id: "3"
    endpoint: "https://hostname/api/v2/job_templates/3/launch/"
  scoring:
    name: "job_template_name"
    id: "4"
    endpoint: "https://hostname/api/v2/job_templates/4/launch/"

