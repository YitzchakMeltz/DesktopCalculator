try:
    import httplib
except:
    import http.client as httplib



def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        print("Internet Connection Availible")
        return True
    except:
        conn.close()
        print("No Internet Connection Found")
        return False

have_internet()