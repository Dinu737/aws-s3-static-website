# AWS S3 Static Website Hosting using Python (Boto3)

## Project Overview

This project demonstrates how to host a static website on Amazon S3 using Python and the AWS SDK for Python (Boto3).

The project automates:

* Uploading website files to Amazon S3
* Enabling Static Website Hosting
* Configuring public access using Bucket Policies
* Generating the website endpoint URL

---

## Architecture

```text
HTML Website
      ↓
Python (Boto3)
      ↓
Amazon S3 Bucket
      ↓
Static Website Hosting
      ↓
Bucket Policy
      ↓
Public Website URL
```

---

## AWS Services Used

* Amazon S3
* AWS IAM
* AWS CLI

---

## Technologies Used

* Python
* Boto3
* HTML
* Git
* GitHub

---

## Project Structure

```text
aws-s3-static-website/
│
├── deploy2.py
├── deploy3.py
├── index33.html
├── requirements.txt
└── README.md
```

---

## Prerequisites

* AWS Account
* AWS CLI Configured
* Python 3.x
* Boto3

Install dependencies:

```bash
pip install boto3
```

---

## Steps Performed

### 1. Create an S3 Bucket

Created an S3 bucket for website hosting.

### 2. Upload Website File

Uploaded the HTML file to the S3 bucket using Boto3.

### 3. Enable Static Website Hosting

Configured:

* Index Document: index.html

### 4. Configure Public Access

* Disabled Block Public Access
* Applied Bucket Policy for public read access

### 5. Access Website

Opened the S3 website endpoint URL in a browser.

---

## Sample Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::dinesh-static-website-demo "]
    }
  ]
}
```

---

## Learning Outcomes

* Amazon S3 Fundamentals
* Static Website Hosting
* Bucket Policies
* AWS CLI Configuration
* Python Automation with Boto3
* Git and GitHub Project Management

---

## Author

Dinesh Ghule

AWS | Python | Cloud Computing
