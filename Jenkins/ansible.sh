#! /bin/bash
cd practicalproject
echo ${PATH}
ansible-playbook -i inventory playbook.yaml
