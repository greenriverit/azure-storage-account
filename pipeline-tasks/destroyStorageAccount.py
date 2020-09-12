## Copyright 2020 Green River IT (GreenRiverIT.com) as described in LICENSE.txt distributed with this project on GitHub.  
## Start at https://github.com/AgileCloudInstitute?tab=repositories    
import deploymentFunctions as depfunc 

storageAccountName = 'tfbkendabc123x'  
storageContainerName = 'tfcontainer'  
resourceGroupName = 'pipeline-resources'  
resourceGroupLocation = 'westus'  

#First delete the storage container within the storage account
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-create
#deleteStorageContainerCommand = "az storage container delete --account-name " + storageAccountName + " --name " + storageContainerName 
#print("deleteStorageContainerCommand is: ", deleteStorageContainerCommand)
#depfunc.runShellCommand(deleteStorageContainerCommand)  

#Then delete the storage account
#https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-cli
deleteStorageAccountCommand = "az storage account delete --name " + storageAccountName + " --resource-group " + resourceGroupName + " --yes "  
print("deleteStorageAccountCommand is: ", deleteStorageAccountCommand)
depfunc.runShellCommand(deleteStorageAccountCommand)  

keyVaultName = 'testvlt789'  
keyName = 'demoStorageKey'  
deleteSecretCommand = 'az keyvault secret delete --vault-name ' + keyVaultName + ' --name ' + keyName 
depfunc.runShellCommand(deleteSecretCommand)
purgeSecretCommand = 'az keyvault secret purge --vault-name ' + keyVaultName + ' --name ' + keyName 
depfunc.runShellCommand(purgeSecretCommand)
