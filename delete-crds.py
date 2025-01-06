import subprocess

# Get the list of CRDs
result = subprocess.run(["kubectl", "get", "crds", "-o", "name"], capture_output=True, text=True)

if result.returncode != 0:
    print(f"Error fetching CRDs: {result.stderr}")
    exit(1)

# Filter and delete CRDs containing 'monitoring'
crds = result.stdout.strip().split("\n")
for crd in crds:
    if "monitoring" in crd:
        delete_result = subprocess.run(["kubectl", "delete", crd], capture_output=True, text=True)
        if delete_result.returncode == 0:
            print(f"Deleted CRD: {crd}")
        else:
            print(f"Failed to delete CRD {crd}: {delete_result.stderr}")
