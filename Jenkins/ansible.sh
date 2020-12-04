#! /bin/bash
cd practicalproject
echo ${PATH}
/home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml
