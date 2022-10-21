"""Generate API documentation."""

# pylint: disable=unspecified-encoding

import sys

import yaml
from inflection import underscore


class DocumentationGeneration:
    """Class for modifying YAML file for documentation."""

    def __init__(self, mozart_filename: str) -> None:
        self.mozart_filename = mozart_filename
        self.mozart_yaml = self._load_yaml()

    def _load_yaml(self) -> dict:
        """Load the yaml file as a dict."""
        with open(self.mozart_filename, "r") as mozart_yaml_file:
            return yaml.safe_load(mozart_yaml_file)

    def update_description(self) -> None:
        """update YAML file with README.md file."""

        with open("README.md", "r") as readme_file:
            readme_content = readme_file.read()

        self.mozart_yaml["info"]["description"] = readme_content
        print(f"{self.mozart_filename} updated with README.md")

    def add_usage_descriptions(self) -> None:
        """Add python endpoint name and partial API usage example."""

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
                description = f"""Use the `{operation_id}` endpoint with one of:
```mozart_client
mozart_client.{method_name}()
```"""
                # Add the rest of the api's that can be used
                # Reverse in order to get mozart_api right after mozart_client
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

        with open("docs/mozart-api.yaml", "w") as mozart_yaml_file:
            yaml.dump(self.mozart_yaml, mozart_yaml_file, indent=4)


def main():
    """Modify the YAML file for documentation generation."""

    # Currently manually define a Mozart YAML file.
    # This should be pulled from somewhere in the future.
    mozart_filename = sys.argv[1]

    documentation = DocumentationGeneration(mozart_filename)

    documentation.update_description()
    documentation.add_usage_descriptions()

    documentation.write_yaml()


if __name__ == "__main__":
    main()
