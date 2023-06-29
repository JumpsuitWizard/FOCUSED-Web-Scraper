
class Bom:
    def __init__(self):
        self.bom_format = "CycloneDX"
        self.spec_version = "1.3"
        self.components = []

    def add_component(self, component_type, name, version, company_name):
        component = {
            "type": component_type,
            "name": name,
            "version": version,
            "company": {
                "name": company_name
            }
        }
        self.components.append(component)

    def add_component_with_shared_authors(self, component_type, name, version, company_name, shared_authors):
        component = {
            "type": component_type,
            "name": name,
            "version": version,
            "company": {
                "name": company_name
            },
            "shared_authors": shared_authors,
        }
        self.components.append(component)

    def to_dict(self):
        bom_dict = {
            "bomFormat": self.bom_format,
            "specVersion": self.spec_version,
            "components": self.components
        }
        return bom_dict
