## Copyright 2020 Green River IT (GreenRiverIT.com) as described in LICENSE.txt distributed with this project on GitHub.  
## Start at https://github.com/AgileCloudInstitute?tab=repositories    
import deploymentFunctions as depfunc 
import subprocess
import re 
  
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')  
  
storageAccountName = 'tfbkendabc123x'  
storageContainerName = 'tfcontainer'  
resourceGroupName = 'pipeline-resources'  
resourceGroupLocation = 'westus'  
keyVaultName = 'testvlt789'  
keyName = 'demoStorageKey'  

#First create storage account
#https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-cli
createStorageAccountCommand = "az storage account create --name " + storageAccountName + " --resource-group " + resourceGroupName + " --location " + resourceGroupLocation + " --sku Standard_RAGRS --kind StorageV2"
print("createStorageAccountCommand is: ", createStorageAccountCommand)
depfunc.runShellCommand(createStorageAccountCommand)  

#Then create a storage container within the storage account  
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-create
createStorageContainerCommand = "az storage container create -n " + storageContainerName + " --fail-on-exist --account-name " + storageAccountName
print("createStorageContainerCommand is: ", createStorageContainerCommand)
depfunc.runShellCommand(createStorageContainerCommand)  

getKeyCommand = 'az storage account keys list --resource-group ' + resourceGroupName + ' --account-name ' + storageAccountName + ' --query [0].value -o tsv'

def runSubShellCommand(commandToRun):
    print("Inside runShellCommand(..., ...) function. ")
    print("commandToRun is: " +commandToRun)

    proc = subprocess.Popen( commandToRun,cwd=None, stdout=subprocess.PIPE, shell=True)
    while True:
      line = proc.stdout.readline()
      if line:
        thetext=line.decode('utf-8').rstrip('\r|\n')
        decodedline=ansi_escape.sub('', thetext)
        print(decodedline)
        return decodedline
      else:
        break

storageAccountKey = runSubShellCommand(getKeyCommand)
print("storageAccountKey is: ", storageAccountKey)

saveSecretCommand = 'az keyvault secret set --vault-name ' + keyVaultName + ' --name ' + keyName + ' --value ' + storageAccountKey
depfunc.runShellCommand(saveSecretCommand)

