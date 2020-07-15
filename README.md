# AWS Batch demo with MatrixMath

This is a simple container workload, used as an introduction to [AWS Batch](https://aws.amazon.com/batch/).

The python code in _matrixmath.py_ simply generates and multiples random matrices, using [Numpy](https://numpydoc.readthedocs.io/en/latest/).

Directory cfn contains CloudFormation template to create AWS Batch resources, including a Job Queue, Compute Environment, and sample Job Definition.

Content created July 2020 to support a customer-facing lab.  There are a handful of rough edges to be wary of, incuding that it hardwires a container repo on DockerHub.

The CloudFormation generates several IAM Roles associated with scheduling jobs on AWS Batch.  In most cases, these roles are created for you from the AWS Console.  Because we're assuming the console for Batch has ever been invoked, they are in the template.

---
last edit 15 July 2020

