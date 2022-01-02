import os

class DockerComposeYaml
    """
    This class handles the docker-compose.yaml file
    """
    def __init__(
        self,
        docker_compose_yaml_file='docker-compose.yaml',
        ):
        self.docker_compose_yaml = os.path.abspath(docker_compose_yaml)
    
    def _load_docker_compose_yaml_file()
        with open(self.docker_compose_yaml_file, 'r') as yf:
            self.docker_compose_yaml = yaml.load(yf, Loader=yaml.FullLoader)

    def _create_services_volumes_dict(self):
        """
        Create a dictionary with all services and their volumes, only include
        services that have a volume.
        """
        self.volumes = {
            service:self.docker_compose_yaml['services'][service]['volumes']
            for service in self.docker_compose_yaml['services'] if 'volumes' in
            self.docker_compose_yaml['services'][service]
            }
