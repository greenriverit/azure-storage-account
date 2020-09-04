## Copyright 2020 Green River IT (GreenRiverIT.com) as described in LICENSE.txt distributed with this project on GitHub.  
## Start at https://github.com/AgileCloudInstitute?tab=repositories    

print("inside createStorageAccount.py")
  
import sys  	
import re	
import os	
import subprocess  	
from pathlib import Path	
import pip  
#import deploymentFunctions as depfunc  

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')	

#Re-usable function that will be replaced with something already in depfunc
def runTerraformCommand(commandToRun, workingDir ):	
    print("Inside runTerraformCommand(..., ...) function. ")	
    print("commandToRun is: " +commandToRun)	
    print("workingDir is: " +workingDir)	
    proc = subprocess.Popen( commandToRun,cwd=workingDir,stdout=subprocess.PIPE, shell=True)	
    while True:	
      line = proc.stdout.readline()	
      if line:	
        thetext=line.decode('utf-8').rstrip('\r|\n')	
        decodedline=ansi_escape.sub('', thetext)	
        print(decodedline)	
      else:	
        break	

###############################################################################
### Print vars to validate that they are imported and also obscured
###############################################################################
storageAccountName=sys.argv[1]  
storageContainerName=sys.argv[2]  
terraBackendKey=sys.argv[3]  
DefaultWorkingDirectory=sys.argv[4]
clientId=sys.argv[5]
clientSecret=sys.argv[6]
subscriptionId=sys.argv[7]
tenantId=sys.argv[8]
#The following 7 need to be made into input variables	
resourceGroupName="pipeline-resources"	
terraKeyFileName = "azure-storage-account-state.tf"
vpc_name="thisVPC"
system_name="thisSystem"
environment_name="thisEnvironment"
owner_name="thisOwner"
vm_name="thisVM"
##Need to populate the following two still:  
resourceGroupLocation='West US'
subnetId=''

#New set environment variables
os.environ["ARM_CLIENT_ID"] = clientId
os.environ["ARM_CLIENT_SECRET"] = clientSecret
os.environ["ARM_SUBSCRIPTION_ID"] = subscriptionId
os.environ["ARM_TENANT_ID"] = tenantId

print("Python version is: ", sys.version_info[0])  	
print("storageAccountName is: ", storageAccountName)  
print("storageContainerName is: ", storageContainerName)  
print("terraBackendKey is: ", terraBackendKey)  
print("DefaultWorkingDirectory is: ", DefaultWorkingDirectory)  
print("clientId is: ", clientId)  
print("clientSecret is: ", clientSecret)  
print("subscriptionId is: ", subscriptionId)  
print("tenantId is: ", tenantId)  
  
####################################################################################
### Set values for pathToApplicationRoot and dirToUseNet  
### while also listing contents of each directory  
####################################################################################
print("About to list contents of DefaultWorkingDirectory")	
print(*Path(DefaultWorkingDirectory).iterdir(), sep="\n")	

subDir2=DefaultWorkingDirectory+"/_terraform-azure-storage-account/drop"	
print("About to list contents of (DefaultWorkingDirectory)/_terraform-azure-storage-account/drop")	
print(*Path(subDir2).iterdir(), sep="\n")	

pathToApplicationRoot = subDir2  

subDir3=DefaultWorkingDirectory+"/_terraform-azure-storage-account/drop/calls-to-modules"	
print("About to list contents of (DefaultWorkingDirectory)/_terraform-azure-storage-account/drop/calls-to-modules")	
print(*Path(subDir3).iterdir(), sep="\n") 

subDir4=DefaultWorkingDirectory+"/_terraform-azure-storage-account/drop/calls-to-modules/terraform-azure-storage-account-call-to-module/" 
print("About to list contents of (DefaultWorkingDirectory)/_terraform-azure-storage-account/drop/calls-to-modules/terraform-azure-storage-account-call-to-module/")	
print(*Path(subDir4).iterdir(), sep="\n")	
  
dirToUseNet = subDir4   
print("dirToUseNet is: ", dirToUseNet)  

##########################################################################################
### Initialize terraform and remote backend from inside the network foundation directory
##########################################################################################
resourceGroupNameLine="    resource_group_name  = \""+resourceGroupName+"\"\n"	
storageAccountNameTerraformBackendLine="    storage_account_name = \""+storageAccountName+"\"\n"	
storageContainerNameLine="    container_name       = \""+storageContainerName+"\"\n"	
terraBackendKeyLine="    key                  = \""+terraKeyFileName+"\"\n"	

tfFileNameAndPath=dirToUseNet+"terraform.tf"	
print("tfFileNameAndPath is: ", tfFileNameAndPath)	
print("About to write 8 lines to a file.")	
f = open(tfFileNameAndPath, "w")	
f.write("terraform {\n")	
f.write("  backend \"azurerm\" {\n")	
f.write(resourceGroupNameLine)	
f.write(storageAccountNameTerraformBackendLine)	
f.write(storageContainerNameLine)	
f.write(terraBackendKeyLine)	
f.write("  }\n")	
f.write("}\n")	
f.close()	

print("About to read the file we just wrote.")	
#open and read the file after the appending:	
f = open(tfFileNameAndPath, "r")	
print(f.read()) 	

print("About to refresh list contents of (DefaultWorkingDirectory)/_terraform-azure-storage-account/drop/calls-to-modules/terraform-azure-storage-account-call-to-module/") 
print(*Path(dirToUseNet).iterdir(), sep="\n")	

print("About to call terraform init:  ")	
initCommand="terraform init -backend=true -backend-config=\"access_key="+terraBackendKey+"\""  	
runTerraformCommand(initCommand, dirToUseNet )	
  
#############################################################################
### Create the Storage Account
#############################################################################
#Get Vars to pass into terraform commands:
varsFragmentStorageAccount = ""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"subscriptionId=" + subscriptionId +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"tenantId=" + tenantId +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"clientId=" + clientId +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"clientSecret=" + clientSecret +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"storageAccountName=" + storageAccountName +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"storageContainerName=" + storageContainerName +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"resourceGroupName=" + resourceGroupName +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"resourceGroupLocation=" + resourceGroupLocation +"\""  
varsFragmentStorageAccount = varsFragmentStorageAccount + " -var=\"subnetId=" + subnetId +"\""  
varsStorageAccount = varsFragmentStorageAccount

print("varsStorageAccount is: ", varsStorageAccount)  
applyCommandNet = "terraform apply -auto-approve" + varsStorageAccount
print("applyCommandNet is: ", applyCommandNet)
#runTerraformCommand(applyCommandNet, dirToUseNet)  

