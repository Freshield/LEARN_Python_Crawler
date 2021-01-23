# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_try_tc_ocr.py
@Time: 2021-01-23 11:35
@Last_update: 2021-01-23 11:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models
import os


class OCRCore(object):

    def ImageToString(self, image_path, isUrl=False, high_acc=False):
        # modify by freshyu, 保证只有为True对时候才使用高精度
        high_acc = True if high_acc is True else False

        secret_id = os.environ.get('TC_SECRETID')
        secret_key = os.environ.get('TC_SECRETKEY')

        cred = credential.Credential(secret_id, secret_key)

        httpProfile = HttpProfile()
        httpProfile.endpoint ='ocr.tencentcloudapi.com'

        clientProfile = ClientProfile()

        clientProfile.httpProfile = httpProfile

        clientProfile.signMethod ="TC3-HMAC-SHA256"
        client = ocr_client.OcrClient(cred, 'ap-guangzhou', clientProfile)
        # modify by freshyu， 增加高精度部分
        req = models.GeneralBasicOCRRequest() if not high_acc else models.GeneralAccurateOCRRequest()

        param=None
        if isUrl:
            param='{"ImageUrl":"image_path"}'.replace("image_path",image_path)
            # print(param)
            #param["ImageUrl"]=image_path
        else:
            # print("local image path")
            param ='{"ImageBase64":"ImageEncoder"}'.replace("ImageEncoder",self.ImageEncoder(image_path))

        req.from_json_string(param)

        try:
            # modify by freshyu, 增加高精度部分
            resp = client.GeneralBasicOCR(req) if not high_acc else client.GeneralAccurateOCR(req)

            res_ai = json.loads(resp.to_json_string())

            return res_ai
        except Exception as e:

            """
            e.message可能包含以下内容 
            3	错误的请求；其中 message:account abnormal,errorno is:2为账号欠费停服
            4	签名为空
            5	签名串错误
            6	签名中的 APPID/Bucket 与操作目标不匹配
            9	签名过期
            10	APPID 不存在
            11	SecretId 不存在
            12	APPID 和 SecretId 不匹配
            13	重放攻击
            14	签名校验失败
            15	操作太频繁，触发频控
            16	Bucket不存在
            21	无效参数
            23	请求包体过大
            24	没有权限
            25	您购买的资源已用完
            107	鉴权服务内部错误
            108	鉴权服务不可用
            213	内部错误
            -1102	图片解码失败
            -1300	图片为空
            -1301	参数为空
            -1304	参数过长
            -1308	图片下载失败
            -9021	未检测到文本
            -9003	OCR 识别失败
            """
            res=dict()
            res['message'] = e.message

            return res

    def ImageEncoder(self,image_path):

        with open(image_path, 'rb')as f:

            byte_data = base64.b64encode(f.read())

            str_data =bytes.decode(byte_data, encoding='utf-8')

        return str_data


if __name__ == '__main__':
    import json

    ocr = OCRCore()
    image_path = 'http://img1.miaoshoucdn.com/dapp/upload/certificate/2018-05-10/3f4e913383d3781fa2e7a2531a81fc02.jpg'
    image_path = 'data/pic2.png'
    res = ocr.ImageToString(image_path, isUrl=False, high_acc=True)
    print(json.dumps(res, indent=4, ensure_ascii=False))
