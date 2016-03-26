import pytest
from django.core.urlresolvers import reverse
from django.conf import settings

def test_admin_index_url():
    assert reverse('admin:index') == '/' + settings.ADMIN_PATH + '/'

if __name__ == '__main__':
    pytest.main()
