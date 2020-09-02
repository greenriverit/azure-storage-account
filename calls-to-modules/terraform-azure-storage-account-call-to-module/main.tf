module "azure-storage-account-demo" {
  source = "../../modules/terraform-azure-storage-account/"

  subscriptionId         = "${var.subscriptionId}"
  tenantId               = "${var.tenantId}"
  clientId               = "${var.clientId}"
  clientSecret           = "${var.clientSecret}"
  storageAccountName     = "${var.storageAccountName}"
  storageContainerName   = "${var.storageContainerName}"
  resourceGroupName      = "${var.resourceGroupName}"
  resourceGroupLocation  = "${var.resourceGroupLocation}"
  subnetId               = "${var.subnetId}"
  environmentName        = "${var.environmentName}"
  
}

##Input variables.  Note: The client referred to is an App Registration.
variable "subscriptionId" { }
variable "tenantId" { }
variable "clientId" { }
variable "clientSecret" { }
variable "storageAccountName" { }
variable "storageContainerName" { }
variable "resourceGroupName" { }
variable "resourceGroupLocation" { }
variable "subnetId" { }
variable "environmentName" { }
  
##Output variables
output "subscription_name" { value = "${module.azure-storage-account-demo.subscription_name}" }
output "subscription_id" { value = "${module.azure-storage-account-demo.subscription_id}" }
output "tenant_id" { value = "${module.azure-storage-account-demo.tenant_id}" }
