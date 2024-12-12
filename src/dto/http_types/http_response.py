
class HttpResponse:
    
    def __init__(self, 
        body: dict, 
        status_code: int, 
        headers: dict = None
    ) -> None:
        
        self.body = body
        self.headers = headers
        self.status_code = status_code
