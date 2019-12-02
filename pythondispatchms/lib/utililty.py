import regex
from pythondispatchms.lib.helpers import whoami
import os,sys
from tg import abort
from pathlib import Path
import pdfkit
from tg import render_template

class URLunicode():
    def __init___(self):
        pass

    def decode(self,payload):
        self.ec = {"%u00b4":"´","%u00c0": "À", "%u00c1": "Á", "%u00c2": "Â", "%u00c3": "Ã", "%u00c4": "Ä", "%u00c5": "Å",
                   "%u00c6": "Æ", "%u00c7": "Ç", "%u00c8": "È", "%u00c9": "É", "%u00ca": "Ê", "%u00cb": "Ë",
                   "%u00cc": "Ì", "%u00cd": "Í", "%u00ce": "Î", "%u00cf": "Ï", "%u00d1": "Ñ", "%u00d2": "Ò",
                   "%u00d3": "Ó", "%u00d4": "Ô", "%u00d5": "Õ", "%u00d6": "Ö", "%u00d8": "Ø", "%u00d9": "Ù",
                   "%u00da": "Ú", "%u00db": "Û", "%u00dc": "Ü", "%u00dd": "Ý", "%u00df": "ß", "%u00e0": "à",
                   "%u00e1": "á", "%u00e2": "â", "%u00e3": "ã", "%u00e4": "ä", "%u00e5": "å", "%u00e6": "æ",
                   "%u00e7": "ç", "%u00e8": "è", "%u00e9": "é", "%u00ea": "ê", "%u00eb": "ë", "%u00ec": "ì",
                   "%u00ed": "í", "%u00ee": "î", "%u00ef": "ï", "%u00f0": "ð", "%u00f1": "ñ", "%u00f2": "ò",
                   "%u00f3": "ó", "%u00f4": "ô", "%u00f5": "õ", "%u00f6": "ö", "%u00f8": "ø", "%u00f9": "ù",
                   "%u00fa": "ú", "%u00fb": "û", "%u00fc": "ü", "%u00fd": "ý", "%u00ff": "ÿ"}
        nv=payload
        keyword_number = regex.search("%u00", payload)
        if keyword_number is not None:
            keywords_found = regex.finditer("%u00", payload)
            for element in keywords_found:
                ini = element.start()
                key=payload[ini:ini+6]
                if key in self.ec:
                    value=self.ec[key]
                else:
                    value=""
                nv=nv.replace(key,value)
        return nv

class ExportCVS():
    """
     Export CVS
    """
    @classmethod
    def create(cls, list,name,url):
        app_dir = os.getenv('dispatch_DIR')
        cwd=os.getenv('dispatch_DIR')
        np=cwd.rfind("/")+1
        who=whoami()
        if who=="":
            error="CSV Failure"
            reason="User not logged"
            message = "The following {} occured, this is due to {}, please DEBUG the url : {}".format(error, reason,url)
            abort(status_code=500, detail=message)
        file_name=cwd+"/"+cwd[np:].replace(".","")+"/public/"+who+"_"+name+".csv"

        my_file = Path(file_name)
        if my_file.is_file():
            os.remove(file_name)
        outfile = open(file_name, 'w')
        for item in list:
            outfile.write(item)
        outfile.close()
        return "/"+who+"_"+name+".csv"

class ExportPDF():
    """
     Export CVS
    """
    @classmethod
    def create(cls, parameters,name,url):
        cwd=os.getenv('dispatch_DIR')
        np=cwd.rfind("/")+1
        who=whoami()
        if who=="":
            error="CSV Failure"
            reason="User not logged"
            message = "The following {} occured, this is due to {}, please DEBUG the url : {}".format(error, reason,url)
            abort(status_code=500, detail=message)
        file_name=cwd+"/"+cwd[np:].replace(".","")+"/public/"+who+"_"+name+".pdf"

        my_file = Path(file_name)
        if my_file.is_file():
            os.remove(file_name)


        ## PDF Generation ##

        options = {
            'page-width': '11.0in',
            'page-height': '8.5in',
            'margin-top': '0.1in',
            'margin-right': '0.1in',
            'margin-bottom': '0.1in',
            'margin-left': '0.1in',
            'encoding': "UTF-8",
            'quiet': '',
        }
        body = render_template(parameters, "mako", url)
        pdfkit.from_string(body, file_name, options=options)

        return "/"+who+"_"+name+".pdf"