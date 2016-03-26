import pytest
from django.core.urlresolvers import reverse
from django.conf import settings

def test_admin_index_url():
    assert reverse('admin:index') == '/' + settings.ADMIN_PATH + '/'

def test_admin_index_view(admin_client):
    response = admin_client.get(reverse('admin:index'))
    assert response.status_code == 200

def test_nested_admin_url():
    assert reverse('nesting_server_data')

if __name__ == '__main__':
    pytest.main()
