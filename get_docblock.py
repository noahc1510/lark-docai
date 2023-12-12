import json

import lark_oapi as lark
from lark_oapi.api.docx.v1 import *

DEBUG = False

# SDK 使用说明: https://github.com/larksuite/oapi-sdk-python#readme
def get_docblock(user_access_token, document_id):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListDocumentBlockRequest = ListDocumentBlockRequest.builder() \
        .document_id(document_id) \
        .page_size(500) \
        .document_revision_id(-1) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token(user_access_token).build()
    response: ListDocumentBlockResponse = client.docx.v1.document_block.list(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.docx.v1.document_block.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    if DEBUG:
        # 处理业务结果
        lark.logger.info(lark.JSON.marshal(response.data, indent=4))
    return json.loads(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    get_docblock()
