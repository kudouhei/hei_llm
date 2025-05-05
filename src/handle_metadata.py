import json

def fix_widgets_state_via_text(input_file, output_file=None):
    """
    通过文本处理修复 .ipynb 文件中 metadata.widgets 缺少的 'state' 键
    
    参数:
        input_file (str): input .ipynb file path
        output_file (str): output .ipynb file path (default overwrite original file)
    """
    if output_file is None:
        output_file = input_file
    
    # read file as text
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # parse to dict
    notebook = json.loads(content)
    
    # check and fix widgets
    if 'metadata' in notebook and 'widgets' in notebook['metadata']:
        widgets = notebook['metadata']['widgets']
        for widget in widgets:
            if 'state' not in widget:
                widget['state'] = {}  # add empty state dict
    
    # save as json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"fixed, saved to: {output_file}")

# execute
fix_widgets_state_via_text("Text_embedding_model_v1.ipynb")