provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "lakehouse_bucket" {
  bucket = "enterprise-lakehouse-bucket-demo"
}
