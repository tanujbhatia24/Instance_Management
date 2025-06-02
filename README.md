# 🚀 Automated EC2 Instance Management with AWS Lambda and Boto3

This project automates the **starting** and **stopping** of EC2 instances using **AWS Lambda** and **Boto3**, based on instance tags.
---

## 📌 Project Overview

Using this setup, a Lambda function checks EC2 instances for specific tags:
- Instances tagged with `Action=Auto-Stop` will be **stopped** if they are running.
- Instances tagged with `Action=Auto-Start` will be **started** if they are stopped.

This is ideal for cost-saving or scheduled automation tasks.
---

## 🛠️ Technologies Used

- AWS EC2
- AWS Lambda
- AWS IAM
- Boto3 (AWS SDK for Python)
- Python 3.x
---

## ✅ Prerequisites

- AWS account with access to EC2, Lambda, and IAM
- IAM permissions to create/manage roles and Lambda functions
- Basic knowledge of Python
---

## ⚙️ Setup Instructions

### 1. Create EC2 Instances
- Go to the **EC2 Dashboard**.
- Launch **two t2.micro** instances (or free-tier eligible).
- Tag the instances:
  - Instance 1: `Key=Action`, `Value=Auto-Stop`
  - Instance 2: `Key=Action`, `Value=Auto-Start`
---

### 2. Create an IAM Role for Lambda

1. Go to **IAM > Roles > Create Role**
2. Choose **Trusted Entity**: `Lambda`
3. Attach the following permissions:
   - ✅ Quick test: `AmazonEC2FullAccess`
   - 🔐 Recommended: Use the custom policy below for least privilege:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}
```
4. Name it something like lambda_ec2_manager_role.
---

### 3. Create the Lambda Function

1.Go to AWS Lambda > Create function
2. Runtime: Python 3.x
3. Name: ManageEC2ByTag
4. Assign the IAM role you created above.
5. Lambda Code
   You can use the file for reference.
---

### 4. Test the Function

1. Click Test in the Lambda console.
2. Use a simple empty test payload {}.
3. Check EC2 Dashboard to confirm:
   1. Auto-Stop instance is stopped.
   2. Auto-Start instance is started.
---

### 5. Validation Snapshots
1. EC2 Instances Before
2. IAM Role with Permissions
3. Lambda Execution Result
4. EC2 Instances After
