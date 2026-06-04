def generate_report(path, cost, filename="outputs/report.txt"):
    with open(filename, "w") as f:
        f.write("INTELLIGENT ROUTE REPORT\n")
        f.write("========================\n")
        f.write(f"Path: {' -> '.join(path)}\n")
        f.write(f"Total Cost: {cost}\n")