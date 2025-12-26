import boto3

region = "ap-south-1"
ec2 = boto3.client("ec2", region_name=region)

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print("Instance ID:", instance["InstanceId"])
        print("Instance Type:", instance["InstanceType"])
        print("State:", instance["State"]["Name"])
        print("Launch Time:", instance["LaunchTime"])
pricing = {
    "t2.micro": 0.0116,
    "t2.small": 0.023,
    "t2.medium": 0.0464
}
from datetime import datetime, timezone, timedelta

launch_time = instance["LaunchTime"]
ist = timezone(timedelta(hours=5, minutes=30))
current_time = datetime.now(ist)
running_hours = (current_time - launch_time).total_seconds() / 3600
instance_type = instance["InstanceType"]
hourly_rate = pricing.get(instance_type, 0)
usd_to_inr = 89.0
total_cost = running_hours * hourly_rate
monthly_estimate = hourly_rate * 24 * 30
total_seconds = running_hours * 3600
minutes = int(total_seconds // 60)
seconds = total_seconds % 60

print("\n--- COST REPORT ---")
print(f"Running Hours: {minutes} min {seconds:.0f} sec")
print(f"Hourly Rate: ₹{hourly_rate * usd_to_inr:.2f}")
print(f"Current Cost: ₹{total_cost * usd_to_inr:.2f}")
print(f"Estimated Monthly Cost: ₹{monthly_estimate * usd_to_inr:.2f}")