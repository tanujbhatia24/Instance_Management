# Automated EC2 Instance Management with AWS Lambda and Boto3
This project automates the **starting** and **stopping** of EC2 instances using **AWS Lambda** and **Boto3**, based on instance tags.
---

## Project Overview
Using this setup, a Lambda function checks EC2 instances for specific tags:
- Instances tagged with `Action=Auto-Stop` will be **stopped** if they are running.
- Instances tagged with `Action=Auto-Start` will be **started** if they are stopped.

This is ideal for cost-saving or scheduled automation tasks.
---

## Technologies Used
- AWS EC2
- AWS Lambda
- AWS IAM
- Boto3 (AWS SDK for Python)
- Python 3.x
---

## Prerequisites
- AWS account with access to EC2, Lambda, and IAM
- IAM permissions to create/manage roles and Lambda functions
- Basic knowledge of Python
---

## Setup Instructions
### 1. Create EC2 Instances<br>
- Go to the **EC2 Dashboard**.<br>
- Launch **two t2.micro** instances (or free-tier eligible).<br>
- Tag the instances:<br>
  - Instance 1: `Key=Action`, `Value=tanuj-Auto-Stop`<br>
  - Instance 2: `Key=Action`, `Value=tanuj-Auto-Start`
---

### 2. Create an IAM Role for Lambda
1. Go to **IAM > Roles > Create Role**
2. Choose **Trusted Entity**: `Lambda`
3. Attach the following permissions:
   - ✅ Quick test: `AmazonEC2FullAccess`(Note: In a real-world scenario, you would want to limit permissions for better security.)
4. Name it something like lambda_ec2_manager_role.
---

### 3. Create the Lambda Function<br>
1. Go to AWS Lambda > Create function
2. Runtime: Python 3.x
3. Name: ManageEC2ByTag_tanuj
4. Assign the IAM role you created above.
5. Lambda Code
   You can use the below file for reference.<br>
   [lambda_function.py](https://github.com/tanujbhatia24/Instance_Management/blob/main/lambda_function.py)
---

### 4. Test the Function
1. Click Test in the Lambda console.
2. Use a simple empty test payload > {}.
3. Check EC2 Dashboard to confirm:
   1. Auto-Stop instance is stopped.
   2. Auto-Start instance is started.
---

## Validation Snapshots
1. EC2 instances before Lambda execution<br>
   ![image](https://github.com/user-attachments/assets/7a41137e-31f9-42d7-861f-fd9b473dea84)<br>
   ![image](https://github.com/user-attachments/assets/952b4d4e-7470-40b1-832e-6cc1355aef43)<br>

2. IAM role with permissions<br>
   ![image](https://github.com/user-attachments/assets/3ce42bf9-2e99-4775-9227-8e2ab13794b6)<br>

3. Labda function<br>
   <img width="934" alt="image" src="https://github.com/user-attachments/assets/7acd22ba-6705-4891-96d1-fad0ed5fb335" /><br>

4. Lambda execution result<br>
   ![image](https://github.com/user-attachments/assets/a8bccc83-6a7c-40bf-b930-2c0b7ffe757a)<br>
   ![image](https://github.com/user-attachments/assets/f01b70c2-45bc-473f-8705-5986f0bd18d2)<br>

5. EC2 instances after Lambda execution<br>
   ![image](https://github.com/user-attachments/assets/b3bf03ca-14c3-4494-8a84-d4b5326d390f)<br>
   ![image](https://github.com/user-attachments/assets/b92d8739-86c4-47a8-bc0a-d49e08b8be29)
---

## License
This project is intended for educational and demonstration purposes. You are welcome to use and adapt it as a reference; however, please ensure that your work represents your own understanding and is not reproduced verbatim.
