## boto3-dynamodb: Explore AWS DynamoDB with Python SDK (boto3)

This repo contains small Python test scripts that demonstrate basic functions
on AWs DynamoDB (create table, insert item, etc.).

### Setup Python Envronment

We use `pipenv` to manage Python virtual environments.

**Note**: You don't need to do this if you're pulling the existing repo. These
  instructions are here to show what is needed if you're starting from scratch.

```sh
> mkdir boto3-dynamodb
> cd boto3-dynamodb
> pipenv --three
> pipenv install boto3
```

To work in the environment:
```sh
> pipenv shell
(boto3-dynamodb-0PTZRWPv) > export AWS_PROFILE=whatever
> python ...       # can also use python3
```
