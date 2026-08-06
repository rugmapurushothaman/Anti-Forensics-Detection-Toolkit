import os

def detect_hidden_files(path):
    hidden_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            # Hidden files beginning with '.'
            if file.startswith("."):
                hidden_files.append(os.path.join(root, file))

            # Windows hidden attribute
            full_path = os.path.join(root, file)

            try:
                if os.name == "nt":
                    import ctypes
                    attrs = ctypes.windll.kernel32.GetFileAttributesW(full_path)
                    if attrs != -1 and attrs & 2:
                        hidden_files.append(full_path)
            except Exception:
                pass

    return hidden_files
