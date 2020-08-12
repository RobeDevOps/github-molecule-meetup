"""Role testing files using testinfra."""

def test_packages_are_installed(host):
    required_package = host.package('nginx')
    assert required_package.is_installed

def test_nginx_service_is_enabled_and_running(host):
    nginx_service = host.service('nginx')
    assert nginx_service.is_enabled
    assert nginx_service.is_running

def test_nginx_server_is_available(host):
    nginx_server = host.addr("localhost")
    assert nginx_server.port('80').is_reachable
