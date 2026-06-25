# 📸 Serverless Photo Recognition System

## 🔍 What It Does
Automatically detects and labels objects in images using AWS AI.

Upload a photo → Lambda triggers → Rekognition reads it → Labels returned!

## 🐒 Live Test Result
Uploaded a monkey photo and got back:
- Animal, Mammal, Monkey, Wildlife, Zoo
- Duration: 670ms | Memory: 93MB

## 🏗️ Architecture
S3 (image upload) → Lambda (trigger) → Rekognition (AI labels) → CloudWatch (logs)

## 🔧 Technologies Used
- AWS S3
- AWS Lambda (Python 3.11)
- Amazon Rekognition
- AWS CloudWatch
- AWS IAM

## 🚀 How to Deploy
1. Create an S3 bucket on AWS
2. Create Lambda function with the code in lambda_function.py
3. Attach IAM roles: AmazonS3ReadOnlyAccess + AmazonRekognitionReadOnlyAccess
4. Add S3 trigger to Lambda
5. Upload any image to S3 and check CloudWatch logs!

## 📊 Sample Output
```json
{
  "image": "monkey.jpg",
  "labels": ["Animal", "Mammal", "Monkey", "Wildlife", "Zoo"]
}
```
