import nbformat

def fix_missing_widgets_state(input_file, output_file=None):
    """
    修复 Jupyter Notebook 中 metadata.widgets 缺少 'state' 键的问题
    
    参数:
        input_file (str): 输入的 .ipynb 文件路径
        output_file (str): 输出的 .ipynb 文件路径 (默认覆盖原文件)
    """
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # check widgets
    if 'metadata' in nb and 'widgets' in nb['metadata']:
        widgets = nb['metadata']['widgets']
        for widget in widgets:
            if 'state' not in widget:
                widget['state'] = {}  # add state 
                print(f"为 widget {widget.get('model_id', 'unknown')} added state")
    
    # save fixed notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"saved to: {output_file}")

# execute
fix_missing_widgets_state("Text_embedding_model_v1.ipynb")  # overwrite original file
