from typing import Callable, Dict, Any
from lesting.api.client import build

class LoginResult:

    certificate: str
    accessToken: str
    lastBindTimestamp: int
    metaData: Dict[str, str]

class QRLogin:

    HOST = "https://legy-jp.line.naver.jp"
    PATH = HOST + "/acct/lgn/sq/v1"
    POLL = HOST + "/acct/lp/lgn/sq/v1"

    HEADERS = {
        "lite": {
            "user-agent": "LLA/2.16.0",
            "x-line-application": "ANDROIDLITE\t2.16.0\tAndroid OS\t10;SECONDARY"
        },
        "ipad": {
            "user-agent": "Line/10.21.3",
            "x-line-application": "IOSIPAD\t10.21.3\tiOS\t14.3;SECONDARY"
        },
        "chrome": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
            "x-line-application": "CHROMEOS\t2.4.1\tChrome OS\t1"
        },
        "desktopwin": {
            "user-agent": "Line/6.5.4",
            "x-line-application": "DESKTOPWIN\t6.5.4\tWindows\t10"
        }
    }

    def __init__(self) -> None:
        self.client = build("line.login", "v1")

    def request(self, method: str, headers: Dict[str, str], *, lp: bool = False, **kwargs: Dict[str, Any]) -> Any:
        return getattr(self.client.parser, method)((self.client.http.request((self.POLL if lp else self.PATH), "POST", getattr(self.client.packer, method)(**kwargs), headers)[1]))

    def loginWithQrCode(self, application: str, certificate: str = "", web: bool = False, callback: Callable = lambda output: print(output)) -> LoginResult:
        headers = QRLogin.HEADERS[application]
        session = self.request("createSession", headers)
        result = self.request("createQrCode", headers, session = session)
        if web:
            callback(f"เว็บไซต์ยืนยัน PIN\n{result.web}")
        callback(f"กดลิ้งนี้ภายใน 2 นาที่\n{result.url}")
        self.request("checkQrCodeVerified", {**headers, **{"x-line-access": session}}, lp = True, session = session)
        try:
            self.request("verifyCertificate", headers, session = session, certificate = certificate)
        except:
            pin = self.request("createPinCode", headers, session = session)
            if web:
                self.client.pin.update(session, pin)
            else:
                callback(f"รหัสยืนยัน PIN\n{pin}")
            self.request("checkPinCodeVerified", {**headers, **{"x-line-access": session}}, lp = True, session = session)
        return self.request("qrCodeLogin", headers, session = session, systemName = headers["x-line-application"].split("\t")[2], autoLoginIsRequired = True)

if __name__ == "__main__":
    qr = QRLogin()
    result = qr.loginWithQrCode("ipad", web = True)
    print("Access Token: " + result.accessToken)
    print("Certificate: " + result.certificate)