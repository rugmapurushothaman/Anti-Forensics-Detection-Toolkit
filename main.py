from detectors.hidden_files import detect_hidden_files

print("=" * 60)
print("ANTI-FORENSICS DETECTION TOOLKIT")
print("=" * 60)

print("\nStarting Scan...\n")

scan_path = "sample_data"

hidden = detect_hidden_files(scan_path)

if hidden:
    print("[!] Hidden files detected:")
    for file in hidden:
        print(file)
else:
    print("[✓] No hidden files found.")
