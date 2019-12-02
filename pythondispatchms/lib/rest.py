# -*- coding: utf-8 -*-
"""The base Controller API."""

from tg import app_globals,abort
import requests

class Rest(object):

    def __init__(self):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()

    def get(self,url,params):
        return self.doresponse("get",url,params)

    def post(self,url,params):
        return self.doresponse("post",url,params)

    def put(self,url,params):
        return self.doresponse("put",url,params)

    def delete(self,url,params):
        return self.doresponse("delete",url,params)

    def doresponse(self,verb,url,params):
        error_number = 0
        try:
            kw = {'params': params, 'verify': False, 'timeout': 10}
            if verb=='get':
                response=self.session.get(url, **kw)
            elif verb=='post':
                response= self.session.post(url, **kw)
            elif verb=='put':
                response= self.session.put(url, **kw)
            elif verb=='delete':
                response= self.session.delete(url, **kw)
            else:
                abort(status_code=500, detail="Programming Error Method unknown")

        except requests.exceptions.RequestException as err:
            error_number = 500
            error_description = "Unknown Error"+str(err)
        except requests.exceptions.HTTPError as err:
            error_number = 501
            error_description = "Http Error:" + str(err)
        except requests.exceptions.ConnectionError as err:
            error_number = 502
            error_description = "Error Connecting:" + str(err)
        except requests.exceptions.Timeout as err:
            error_number = 503
            error_description = "Timeout Error:"+ str(err)
        except requests.exceptions.ConnectTimeout as err:
            error_number = 504
            error_description = "Connect Timeout Error:"+ str(err)
        except requests.exceptions.ReadTimeout as err:
            error_number = 505
            error_description = "Read Timeout Error:"+ str(err)
        except requests.exceptions.URLRequired as err:
            error_number = 506
            error_description = "URLRequired Error:"+ str(err)
        finally:
            if error_number==0:
                if response.status_code != requests.codes.ok:
                    nr = response.text.replace('{', "").replace('}', "").replace('"', "")
                    abort(status_code=response.status_code, detail=nr)
                else:
                    r=response.json()
                    #if "error" in r:
                    #    if r["error"]!="ok":
                    #        abort(status_code=503, detail="not found")
                return response.json()
            else:
                abort(status_code=error_number, detail=error_description)



class TelefonicaRest(object):

    def __init__(self):
        self.session = requests.session()

    def get(self,url,params):
        return self.doresponse("get",url,params)

    def post(self,url,params):
        return self.doresponse("post",url,params)

    def put(self,url,params):
        return self.doresponse("put",url,params)

    def delete(self,url,params):
        return self.doresponse("delete",url,params)

    def doresponse(self,verb,url,params):
        error_number = 0
        try:
            kw = {'params': params, 'cert': app_globals.cert, 'verify': False, 'timeout': 10}
            if verb=='get':
                response=self.session.get(url, **kw)
            elif verb=='post':
                response= self.session.post(url, **kw)
            elif verb=='put':
                response= self.session.put(url, **kw)
            elif verb=='delete':
                response= self.session.delete(url, **kw)
            else:
                abort(status_code=500, detail="Programming Error Method unknown")
        except requests.exceptions.RequestException as err:
            error_number = 500
            error_description = "Unknown Error"+str(err)
        except requests.exceptions.HTTPError as err:
            error_number = 501
            error_description = "Http Error:" + str(err)
        except requests.exceptions.ConnectionError as err:
            error_number = 502
            error_description = "Error Connecting:" + str(err)
        except requests.exceptions.Timeout as err:
            error_number = 503
            error_description = "Timeout Error:"+ str(err)
        except requests.exceptions.ConnectTimeout as err:
            error_number = 504
            error_description = "Connect Timeout Error:"+ str(err)
        except requests.exceptions.ReadTimeout as err:
            error_number = 505
            error_description = "Read Timeout Error:"+ str(err)
        except requests.exceptions.URLRequired as err:
            error_number = 506
            error_description = "URLRequired Error:"+ str(err)
        finally:
            if error_number==0:
                if response.status_code != requests.codes.ok:
                    nr = response.text.replace('{', "").replace('}', "").replace('"', "")
                    abort(status_code=response.status_code, detail=nr)
                else:
                    r=response.json()
                    if "error" in r:
                        if r["error"]!="ok":
                            abort(status_code=503, detail="not found")
                return response.json()
            else:
                abort(status_code=error_number, detail=error_description)