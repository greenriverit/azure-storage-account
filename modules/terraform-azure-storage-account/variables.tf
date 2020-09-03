## Copyright 2020 Green River IT (GreenRiverIT.com) as described in LICENSE.txt distributed with this project on GitHub.  
## Start at https://github.com/AgileCloudInstitute?tab=repositories    

####################################################################################################################
####Define the input variables:  
####################################################################################################################
#Note that the client referred to is an App Registration.
variable "subscriptionId" { }
variable "tenantId" { }
variable "clientId" { }
variable "clientSecret" { }
variable "storageAccountName" { }
variable "storageContainerName" { }
variable "resourceGroupName" { }
variable "resourceGroupLocation" { }
variable "subnetId" { }
#variable "environmentName" { }

##Define the output variables
data "azurerm_subscription" "current" {}
output "subscription_name" { value = data.azurerm_subscription.current.display_name }
output "subscription_id" { value = data.azurerm_subscription.current.subscription_id }
output "tenant_id" { value = data.azurerm_subscription.current.tenant_id }
