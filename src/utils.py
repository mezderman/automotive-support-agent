import os

def load_prompt_template(template_name, **kwargs):
    # Construct the path to the template
    template_path = os.path.join("src", "prompts", f"{template_name}.txt")

    # Read the template file
    with open(template_path, "r") as file:
        template = file.read()

    # Replace placeholders with provided variables
    return template.format(**kwargs)
