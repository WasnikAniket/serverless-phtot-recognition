## Architecture Diagram

User uploads image
       ↓
   AWS S3 Bucket
       ↓ (triggers)
  AWS Lambda Function
       ↓ (calls)
  Amazon Rekognition
       ↓ (returns labels)
  CloudWatch Logs
