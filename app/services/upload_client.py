import mimetypes
from pathlib import Path

import requests


DEFAULT_URL = "http://localhost:1024/api/system/recharge/batchkuaishou"
DEFAULT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
    "eyJleHAiOjE3NzU3MDIzMDksInVzZXJJZCI6IjEwMDAwMDAwMDA0NiIsInRpbWVzdGFtcCI6IjE3NzU2OTg3MDk2MjYifQ."
    "cDi1MdVcQQoamfsfuNFEFN5wpqqUhyOg1OMeVIXFDNw"
)


class UploadClientError(RuntimeError):
    """Raised when the upstream upload request fails."""


def upload_file(
    file_path,
    auth_token,
    url=DEFAULT_URL,
    field_name="file",
    timeout=60,
    use_cookie=True,
):
    """Upload a local file by POST multipart/form-data."""
    path = Path(file_path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"文件不存在: {path}")

    content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    headers = {
        "Authorization": auth_token,
        "Accept": "*/*",
        "Origin": "http://localhost:1024",
        "Referer": "http://localhost:1024/recharge",
        "Connection": "keep-alive",
    }
    cookies = {"Admin-Token": auth_token} if use_cookie else None

    try:
        with path.open("rb") as file_obj:
            files = {
                field_name: (path.name, file_obj, content_type),
            }
            response = requests.post(
                url,
                headers=headers,
                cookies=cookies,
                files=files,
                timeout=timeout,
            )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise UploadClientError(f"上传请求失败: {exc}") from exc

    return response


def parse_response(response):
    try:
        return response.json()
    except ValueError:
        return response.text

