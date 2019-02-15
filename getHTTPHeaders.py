import re
import zlib

def HTTPHeaders(http_payload):
  try:
    #isolate headers
    headers_raw = http_payload[:http_payload.index("\r\n\r\n") + 2]
    #matches = re.finditer(r'\r\n\r\n', http_payload)
    # for matchNum, match in enumerate(matches):
    #     matchNum = matchNum + 1
    #     headers_raw = http_payload[:match.end()]
    #     print headers_raw
	# #regex = ur"/?P&lt;'name&gt;.*?/: /?P&lt;value&gt;.*?/\n"
    regex = ur"(?:[\r\n]{0,1})(\w+\-\w+|\w+)(?:\ *:\ *)([^\r\n]*)(?:[\r\n]{0,1})"
    headers = dict(re.findall(regex, headers_raw, re.UNICODE))
    # print headers
    return headers
  except:
    return None
  if 'Content-Type' not in headers:
    return None
  return headers

def extractText(headers, http_payload):
  text = None
  #text_type = None
  try:
	  if 'text/html' in headers['Content-Type']:
		  text = http_payload[http_payload.index("\r\n\r\n")+4:]
          # print text
          try:
			  if "Accept-Encoding" in headers.keys():
				  if headers['Accept-Encoding'] == "gzip":
					  text = zlib.decompress(text, 16+zlib.MAX_WBITS)
		  	  elif headers['Content-Encoding'] == "deflate":
				  text = zlib.decompress(text)
          except: pass
  except:
		return None
  return text

	# text_type = headers['Content-Type'].split("/")[1]
	# text = http_payload[http_payload.index("\r\n\r\n")+4:]
    # return text,text_type
