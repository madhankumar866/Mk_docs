## scenario question

1 Scenario
Looking to cleanup file in s3 with the specific tag — encrypted

{[{"arn": "s3:uswesr10290", "name": "s3_1", "tags": ["encrypted"]}, {"arn": "s3:uswesr10090", "name": "s3_2", "tags": ["db"]}]}
List one contains which have the tag encrypted
List tow contains which do not have tag db


Answer: 

import boto3

def list_s3_buckets_tags():
  s3_client = boto3.client('s3')
  encrypted_buckets = []
  non_encrypted_buckets = []s

try:
    response = s3_client.list_buckets()
    buckets = response[Buckets']

for bucket in buckets:
      bucket_name = bucket['Name']
      try:
        tags = s3client.get_bucket_tagging(Bucket=bucket_name)
        tag_set = tags['Set']
        if any(tag['Key'] == 'encrypted' for tag in tag_set):
          encrypted_buckets.append({
            'arn'{bucket_name}",
            'name': bucket_name,
            'tags': ['encrypted']
          })
       else:
          non_encryptedbuckets.append({
            'arn'bucket_name}",
            'name': bucket_name,
            tags': [tagKey'] for tag in tag_set]
          })

return encrypted_buckets, non_encrypted_buckets

if name == "main":
  encrypted, non_encrypted = list_s3_buckets_tags()
   
  print("Buckets with 'encrypted' tag")
  for bucket in encrypted:
   print(bucket)

print("Buckets without 'encrypted' tag")
  for bucket in non_encrypted:
   print(bucket)