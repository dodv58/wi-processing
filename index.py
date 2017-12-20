import numpy as np
def handler(event, context):
  arr1 = [1, 2, 3]
  arr2 = [2, 3, 4]
  result =  np.array(arr1) + np.array(arr2)
  return {
        "statusCode": 200,
        "body": np.array_str(result),
        "headers":
        {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Origin": "*"
        }
    }

