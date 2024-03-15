# Lambda-Dynamodb-Insert
A simple AWS serverless project showcasing AWS Lambda &amp; DynamoDB. Includes a Lambda function inserting data into DynamoDB, with IAM role permissions. Perfect for kickstarting serverless data insertion with AWS.
# Dynamodb
DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS). It's designed to provide seamless scalability, high performance, and low latency for applications that require flexible and reliable data storage.

# key features and concepts:

1] NoSQL Database: DynamoDB is a NoSQL database, which means it doesn't follow the traditional relational database model. Instead, it provides a flexible schema where each item (equivalent to a row in a relational database) can have different attributes.

2] Managed Service: DynamoDB is a fully managed service, which means AWS handles administrative tasks like hardware provisioning, setup, and maintenance. This allows developers to focus solely on building their applications rather than managing infrastructure.

3] Scalability: DynamoDB is designed to scale seamlessly. You can start with a small capacity and then scale up or down as needed without any downtime. It automatically distributes data across multiple servers to handle load spikes and ensure high availability.

4] Performance: DynamoDB offers single-digit millisecond latency for read and write operations, making it suitable for applications that require low-latency access to data.

5] Data Model: Data in DynamoDB is organized into tables, which consist of items (similar to rows in a relational database) and attributes (similar to columns). Each item has a primary key, which uniquely identifies the item within the table. DynamoDB supports two types of primary keys:

6] Partition Key: A single attribute that uniquely identifies an item.
7] Composite Key (Partition Key + Sort Key): A combination of two attributes where the first attribute is the partition key and the second attribute is the sort key. This allows for hierarchical organization of data within a partition.
8] Consistency Models: DynamoDB offers two consistency models:

9] Eventually Consistent Reads: Reads may not reflect the most recent write, but they will eventually converge.
10] Strongly Consistent Reads: Reads are guaranteed to reflect the most recent write.
11] Indexes: DynamoDB supports two types of indexes:

12] Global Secondary Indexes (GSI): Allow querying the table using non-primary key attributes.
13] Local Secondary Indexes (LSI): Similar to GSI but limited to attributes within the same partition key.
14] Throughput Capacity: DynamoDB allows you to provision read and write throughput capacity for your tables, which determines the maximum number of reads and writes per second your table can handle.

15] Pricing: DynamoDB pricing is based on provisioned throughput capacity, storage used, and data transfer. It offers a free tier with limited usage to get started.

# Step-1 

## 1] Created The Dynamodb NoSQL Databse 

![1](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/0ddae2ad-103b-47e7-b954-2c1b4b998128)


## 2] After this created the lambda function 

![2_lambda_function](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/c8fcaae1-ec79-40d7-989a-5420055038ca)


## 3] Configured the Event in lamda function 
  ### Event In lambda 

In AWS Lambda, events are the triggers or stimuli that invoke the execution of your Lambda functions. Lambda functions are designed to respond to various types of events coming from different AWS services or external sources. Here's a simplified explanation of events in Lambda:

![3 1_configuring the events](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/ed53cfa4-462e-4786-9bb8-f42ccad3ebc9)

## 4]  Created the lambda function in python to insert the data into dynamodb 

![4_code](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/2d59dda4-b75b-4cec-9aee-12094123215a)

## 5] Created the items in dyanmodb 

## Items In Dynamodb

In Amazon DynamoDB, an "item" refers to a single data record within a table. It's analogous to a row in a traditional relational database. Items in DynamoDB are composed of attributes, where each attribute has a name and a value. Here are some key points about items in DynamoDB:

![1 1_dynamodb_item_creation](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/b9fff8d5-00e6-43f9-ad2c-08c0030dc38f)


## 6] Created the IAM Roles for Lambda function to give Full-Access of Dynamodb to the Lambda function 

![3_IAM_role](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/1a75e2b5-ff0b-42ce-bd2a-e2518b4cbbec)


## 7] Deploy And tested The code 

![5](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/238843c6-cccf-448e-b317-ddc8bbfe2aa3)


## 8] After testing of Code data Is inserted successfully into The Dynamodb NoSQL Database

![6_Dynamodb_console_output](https://github.com/pranavsk313/Lambda_Dynamo_insert/assets/122976840/5594050c-3462-4bd8-858a-017ee149d63d)




