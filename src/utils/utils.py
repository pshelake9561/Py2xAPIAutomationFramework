# class or function
class Util(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_header_put_delete(token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token)
        }
        return headers

    def read_env_file(self):
        pass
