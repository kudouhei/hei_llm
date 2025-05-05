import nbformat

# Load the notebook
file_path = 'Text_embedding_model.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Fix or remove widgets metadata
if 'widgets' in nb['metadata']:
    if not all('state' in widget for widget in nb['metadata']['widgets']):
        # Either remove widgets or add state keys
        del nb['metadata']['widgets']  # or implement proper state addition

# Save the fixed notebook
with open('Text_embedding_model_v1.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)