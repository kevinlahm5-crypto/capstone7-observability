## Build phases
| Phase | What it covers |
|---|---|
| 0 | VPC, subnets, NAT gateway, route tables, security groups |
| 1 | EC2 + ALB web tier |
| 2 | ECS Fargate app tier |
| 3 | RDS MySQL with Enhanced Monitoring + Performance Insights |
| 4 | Kinesis Firehose → S3 centralized logging, CloudWatch Agent log collection |
| 5 | Logs Insights queries, X-Ray tracing, RDS slow query testing |
| 6 | CloudWatch Alarms (ECS CPU, ALB 5xx, error count) |
| 7 | EventBridge rules |
| 8 | Lambda automated remediation + SNS alerts |
| 9 | CloudWatch dashboard, mock failure test, final report |

Full details, including test results and screenshots for each phase, are in [REPORT.md](./REPORT.md) and the `evidence/` folder.

## Environment
- Region `us-east-1`
- All resources prefixed `capstone7-*`
- Resources torn down after submission — no active infrastructure