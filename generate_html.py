"""Generate API documentation."""

import sys

import yaml


class DocumentationGeneration:
    """Class for modifying YAML file for documentation."""

    def __init__(self, mozart_filename: str) -> None:
        self.mozart_filename = mozart_filename
        self.mozart_yaml = self._load_yaml()

    def _load_yaml(self) -> dict:
        """Load the yaml file as a dict."""
        with open(self.mozart_filename, "r") as mozart_yaml_file:
            return yaml.safe_load(mozart_yaml_file)

    def update_license(self) -> None:
        """update license key with a URL."""
        if "url" not in self.mozart_yaml["info"]["license"]:
            mit_license_url = {"url": "https://spdx.org/licenses/MIT"}

            self.mozart_yaml["info"]["license"].update(mit_license_url)
            print(f"{self.mozart_filename} updated with {mit_license_url}")

    def update_contact(self) -> None:
        """update contact key with a URL."""
        if "url" not in self.mozart_yaml["info"]["contact"]:
            support_url = {"url": "https://support.bang-olufsen.com/"}

            self.mozart_yaml["info"]["contact"].update(support_url)
            print(f"{self.mozart_filename} updated with {support_url}")

    def update_servers(self) -> None:
        """update YAML file with WebSocket servers."""

        if "servers" not in self.mozart_yaml:
            websocket_servers = {
                "servers": [
                    {
                        "url": "ws://localhost:9339/",
                        "description": "WebSocket notification channel",
                    },
                    {
                        "url": "ws://localhost:9339/remoteControl",
                        "description": "Remote control WebSocket notification channel",
                    },
                ],
            }

            self.mozart_yaml.update(websocket_servers)
            print(f"{self.mozart_filename} updated with {websocket_servers}")

    def update_description(self) -> None:
        """update YAML file with WebSocket servers."""

        with open("README.md", "r") as readme_file:
            readme_content = readme_file.read()
            print(readme_content)

        self.mozart_yaml["info"]["description"] = readme_content
        print(f"{self.mozart_filename} updated with README.md")

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

    documentation.update_license()
    documentation.update_contact()
    documentation.update_servers()
    documentation.update_description()

    documentation.write_yaml()


if __name__ == "__main__":
    main()
