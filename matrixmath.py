import numpy as np
import timeit
import boto3
from botocore.exceptions import ClientError
from time import strftime, localtime, time
import os

loggroup = "/cdd/batchjob/"

client = boto3.client('logs',region_name='us-east-2')

def createlog(group):
    try:
        r = client.create_log_group( logGroupName = group)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceAlreadyExistsException':
            pass
        else:
            print("Unexpected error: %s" % e)
            exit()
    return

def createlogstream(group,stream):
    try:
        r = client.create_log_stream(
            logGroupName=group,
            logStreamName=stream
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceAlreadyExistsException':
            pass
        else:
            print("Unexpected error: %s" % e)
            exit()
    return


loops = int(os.environ.get('LOOPS',10))
matrix_size=int(os.environ.get('MATRIX_SIZE',2048))

def compute():
    x = y = matrix_size
    seed = 42
    np.random.seed(seed)
    m1 = np.random.rand(x,y)
    m2 = np.random.rand(x,y)
    m3 = m1 * m2

if __name__ == "__main__":
    createlog(loggroup)
    now = strftime('%m-%d-%y-%H-%M-%S',localtime())
    logstreamname = "demo-" + now
    createlogstream(loggroup,logstreamname)
    results = timeit.timeit("compute()", setup="from __main__ import compute", number=loops)
    results = f'calculated {loops} loops of {matrix_size}x{matrix_size} matrix multiplies in {results} seconds'
    print(results)
    # Get most recent sequence token, the print results to CloudWatch Logs
    # r = client.describe_log_streams(logGroupName=loggroup, logStreamNamePrefix=logstreamname)
    # seq = r['logStreams']['uploadSequenceToken']
    r = client.put_log_events(logGroupName=loggroup, logStreamName=logstreamname,
        logEvents = [ {
            'timestamp': int(1000*time()),
            'message': results
        }]
    )
    pass
