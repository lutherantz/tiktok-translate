from time import time
from requests import post
from urllib.parse import urlencode
from signer import Argus, Ladon, Gorgon, md5
from os import system as sysc, name, get_terminal_size as term_size

Windows = name == "nt"

banner = """
 ███████████  ███  █████              ████                        █████   
░█░░░███░░░█ ░░░  ░░███              ░░███                       ░░███    
░   ░███  ░  ████  ░███ █████  █████  ░███   ██████   ████████   ███████  
    ░███    ░░███  ░███░░███  ███░░   ░███  ░░░░░███ ░░███░░███ ░░░███░   
    ░███     ░███  ░██████░  ░░█████  ░███   ███████  ░███ ░███   ░███    
    ░███     ░███  ░███░░███  ░░░░███ ░███  ███░░███  ░███ ░███   ░███ ███
    █████    █████ ████ █████ ██████  █████░░████████ ████ █████  ░░█████ 
   ░░░░░    ░░░░░ ░░░░ ░░░░░ ░░░░░░  ░░░░░  ░░░░░░░░ ░░░░ ░░░░░    ░░░░░  
\033[0m
"""

class Api:
    @staticmethod
    def sign(params, payload: str = None, cookie: any = None, aid: int = 1233, license_id: int = 1611921764):
        # Fuck, j'aime pas danser dans la fête, j'ai tout le temps des sons dans la tête
        return ...

    @staticmethod
    def get_timestamp():
        return int(time())

    @staticmethod
    def get_timestamp_ms():
        return int(round(time() * 1000))
    
class Terminal:
    @staticmethod
    def _print(thing: any, content: any, _input: bool = False, new_line: bool = True) -> str:
        col = "\033[38;2;255;-;255m"
        first_part = f"[{thing}] | {content}"
        new_part = ""

        counter = 0
        for caracter in first_part:
            new_part += col.replace('-', str(225 - counter * int(255/len(first_part)))) + caracter
            counter += 1

        if _input:
            return f"{new_part}\033[0m"
        if not new_line:
            print(f"{new_part}\033[0m", end="\r")
        else:
            print(f"{new_part}\033[0m")

    @staticmethod
    def clear():
        sysc(f"cls" if Windows else "clear")
    
    @staticmethod
    def center_banner(banner: str):
        color = "\033[38;2;255;-;255m"
        terminal_width = term_size().columns
        centered_banner = ""

        counter = 0
        for line in banner.splitlines():
            counter += 4
            centered_line = line.center(terminal_width)
            color_value = str(225 - counter * int(255/len(line))) if len(line) > 0 else "255"
            centered_banner += f"{color.replace('-', color_value)}{centered_line}\n"

        return centered_banner

class Translation:
    def get_translation(self, item_id: int, target_lang: str):
        params = {
            "iid": "7340767782260279072",
            "device_id": "7340765072865756704",
            "ac": "wifi",
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "330603",
            "version_name": "33.6.3",
            "device_platform": "android",
            "os": "android",
            "ab_version": "33.6.3",
            "ssmix": "a",
            "device_type": "ASUS_Z01QD",
            "device_brand": "Asus",
            "language": "fr",
            "os_api": "28",
            "os_version": "9",
            "openudid": "709386489a6818a0",
            "manifest_version_code": "2023306030",
            "resolution": "720*1280",
            "dpi": "240",
            "update_version_code": "2023306030",
            "_rticket": Api.get_timestamp_ms(),
            "is_pad": "0",
            "current_region": "FR",
            "app_type": "normal",
            "sys_region": "FR",
            "mcc_mnc": "20801",
            "timezone_name": "Asia/Shanghai",
            "residence": "FR",
            "app_language": "fr",
            "carrier_region": "FR",
            "ac2": "wifi",
            "uoo": "0",
            "op_region": "FR",
            "timezone_offset": "28800",
            "build_number": "33.6.3",
            "host_abi": "arm64-v8a",
            "locale": "fr",
            "region": "FR",
            "ts": Api.get_timestamp(),
            "cdid": "286db893-6cff-4c22-bff3-6db54fb251ae"
        }

        data = urlencode({
            "item_id": item_id,
            "target_lang": target_lang
        })

        headers = {
            "User-Agent"  : f"com.zhiliaoapp.musically/2023306030 (Linux; U; Android 9; fr; ASUS_Z01QD; Build/PI;tt-ok/3.12.13.4-tiktok)",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        } | Api.sign(params, data)

        res = post(
            url = "https://api31-normal-useast2a.tiktokv.com/aweme/v1/translation/description/?",
            params = urlencode(params),
            data = data,
            headers = headers
        ).json()

        if res["status_msg"]:
            return "The content don't need to be transtale."
        
        return res["translated_content"]
    
if __name__ == "__main__":
    Terminal.clear()
    print(Terminal.center_banner(banner))

    item_id = int(input(Terminal._print("?", "Video ID> ", True)))
    target_lang = input(Terminal._print("?", "Desired Language> ", True))

    content = Translation().get_translation(item_id, target_lang)
    
    Terminal._print("-", f"Content> {content}")