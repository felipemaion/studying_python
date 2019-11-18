"""
Python 3.6

3rd party packages:
    - requests
"""

import os
import datetime
from time import sleep

import requests
## GENERAL
# Request URL: https://paladins.gamepedia.com/Category:Voice_lines
# Request Method: GET
# Status Code: 200 
# Remote Address: 104.17.95.92:443
# Referrer Policy: no-referrer-when-downgrade

## RESPONSE HEADERS
# age: 12778
# cache-control: s-maxage=18000, must-revalidate, max-age=0
# cf-ray: 4b5e3e461a0b4ca2-GRU
# content-encoding: br
# content-language: en
# content-type: text/html; charset=UTF-8
# date: Mon, 11 Mar 2019 14:33:24 GMT
# expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
# last-modified: Mon, 11 Mar 2019 06:00:26 GMT
# link: <https://gamepedia.cursecdn.com/paladins_gamepedia/b/bc/Wiki.png?version=9b9ae0ddfb261847906f2e4c0ad94b63>;rel=preload;as=image
# server: cloudflare
# status: 200
# vary: X-Forwarded-Proto, X-Mobile, X-LoggedIn, X-Version, Accept-Encoding
# x-content-type-options: nosniff
# x-frame-options: DENY
# x-ua-compatible: IE=Edge

## REQUEST HEADERS
# :authority: paladins.gamepedia.com
# :method: GET
# :path: /Category:Voice_lines
# :scheme: https
# accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# accept-encoding: gzip, deflate, br
# accept-language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7
# cache-control: max-age=0
# cookie: __cfduid=d86280e5dd81689f7e485fff1f602fea91552289659; _ga=GA1.2.77390328.1552289661; _gid=GA1.2.729937787.1552289661; cdmgeo=br; __gads=ID=2ea02dc01169da8f:T=1552289662:S=ALNI_MZ_10hWmyZI7CwVr8fVgJWn_ZsRcw; i10cfd=1; _gat_tracker0=1; _gat_tracker1=1
# if-modified-since: Mon, 11 Mar 2019 05:10:49 GMT
# upgrade-insecure-requests: 1
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36

# :authority: paladins.gamepedia.com
# :method: GET
# :path: /A-bomb-inable_Bomb_King_voice_lines
# :scheme: https
# accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# accept-encoding: gzip, deflate, br
# accept-language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7
# cookie: __cfduid=d86280e5dd81689f7e485fff1f602fea91552289659; _ga=GA1.2.77390328.1552289661; _gid=GA1.2.729937787.1552289661; cdmgeo=br; __gads=ID=2ea02dc01169da8f:T=1552289662:S=ALNI_MZ_10hWmyZI7CwVr8fVgJWn_ZsRcw; i10cfd=1
# if-modified-since: Sun, 10 Mar 2019 23:42:42 GMT
# referer: https://paladins.gamepedia.com/Category:Voice_lines
# upgrade-insecure-requests: 1
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
class Engine:
    """ Persistent requests wrapper.
    Handles all errors except system ones,
    until counter reaches MAX_RETRY value.

    All methods:
    -> requests.Response
    """
    MAX_RETRY = 3
    DELAY = 1.5
    
    def POST(self, *args, **kwargs):
        errors = 0
        while True:
            try:
                sleep(self.DELAY)
                response = requests.post(*args, **kwargs)
                response.raise_for_status()
                return response
            
            except Exception as e:
                if errors == self.MAX_RETRY:
                    raise ConnectionError(e)
                
                print(e.__class__.__name__, e)
                errors += 1


class Scraper(Engine):
    POST_SET = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '452',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'sinfat.ima.sc.gov.br',
        'Origin': 'http://sinfat.ima.sc.gov.br',
        'Pragma': 'no-cache',
        'Referer': 'http://sinfat.ima.sc.gov.br/relatorio.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
    }

    POST_DOWNLOAD = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '161',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'sinfat.ima.sc.gov.br',
        'Origin': 'http://sinfat.ima.sc.gov.br',
        'Pragma': 'no-cache',
        'Referer': 'http://sinfat.ima.sc.gov.br/relatorio.jsp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
    }

    DATA_SET = {
        'AJAXREQUEST': 'j_id_jsp_1801007148_0',
        'formularioDeEmissaoDeRelatorio': 'formularioDeEmissaoDeRelatorio',
        'javax.faces.ViewState': 'j_id1',
        'formularioDeEmissaoDeRelatorio:j_id_jsp_1801007148_36': 'formularioDeEmissaoDeRelatorio:j_id_jsp_1801007148_36',
    }
    
    DATA_DOWNLOAD = {
        'j_id_jsp_1801007148_253': 'j_id_jsp_1801007148_253',
        'j_id_jsp_1801007148_253:btImprimir.x': '290',
        'j_id_jsp_1801007148_253:btImprimir.y': '508',
        'javax.faces.ViewState': 'j_id1',
    }

    URL = 'http://sinfat.ima.sc.gov.br/publico/relatorios/index_er.jsf'
  

    def __init__(self, session_id, reports_types=None, print_state=True):
        self.print_state = print_state

        self.POST_SET['Cookie'] = self.POST_DOWNLOAD['Cookie'] = 'JSESSIONID={}'.format(session_id)


    def POST_set_report(self, reports_type, month, month_num, year) -> None:
        self.DATA_SET['formularioDeEmissaoDeRelatorio:inTipoRelatorio'] = str(reports_type)
        self.DATA_SET['formularioDeEmissaoDeRelatorio:j_id_jsp_1801007148_33InputDate'] = '{} 5, {}'.format(month, year)
        self.DATA_SET['formularioDeEmissaoDeRelatorio:j_id_jsp_1801007148_33InputCurrentDate'] = '{:0>2}/{}'.format(month_num, year)
        
        self.POST(self.URL, headers=self.POST_SET, data=self.DATA_SET)
        
    def POST_get_report(self) -> requests.Response:
        return self.POST(self.URL, headers=self.POST_DOWNLOAD, data=self.DATA_DOWNLOAD)

    def exists(self, filepath):
        if os.path.exists(filepath):
            
            if self.print_state:
                print('exists')
                
            return True

    def save(self, file: bytes, filepath) -> None:
        
        if self.print_state:
            print(len(file))
                    
        with open(filepath, 'wb') as OUT:
            OUT.write(file)
    
    def run(self, output_folder):
        dates = self.dates_range()
        
        for reports_type in self.reports_types:
            for month, month_num, year in dates:
                
                if self.print_state:
                    print('Type: {}, date: {}({}) {}, length:'.format(reports_type, month_num, month, year), end=' ')

                filepath = '{}/REL_{}_{}_{}.pdf'.format(output_folder, reports_type, month_num, year)
                if not self.exists(filepath):
                    self.POST_set_report(reports_type, month, month_num, year)
                    response = self.POST_get_report()
                    self.save(response.content, filepath)


def outputs_to(folder_name) -> str:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name


def main(session_id, folder_name):
    scraper = Scraper(session_id)
    scraper.run(outputs_to(folder_name))




if __name__ == '__main__':
    main(session_id='85D5ACB787BF04CAF363B98464B18CF9', folder_name='reports')












