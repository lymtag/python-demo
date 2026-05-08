from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.schemas.uploads import UploadProxyResponse
from app.services.upload_client import UploadClientError, parse_response, upload_file


router = APIRouter(prefix="/uploads", tags=["uploads"])


@router.post("/proxy", response_model=UploadProxyResponse)
async def proxy_upload(
    file: UploadFile = File(...),
    token: str = Form(...),
    url: str = Form(...),
    field_name: str = Form("file"),
    timeout: int = Form(60),
    use_cookie: bool = Form(True),
) -> UploadProxyResponse:
    suffix = Path(file.filename or "upload.bin").suffix

    try:
        with NamedTemporaryFile(delete=True, suffix=suffix) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file.flush()

            response = upload_file(
                file_path=temp_file.name,
                auth_token=token,
                url=url,
                field_name=field_name,
                timeout=timeout,
                use_cookie=use_cookie,
            )
    except (FileNotFoundError, UploadClientError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return UploadProxyResponse(data=parse_response(response))

