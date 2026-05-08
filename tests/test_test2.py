from pathlib import Path

import pytest

from app.services import upload_client


class DummyResponse:
    def __init__(self, json_value=None, text="", json_error=None):
        self._json_value = json_value
        self.text = text
        self._json_error = json_error
        self.raise_for_status_called = False

    def json(self):
        if self._json_error:
            raise self._json_error
        return self._json_value

    def raise_for_status(self):
        self.raise_for_status_called = True


def test_upload_file_posts_multipart_request(monkeypatch, tmp_path):
    upload_target = tmp_path / "demo.txt"
    upload_target.write_text("hello", encoding="utf-8")
    response = DummyResponse(json_value={"code": 0})
    captured = {}

    def fake_post(url, headers, cookies, files, timeout):
        captured["url"] = url
        captured["headers"] = headers
        captured["cookies"] = cookies
        captured["files"] = files
        captured["timeout"] = timeout
        file_obj = files["payload"][1]
        captured["file_content"] = file_obj.read()
        return response

    monkeypatch.setattr(upload_client.requests, "post", fake_post)

    result = upload_client.upload_file(
        file_path=upload_target,
        auth_token="token-123",
        url="http://example.test/upload",
        field_name="payload",
        timeout=15,
    )

    assert result is response
    assert response.raise_for_status_called is True
    assert captured["url"] == "http://example.test/upload"
    assert captured["headers"]["Authorization"] == "token-123"
    assert captured["cookies"] == {"Admin-Token": "token-123"}
    assert captured["files"]["payload"][0] == "demo.txt"
    assert captured["files"]["payload"][2] == "text/plain"
    assert captured["file_content"] == b"hello"
    assert captured["timeout"] == 15


def test_upload_file_can_skip_cookie(monkeypatch, tmp_path):
    upload_target = tmp_path / "data.bin"
    upload_target.write_bytes(b"data")
    captured = {}

    def fake_post(url, headers, cookies, files, timeout):
        captured["cookies"] = cookies
        return DummyResponse(json_value={"ok": True})

    monkeypatch.setattr(upload_client.requests, "post", fake_post)

    upload_client.upload_file(upload_target, "token-123", use_cookie=False)

    assert captured["cookies"] is None


def test_upload_file_rejects_missing_file(tmp_path):
    missing_file = tmp_path / "missing.xlsx"

    with pytest.raises(FileNotFoundError, match="文件不存在"):
        upload_client.upload_file(missing_file, "token-123")


def test_parse_response_returns_json_payload():
    response = DummyResponse(json_value={"message": "ok"})

    assert upload_client.parse_response(response) == {"message": "ok"}


def test_parse_response_falls_back_to_text():
    response = DummyResponse(text="plain response", json_error=ValueError("bad json"))

    assert upload_client.parse_response(response) == "plain response"


def test_default_url_keeps_expected_endpoint_shape():
    path = Path(upload_client.DEFAULT_URL)

    assert path.name == "batchkuaishou"
