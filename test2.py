import argparse
import json

from app.services.upload_client import (
    DEFAULT_TOKEN,
    DEFAULT_URL,
    parse_response,
    upload_file,
)



def main():
    parser = argparse.ArgumentParser(description="POST 文件上传")
    parser.add_argument("file_path", help="需要上传的本地文件路径")
    parser.add_argument("--url", default=DEFAULT_URL, help="文件上传接口地址")
    parser.add_argument("--token", default=DEFAULT_TOKEN, help="接口授权 token")
    parser.add_argument(
        "--field-name",
        default="file",
        help="文件字段名，默认 file",
    )
    parser.add_argument("--timeout", type=int, default=60, help="请求超时时间，单位秒")
    parser.add_argument(
        "--no-cookie",
        action="store_true",
        help="不携带 Admin-Token cookie",
    )
    args = parser.parse_args()

    response = upload_file(
        file_path=args.file_path,
        auth_token=args.token,
        url=args.url,
        field_name=args.field_name,
        timeout=args.timeout,
        use_cookie=not args.no_cookie,
    )
    result = parse_response(response)

    if isinstance(result, (dict, list)):
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result)


if __name__ == "__main__":
    main()
