#### What is Terraform?
- An `infrastructure as code` tool
- Automate and manage your:
  - infrastructure
  - platform
  - services that run on that platform

#### Other infrastructure as code tools
- Ansible
- Chef
- AWS CloudFormation

#### How does Terraform work?
![img](../images/terraform_1.PNG)
![img](../images/terraform_2.PNG)
![img](../images/terraform_3.PNG)
![img](../images/terraform_4.PNG)
![img](../images/terraform_5.PNG)

#### Terraform with azure
- `az login` ==> login to azure
- `az account show` ==> show account details
- `terraform fmt` ==> formats code
- `terraform init` ==> initializes the terraform backend
- `terraform apply -auto-approve` ==> apply without getting asked to confirm
- `terraform state list` ==> show list of the resources we have
- `terraform state show <resource>` ==> show specific resource state
- `terraform show` ==> show all of the state
- `terraform apply -destroy` or `terraform destroy` ==> destroy resources

##### Links
- Azure-citadel-terraform (very good): https://www.azurecitadel.com/terraform/
- Awesome-terraform-overview: https://www.trackawesomelist.com/shuaibiyy/awesome-terraform/readme/#private-module-registries
- terraform-azure-PaaS: https://devkimchi.com/2019/01/21/terraforming-azure-paas/
- terraform-azure (freecodecamp): https://www.youtube.com/watch?v=V53AHWun17s
- deploy python app to azure: https://dev.to/kemurayama/deploying-azure-functions-for-python-with-terraform-n
- python/terraform: https://purple.telstra.com/blog/devsecops-on-azure-using-terraform-and-python
- python/terraform/azure: https://medium.com/datasparq-technology/how-to-deploy-a-python-function-app-in-azure-with-terraform-68af428a6c9a
- todo-python-mongo-terraform: https://github.com/Azure-Samples/todo-python-mongo-terraform
- deploy-fastapi-azure: https://www.youtube.com/watch?v=oLdEI3zUcFg
- deploy-fastaapi-on-azure-with-github-actions: https://towardsdatascience.com/deploy-fastapi-on-azure-with-github-actions-32c5ab248ce3