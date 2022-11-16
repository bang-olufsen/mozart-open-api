#!/bin/python

"""Generate API documentation and README."""

import sys
from dataclasses import dataclass

import yaml
from inflection import underscore


@dataclass
class MarkdownFile:
    """Class for handling markdown templates."""

    path: str | None = None
    content: str | None = None
    tag: str | None = None


class DocumentationGeneration:
    """Class for modifying YAML file for documentation."""

    def __init__(self, mozart_filename: str) -> None:
        self.mozart_filename = mozart_filename
        self.mozart_yaml = self._load_yaml()
        self.mozart_api_name = self.mozart_yaml["info"]["title"]
        self.mozart_api_version = self.mozart_filename.replace(
            "mozart-api-", ""
        ).removesuffix(".yaml")

        self.markdown_files = [
            MarkdownFile(path="docs/markdown/badges.md", tag="{BADGES}"),
            MarkdownFile(path="docs/markdown/description.md", tag="{DESCRIPTION}"),
            MarkdownFile(path="docs/markdown/overview.md", tag="{OVERVIEW}"),
            MarkdownFile(path="docs/markdown/supports.md", tag="{SUPPORTS}"),
            MarkdownFile(content=f"# {self.mozart_api_name}", tag="{HEADER}"),
            MarkdownFile(content=self.mozart_api_version, tag="{VERSION}"),
        ]

        self.readme_template = MarkdownFile(path="docs/markdown/readme_template.md")
        self.mozart_api_template = MarkdownFile(
            path="docs/markdown/mozart_api_template.md"
        )

        self._load_markdown()

    def _load_yaml(self) -> dict:
        """Load the yaml file as a dict."""
        with open(self.mozart_filename, "r", encoding="utf-8") as mozart_yaml_file:
            return yaml.safe_load(mozart_yaml_file)

    def _load_markdown(self) -> None:
        """Read the markdown files."""

        # Get content from the markdown files
        for markdown_file in self.markdown_files:
            if markdown_file.path is not None:
                with open(markdown_file.path, "r", encoding="utf-8") as file:
                    markdown_file.content = file.read()

        # Get the templates
        with open(self.mozart_api_template.path, "r", encoding="utf-8") as file:
            self.mozart_api_template.content = file.read()

        with open(self.readme_template.path, "r", encoding="utf-8") as file:
            self.readme_template.content = file.read()

    def fill_templates(self) -> None:
        """Update templates with self.markdown_files MarkdownFile objects."""

        for markdown_file in self.markdown_files:
            self.mozart_api_template.content = self.mozart_api_template.content.replace(
                markdown_file.tag, markdown_file.content
            )

            self.readme_template.content = self.readme_template.content.replace(
                markdown_file.tag, markdown_file.content
            )

        print("Filled mozart_api_template and readme_template")

    def add_dummy_server(self) -> None:
        """Add a dummy server address for the try it feature to be shown and always fail."""
        self.mozart_yaml["servers"] = [
            {
                "url": "http://0.0.0.0",
                "description": "Local IP address placeholder",
            }
        ]

        print("Added dummy IP address for documentation")

    def add_usage_descriptions(self) -> None:
        """Add Python method name and partial API usage example."""

        # Get the endpoint
        for path in self.mozart_yaml["paths"].copy():
            for http_method in self.mozart_yaml["paths"][path].copy():
                if http_method not in ("get", "put", "post", "delete"):
                    continue

                # Create the descriptions
                operation_id = self.mozart_yaml["paths"][path][http_method][
                    "operationId"
                ]
                method_name = underscore(operation_id)

                # Add text and mozart_client
                description = f"""Use the `{operation_id}` method in the Python package with one of:
```mozart_client
mozart_client.{method_name}()
```"""
                # Add the rest of the api's that can be used
                # Reverse order to get mozart_api right after mozart_client
                for tag in reversed(
                    self.mozart_yaml["paths"][path][http_method]["tags"]
                ):
                    description += f"""
```{tag.lower()}_api
{tag.lower()}_api.{method_name}()
```"""
                # Keep the original description if it exists.
                if "description" in self.mozart_yaml["paths"][path][http_method]:
                    self.mozart_yaml["paths"][path][http_method][
                        "description"
                    ] += f"""
{description}"""
                else:
                    self.mozart_yaml["paths"][path][http_method][
                        "description"
                    ] = description

        print("Descriptions updated with usage descriptions.")

    def add_websocket_usage_descriptions(self) -> None:
        """Add Python method name and partial API usage example."""

        # Get the WebSocketEvent
        for schema in self.mozart_yaml["components"]["schemas"].copy():
            if "WebSocketEvent" in schema:

                # Create Python usage descriptions
                event_name = schema.removeprefix("WebSocketEvent")
                method_name = f"get_{underscore(event_name)}_notifications"

                # Create the usage example
                description = f"""Use the `{method_name}()` method in the Python package to get notifications of this type:
```python
from mozart_api.mozart_client import MozartClient

def {underscore(event_name)}_notifications(notification: object):
    \"""{event_name} notification handler.\"""
    print(notification)

mozart_client = MozartClient(host="192.168.0.1")
mozart_client.{method_name}({underscore(event_name)}_notifications)
mozart_client.connect_notifications()
```"""

                # Keep the original description if it exists.
                if "description" in self.mozart_yaml["components"]["schemas"][schema]:
                    self.mozart_yaml["components"]["schemas"][schema][
                        "description"
                    ] += f"""
{description}"""
                else:
                    self.mozart_yaml["components"]["schemas"][schema][
                        "description"
                    ] = description

        print("WebSocketEvent descriptions updated with usage descriptions.")

    def update_description(self) -> None:
        """update YAML file with filled template."""

        self.mozart_yaml["info"]["description"] = self.mozart_api_template.content
        print(f"{self.mozart_filename} updated with filled mozart_api_template")

    def update_readme(self) -> None:
        """update README.md file with filled template."""

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(self.readme_template.content)

        print("README.md updated with filled readme_template")

    def write_yaml(self) -> None:
        """Save the yaml dict as a file."""
        # Ensure that multiline strings use the | character
        yaml.add_representer(
            str,
            lambda dumper, data: dumper.represent_scalar(
                "tag:yaml.org,2002:str", data, style="|"
            )
            if "\n" in data
            else dumper.represent_scalar("tag:yaml.org,2002:str", data),
        )

        with open("docs/mozart-api.yaml", "w", encoding="utf-8") as mozart_yaml_file:
            yaml.dump(self.mozart_yaml, mozart_yaml_file, indent=4)


def main():
    """Modify the YAML file for documentation generation."""

    # Currently manually define a Mozart YAML file.
    # This should be pulled from somewhere in the future.
    mozart_filename = sys.argv[1]

    documentation = DocumentationGeneration(mozart_filename)

    documentation.fill_templates()

    documentation.update_readme()
    documentation.update_description()

    documentation.add_dummy_server()
    documentation.add_usage_descriptions()
    documentation.add_websocket_usage_descriptions()

    documentation.write_yaml()


if __name__ == "__main__":
    main()
