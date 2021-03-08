import hjson

def getHelpDoc(key:str):
    try:
        with open('data/nodice/HelpDoc.hjson','r',encoding='utf-8') as f:
            HelpDoc=hjson.loads(f.read())
            return HelpDoc[key]
    except:
        return False