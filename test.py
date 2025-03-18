from typing import Literal
import requests

def request_get(
    url:str,
    headers:dict | None=None
) -> tuple[Literal[True], requests.Response] | tuple[Literal[False], str]:
    """
    Performs a GET request

    returns: tuple(success:bool, response:Response or failure message:str)
    """
    try:
        response = requests.get(
            url,
            stream=True,
            verify=False,
            headers=headers,
        )

    except TimeoutError:
        output = f"GET Request timed out for {url}"
        print(output)
        return False, output

    if not response.ok:
        status_code = response.status_code
        reason = response.reason
        print(
            f"""
            GET Request failed with error code:
            {status_code}: {reason}
            """
        )
        return False, reason

    return True, response

# CIVITAI_TOKEN="a97fcd5f5c1b2050f636e41fd253a463"
# headers = {"Authorization": f"Bearer {CIVITAI_TOKEN}"}
# success, response = request_get("https://civitai.com/api/download/models/959372?type=Model&format=SafeTensor", headers=headers)
headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    ),
    "Authorization": "Bearer a97fcd5f5c1b2050f636e41fd253a463"
}
# success, response = request_get("https://civitai.com/api/download/models/959372?type=Model&format=SafeTensor", headers=headers)
success, response = request_get("https://liblibai-online.liblib.cloud/web/model/037414ba212f4affa014b2c2d164ba41/65d5e8980e1cb17a81256cc30685e90d14a15c2dbef7cd9b1accf56705fa12ba.safetensors?auth_key=1742307840-50a946d355fd4840854f93566f004ceb-0-8d663db59609c0d2ed9fe5d2aa13d61a&attname=%E4%B8%87%E4%BA%AB_%E5%A4%9A%E6%A8%A1%E6%80%81%E8%B6%85%E6%91%84%E5%86%99%E5%AE%9E_V1.safetensors")
# success, response = request_get("https://www.modelscope.cn/models/fireicewolf/Flux_Real_Photo/resolve/master/Flux%20Real%20Photo_V1.safetensors", headers=headers)
filename=response.headers.get("Content-Disposition").split('=')[1]
print(filename)