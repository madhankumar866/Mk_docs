import os
import yaml

# Custom loader to ignore unknown tags
class SafeLoaderIgnoreUnknown(yaml.SafeLoader):
    pass

def ignore_unknown_tags(loader, tag_suffix, node):
    return None  # Ignore and return None for unknown tags

SafeLoaderIgnoreUnknown.add_multi_constructor("tag:yaml.org,2002:", ignore_unknown_tags)

def generate_nav_from_docs(docs_dir):
    nav = []
    for root, _, files in os.walk(docs_dir):
        rel_dir = os.path.relpath(root, docs_dir)
        if rel_dir == ".":
            rel_dir = ""
        section = []
        for file in sorted(files):
            if file.endswith(".md"):
                path = os.path.join(rel_dir, file).replace("\\", "/")
                title = os.path.splitext(file)[0].replace("-", " ").capitalize()
                section.append({title: f"{path}"})
        if section:
            if rel_dir:
                nav.append({rel_dir.capitalize(): section})
            else:
                nav.extend(section)
    return nav

def update_mkdocs_yaml(nav, yaml_file="mkdocs.yml"):
    with open(yaml_file, "r") as f:
        # Use the custom loader to safely ignore unknown tags
        config = yaml.load(f, Loader=SafeLoaderIgnoreUnknown)

    config["nav"] = nav

    with open(yaml_file, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    docs_directory = "docs"
    nav_structure = generate_nav_from_docs(docs_directory)
    update_mkdocs_yaml(nav_structure)
    print("mkdocs.yml updated with navigation from docs folder.")
