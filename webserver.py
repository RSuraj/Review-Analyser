from http.server import BaseHTTPRequestHandler,HTTPServer
#from sqlalchemy import create_engine
#from  sqlalchemy.orm import sessionmaker
#from  te import Base, Restaurant,MenuItem
import cgi,cgitb
class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='post'  action='/poste'>
                <h2>What would you like me to say?</h2>
                <input type="text"  name="message" id="message" >
                <input type="submit" value="Submit">
                </form>'''
                output += "</body></html>"
                self.wfile.write(bytes(output, "UTF-8"))
                return
            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='post'  action='/hello'>
                <h2>What would you like me to say?</h2>
                <input type="text"  name="message" id="message" >
                <input type="submit" value="Submit">
                </form>'''
                output += "</body></html>"
                self.wfile.write(bytes(output, "UTF-8"))
                return
        except IOError:
            self.send_error(404,"file not found %s" % self.path)       

    def do_POST(self):
        try:
            if self.path.endswith("/poste"):
                self.send_response(301)

            form = cgi.FieldStorage( fp=self.rfile, headers=self.headers,environ={'REQUEST_METHOD':'POST'})
            messagecontent = form.getvalue("message")
            self.end_headers()
            print(messagecontent)

            #ctype = cgi.parse_header(self.headers.getheader('Content-type'))
            #pdict = cgi.parse_header(self.headers.getheader('Content-type'))

            #if ctype == 'multipart/form-data':

                #fields=cgi.parse_multipart(self.rfile , pdict)
                #messsagecontent =fields.get('message')
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent
            output += '''<form method='POST' enctype='multipart/form-data' action='/poste'><h2>What would you ggglike me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(bytes(output, "UTF-8"))
            print(output)
            return
        except:
            pass

def main():
    try:
        port=8080
        server = HTTPServer(('',port),webserverHandler)
        print("webserver is running on port %s" %port)
        server.serve_forever()
    except KeyboardInterrupt:
        print ("c pressed stopping webserver........")
        server.socket.close();
if __name__ == '__main__':
        main()
 

