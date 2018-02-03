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
> pipenv install httpie
```

To work in the environment:
```sh
> pipenv shell
(boto3-dynamodb-0PTZRWPv) > export AWS_PROFILE=whatever
> python ...       # can also use python3
```

Install DynamoDB
[locally](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html):

```sh
> java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
> ^C     # to kill
```

### Determine Key Structure

For small examples (e.g. `cable-scrape`) we will only need one partition. The
partition key is year (e.g. 2018) and the sort key is a concatenation of month
and day (e.g. `03-27`). The relevant items will be lists of values for speed,
sn, etc. (e.g. `up: [6.76, 7.66, 5.98,...]`).

The queries of this table will **not** be *ad hoc*. We'll usually query a year
based on partition key and then all values for every month (what if there is no
month yet?).



