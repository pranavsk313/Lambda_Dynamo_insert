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

![Screenshot 2024-02-24 234557](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/5e26d5ec-eac0-437d-a2b8-1896e943693f)

## 2] after this created the lambda function 

![Screenshot 2024-02-24 235008](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/e981f00a-c8ff-46ee-962c-6a78a6e472b3)

![Screenshot 2024-02-24 235020](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/22d40611-3b58-4708-b6e2-ceb01df6c8a2)

## 4] Configured the Event in lamda function 

## Event In lambda 

In AWS Lambda, events are the triggers or stimuli that invoke the execution of your Lambda functions. Lambda functions are designed to respond to various types of events coming from different AWS services or external sources. Here's a simplified explanation of events in Lambda:

![Screenshot 2024-02-25 000351](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/96f3958a-5ca7-421c-8973-059ddb55d1ca)

## 5]  Created the lambda function in python to insert the data into dynamodb 

![Screenshot 2024-02-27 170038](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/1af9b67c-a5ef-4f89-a4e5-070e4a85b024)

## 6] Created the items in dyanmodb 

## Items In Dynamodb

In Amazon DynamoDB, an "item" refers to a single data record within a table. It's analogous to a row in a traditional relational database. Items in DynamoDB are composed of attributes, where each attribute has a name and a value. Here are some key points about items in DynamoDB:

![Screenshot 2024-02-25 001657](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/04f2d50b-bd09-463b-be0b-afcde3c9632e)

## 7] Created the IAM Roles for Lambda function to give Full-Access of Dynamodb to the Lambda function 

![Screenshot 2024-02-25 002731](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/3aa42412-d0bc-468b-83e6-044bb9d0ba18)

![Screenshot 2024-02-25 002914](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/96dbab30-53c5-4f26-9baf-006ba354aebd)

![Screenshot 2024-02-25 002932](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/8c706d0f-a4e7-46d4-b9d8-9dfa5690b096)

## 8] Deploy And tested The code 

![Screenshot 2024-02-27 170059](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/793c8f05-bbc4-4cd2-8dee-9a71861e6e8a)

## 9] After testing of Code data Is inserted successfully into The Dynamodb NoSQL Database

![Screenshot 2024-02-27 170953](https://github.com/AdityaAgasti07/Lambda-Dynamodb-Insert/assets/159541012/5a738618-cefa-450c-ba0f-4725549b64e8)




