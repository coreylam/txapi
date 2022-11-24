from txapi import API

def test_create_apiv2():
    apiv2 = API.v2(
        api_domain="domain1",
        endpoint="endpoint1",
        version="222",
        region="ap-guangzhou",
        secret_id="xxx",
        secret_key="xxx",
        token=None,
        ssl=True,
        debug=False)
