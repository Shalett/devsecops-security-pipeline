resource "aws_s3_bucket" "test" {
  bucket = "security-demo-test"

  tags = {
    Name = "security-demo"
  }
}