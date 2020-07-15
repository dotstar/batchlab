stack=batch
template=batch.yaml
parameters=batch_parameters.json
test:
	cfn-lint ${template} # --ignore-checks W2001, W1020

create:
	aws cloudformation create-stack \
	  --stack-name ${stack} \
	  --template-body file://${template} \
	  --parameters file://${parameters} \
  	  --capabilities CAPABILITY_NAMED_IAM

update:
	aws cloudformation update-stack \
	--stack-name ${stack} \
	--template-body file://${template} \
	--parameters file://${parameters} \
	--capabilities CAPABILITY_NAMED_IAM
	
delete:
	aws cloudformation delete-stack --stack-name ${stack}
	
resources:
	aws cloudformation describe-stack-resources --stack-name ${stack} --query StackResources[].[LogicalResourceId,ResourceStatus,Timestamp] --output table
