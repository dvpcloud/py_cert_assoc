class Employee:

    default_db_file="test_employee_file.txt"
    def __init__(self, name, email_address, title, phone_number=None,identifier=None):
        self.name = name
        self.email_address = email_address
        self.title = title
        self.phone_number = phone_number
        self.identifier = identifier

    def email_signature(self, include_phone=False):
        signature = f"{self.name} - {self.title}\n{self.email_address}"
        if include_phone and self.phone_number:
            signature += f" ({self.phone_number})"
        return signature
    
    @classmethod
    def get_all(cls,filename=None):
        results = []

        if not filename:
            filename = cls.default_db_file
        
        with open(filename,"r") as file:            
            lines = [
                line.strip("\n").split(',') + [index+1]
                for index,line in enumerate(file.readlines())
            ]
        
        print(lines)

        for line in lines:
            results.append(cls(*line))

       

        return results
        
    @classmethod
    def get_at_line(cls,line_number,filename=None):
        if not filename:
            filename = cls.default_db_file
        with open(filename, "r") as f:
            line = f.readlines()[line_number -1]
            attrs = line.strip("\n").split(",") + [line_number]

        print(cls(*attrs))
        return cls(*attrs)

    def save(self,filename=None):
        if not filename:
            filename = self.default_db_file
        
        with open(filename,"r+") as f:
            lines = f.readlines()
            print(self.identifier)
            if self.identifier:
                lines[self.identifier - 1] = self._database_line()
            else:
                lines.append(self._database_line())
            print(lines)
            f.seek(0)
            f.writelines(lines)
        
    def _database_line(self):
        return (
            ",".join([self.name,self.email_address,self.title,self.phone_number or ""])
            + "\n"
        )


