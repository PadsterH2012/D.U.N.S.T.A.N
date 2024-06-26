import os
import sys

# Ensure /app and /app/content-creator are in the PYTHONPATH
sys.path.append('/app')
sys.path.append('/app/content_creator')  # Adjusted the path to match the correct directory name
sys.path.append('/app/content_creator/extractor')

# print("PYTHONPATH is set to:", os.environ.get('PYTHONPATH'))
# print("sys.path:", sys.path)
# print("Contents of /app directory:")
# for root, dirs, files in os.walk('/app'):
#     for name in files:
#         print(os.path.join(root, name))

# print("Contents of /app/content_creator directory:")
# for root, dirs, files in os.walk('/app/content_creator'):
#     for name in files:
#         print(os.path.join(root, name))

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
